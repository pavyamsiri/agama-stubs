# agama-stubs

Type stubs for the [Agama](https://github.com/pavyamsiri/Agama/tree/uv) package.

## Installation

```bash
uv pip install agama-stubs
```

## Usage

These stubs are designed to provide type information for the `agama` package. Most type checkers (like Pyright or Mypy) will automatically discover and use them if they are installed in your environment.

## Classes Covered

The following top-level classes are included in these stubs:

- `ActionFinder`
- `ActionMapper`
- `Component`
- `Density`
- `DistributionFunction`
- `GalaxyModel`
- `Potential`
- `SelectionFunction`
- `SelfConsistentModel`
- `Spline`
- `Target`

And various top-level functions such as `readSnapshot`, `writeSnapshot`, `setUnits`, `orbit`, etc.

## Development

Install development dependencies with `just sync`. Run `just ready` while
developing to regenerate and format files before complete validation, or run
`just check` for a non-mutating check. The stubs and typing fixtures are checked
with BasedPyright, BasedMypy, ty, and Pyrefly.

Dynamic constructor overloads are generated because each runtime variant accepts
a different parameter set. Edit `scripts/potential_spec.py` for `Potential`, or
`scripts/constructor_spec.py` for `Density`, `DistributionFunction`, `Target`,
and `Component`, then run:

```bash
just generate
just check
```

The generators update only marked constructor sections. Methods outside those
sections remain handwritten and may be edited normally. Do not edit generated
constructor sections directly.
