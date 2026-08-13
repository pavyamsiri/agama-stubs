# C++ extension overload audit

This document inventories runtime-dispatched Python APIs that need overloads or
generated declarations. It is based on the `uv` branch of `../Agama` at commit
`219ab99`, primarily `interface/python/interface_python.cpp`. Line references
below refer to that checkout.

The audit distinguishes two mechanisms:

1. **Schema dispatch:** a discriminator selects which keyword names are legal.
   These APIs are good candidates for a declarative generator.
2. **Result dispatch:** literal flags, input rank, or dtype select the return
   tuple and array shapes. These usually need systematic overload generation,
   but not the same parameter schema as constructors.

## Recommended generator scope

Implementation status: constructor schemas for `Potential`, `Density`,
`DistributionFunction`, `Target`, and `Component` are generated. Result-dispatch
and shape/dtype-dispatch APIs remain audit-only and are intentionally deferred.

| Priority | API | Dispatch keys | Recommendation |
| --- | --- | --- | --- |
| P0 | `Potential.__init__` | source form, `type`, aliases | Existing constructor generator |
| P0 | `Target.__init__` | `type` | Add a discriminator schema |
| P0 | `DistributionFunction.__init__` | source form, `type` | Add a discriminator schema sourced from `src/df_factory.cpp` |
| P1 | `Density.__init__` | source form, `type`, aliases | Share parameter definitions with the potential schema |
| P1 | `Potential.eval`, `projectedEval` | `pot`, `acc`, `der`, input rank | Add a reusable flag-product generator |
| P1 | `ActionFinder.__call__`, `actions` | `actions`, `angles`, `frequencies`, input rank | Migrate existing handwritten overload products |
| P1 | `GalaxyModel.moments`, `vdf`, `projectedDF` | output flags, `separate`, input rank | Add a shape/flag generator |
| P2 | `Component.__init__` | static/DF source, `disklike` | Small declarative variant schema |
| P2 | `orbit` | `dtype`, `trajsize`, `der`, `lyapunov`, targets, input rank | Dedicated generator; combinatorics are unique |
| P3 | shape-polymorphic numerical methods | scalar vs batch input | Handwritten templates or a small rank generator |

## Schema-dispatched constructors

### `Potential.__init__`

Authoritative implementation: lines 2739–2930. The constructor has mutually
exclusive top-level forms:

- one positional filename;
- one or more positional `Potential`, compatible callable, or parameter-dict
  components;
- a positional compatible callable plus the sole keyword `symmetry`;
- keyword construction from `type=...` and type-specific parameters;
- keyword wrapping from `potential=...` plus modifiers;
- keyword loading from `file=...` without `type`.

Within keyword construction, `particles`, `file`, `density`, and `potential`
are source alternatives. The detailed potential parameter parsing and synonym
rejection live in `src/potential_factory.cpp` lines 45–465. This is already the
model for `scripts/potential_spec.py`.

Remaining schema work:

- expansion types with a string density model combine two discriminators:
  `type="Multipole"` (or another expansion) and `density="Dehnen"` (or another
  density model); density-model parameters must be added to that overload;
- case-insensitive runtime type names cannot be represented exhaustively with
  `Literal`; the spec should list canonical and supported conventional casing;
- required-at-runtime fields such as valid King and Ferrers parameters should
  be marked separately from fields that merely have parser defaults.

### `Density.__init__`

Authoritative implementation: lines 1850–1955. Forms are:

- `Density(cumulmass=...)`, including the positional equivalent;
- one positional filename;
- positional composition of existing densities;
- a compatible callable with `symmetry=...`;
- keyword construction selected by `type=...` or `density=...`.

Density keyword parsing uses the same factory parameter table as `Potential`.
The future schema should therefore reuse parameter and alias definitions instead
of maintaining an independent handwritten catch-all. `cumulmass`, callable,
filename, and composite forms should remain explicit overload templates.

### `DistributionFunction.__init__`

Authoritative Python wrapper: lines 4154–4240. Type-specific parsing is in
`src/df_factory.cpp`, especially lines 115–255. Top-level forms are:

- one or more positional existing DFs or compatible callables, producing a
  composite DF;
- keyword-only construction with a mandatory `type`;
- some types additionally consume `potential` and/or `density` objects.

Current discriminator values are:

- `DoublePowerLaw`;
- `Exponential`;
- `QuasiIsothermal`;
- `QuasiSpherical`.

Each type has a separate parameter parser in `df_factory.cpp`. This is the next
closest match to the potential generator: define reusable parameters, aliases,
required fields, exclusive normalization alternatives, and per-type membership.

### `Target.__init__`

Authoritative implementation: lines 7093–7270. `type` is mandatory and selects
the complete accepted keyword set:

| Type | Required data | Other accepted fields |
| --- | --- | --- |
| `DensityClassicTopHat` | `gridr` | `stripsPerPane`, `axisRatioY`, `axisRatioZ` |
| `DensityClassicLinear` | `gridr` | `stripsPerPane`, `axisRatioY`, `axisRatioZ` |
| `DensitySphHarm` | `gridr` | `lmax`, `mmax` |
| `DensityCylindricalTopHat` | `gridr`, `gridz` | `mmax` |
| `DensityCylindricalLinear` | `gridr`, `gridz` | `mmax` |
| `KinemShell` | `gridr`, `degree` | none |
| `LOSVD` | `gridx`, `gridv`, `apertures`, `degree` | `gridy`, `alpha`, `beta`, `gamma`, `symmetry`, `psf`, `velpsf` |

`degree` for `KinemShell` and `LOSVD` is restricted to `Literal[0, 1, 2, 3]`.
`LOSVD.psf` accepts either one float or a K×2 array. `apertures` accepts either
a 3D array of polygons or a sequence of independently sized N×2 polygons. This
constructor is an excellent generator candidate and currently has essentially
no usable declaration.

### `Component.__init__`

Authoritative implementation: lines 5441–5555. This is variant dispatch rather
than string dispatch:

- static potential: `potential` only;
- static density: `density`, mandatory `disklike`, optional `potential`;
- DF with `disklike=False`: mandatory `df`, optional `density`, plus spherical
  grid parameters;
- DF with `disklike=True`: mandatory `df`, optional `density`, plus cylindrical
  grid parameters.

The existing handwritten overloads already model this structure. A generator
would be useful only if constructor schemas are generalized beyond string types.

## Flag-dispatched result structures

### `Potential.eval` and `Potential.projectedEval`

Authoritative implementations: lines 3040–3227. Three boolean flags select a
non-empty ordered subset of results:

- `pot=True`: potential scalar/array;
- `acc=True`: acceleration vector/array;
- `der=True`: six Hessian components per point;
- multiple selected values are returned as a tuple in `pot`, `acc`, `der` order;
- all flags false raises `RuntimeError`.

Input rank independently selects scalar versus batch output. Runtime probes on
the installed extension confirmed:

| Input | `pot` | `acc` | `der` |
| --- | --- | --- | --- |
| one point | `float` | `(3,) float64 array` | `(6,) float64 array` |
| N points | `(N,) float64 array` | `(N,3) float64 array` | `(N,6) float64 array` |

This requires 7 flag combinations × 2 input-rank families for each method.
`projectedEval` has the same output selection with projected coordinate inputs
and optional orientation/time arrays. A shared flag-product generator is
preferable to 28 handwritten overloads.

### Action APIs

Authoritative implementations: lines 3589–3935.

`ActionFinder.__call__` and module-level `actions` use three flags. Defaults are
`actions=True`, `angles=False`, and `frequencies=angles`. The result is `None`,
one array, or a tuple of two/three arrays in actions/angles/frequencies order.
Scalar phase-space input produces triplets; batch input produces N×3 arrays.

`ActionMapper.__call__` uses `frequencies=False`. It returns mapped phase-space
coordinates alone, or `(coordinates, frequencies)` when true. Scalar and batch
inputs produce `(6,)`/`(3,)` or `(N,6)`/`(N,3)` arrays respectively. Its current
stub incorrectly returns only `None` and should be replaced.

### `DistributionFunction.__call__`

Authoritative implementation: lines 4311–4325. `der=False` returns DF values;
`der=True` returns `(values, derivatives)`. One action triplet produces a scalar
and a length-3 derivative; N triplets produce an N-vector and N×3 derivative
array. This is a compact handwritten overload set or a small flag/rank template.

### `GalaxyModel`

Authoritative implementations: lines 4786–5246.

- `totalMass(separate=False)` returns `float`; `separate=True` returns one value
  per DF component.
- `moments` combines `dens`, `vel`, `vel2`, and `separate`. Selected outputs are
  returned singly or in a tuple. Input may be unpacked coordinates, one point,
  or a batch. `separate` inserts a component dimension.
- `projectedDF` changes scalar/array rank with input rank and `separate`.
- `vdf` combines `dens` and `separate`; it always returns three velocity
  distribution functions and optionally density, with callable spline outputs
  for a single non-separated point and arrays otherwise.

These methods already account for most of the handwritten overload volume in
`_galaxy.pyi`. A generic schema should describe inputs, independent literal
flags, output ordering, and dimension transformations, then generate contiguous
overload groups.

## Shape- and dtype-dispatched APIs

These need overloads, but are weaker candidates for the constructor generator:

- `Density.density`, `projectedDensity`, `enclosedMass`, and `principalAxes`:
  scalar versus batched coordinates/radii control scalar and array results
  (lines 1999–2158).
- `Potential.potential`, `force`, deprecated `forceDeriv`, `Rcirc`, `Tcirc`,
  `Rmax`, and `Rperiapo`: scalar versus batch inputs control output ranks
  (lines 2952–3412). The current `potential` and `force` declarations use `Any`
  and are high-priority handwritten additions.
- `SelectionFunction.__call__`: one phase-space point returns a scalar; N points
  return an N-vector (lines 4536–4620).
- `Spline.__call__`: scalar/array input and derivative order select scalar/array
  outputs; `integrate`, `roots`, and `extrema` have simpler fixed results
  (lines 5988–6260).
- `Target.__call__`: input may be a density, galaxy model, orbit(s), or weighted
  particle array, with output rank depending on that input (lines 7281–7430).
- `integrateNdim` and `sampleNdim`: bounds are either an integer dimension or a
  pair of lower/upper arrays (lines 8679–8775). These require two input overloads
  but have fixed return structures.
- `solveOpt`: matrix/rhs may be a single pair or matching sequences of pairs;
  output remains a 1D array (lines 8434–8660).
- `ghMoments`: input matrix rank controls output rank (lines 8049–8245).

## Special case: `orbit`

Authoritative implementation: lines 7584–8035. Return structure depends on:

- one initial condition versus N initial conditions;
- presence and scalar/array value of `trajsize`;
- numeric versus object `dtype`;
- real versus complex trajectory dtype;
- number of `targets`;
- `der` and `lyapunov` flags.

This should not be folded into the constructor schema. It needs a dedicated
specification describing independently optional output columns. Start with
common cases (`trajsize` numeric arrays and `dtype=object`) before attempting the
full Cartesian product.

## Ordinary overloads and exclusions

- `setUnits` has four valid signatures: reset with no arguments, or `mass` plus
  exactly two of `length`, `velocity`, and `time` (lines 893–960). Handwritten
  overloads are clearer than generation.
- Methods with merely optional parameters but a fixed result do not need
  overloads.
- Runtime value constraints such as positive radii or matching array lengths
  belong in documentation/tests, not overload generation.
- Arbitrary case-insensitive strings cannot be modeled exactly with `Literal`;
  generated stubs should intentionally support documented spellings.

## Suggested schema evolution

Keep constructor and result schemas separate:

```text
constructor schema
  kinds -> accepted parameters, aliases, exclusive groups, required fields
  sources -> positional/keyword construction alternatives
  compositions -> expansion type + density-model type

result schema
  input families -> scalar, one array point, batch array
  flags -> literals, defaults, dependent defaults
  outputs -> ordered fields and shape transform for each input family
```

The next implementation step should be `Target.__init__`: it is self-contained,
has seven finite discriminator values, and will establish whether the existing
potential schema can be generalized cleanly before tackling the larger DF
factory and flag-product generators.
