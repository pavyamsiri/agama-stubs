"""Declarative constructor specification for ``agama.Potential``.

Parameter aliases are alternatives: the generator emits separate overloads so a
type checker rejects calls that supply two synonymous names at once.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Parameter:
    annotation: str
    names: tuple[str, ...]


@dataclass(frozen=True)
class PotentialKind:
    names: tuple[str, ...]
    parameters: tuple[str, ...] = ()
    exclusive: tuple[tuple[str, ...], ...] = ()
    sources: tuple[str, ...] = ()


PARAMETERS = {
    "mass": Parameter("float", ("mass",)),
    "surface_density": Parameter("float", ("surfaceDensity", "Sigma0")),
    "density_norm": Parameter("float", ("densityNorm", "rho0")),
    "scale_radius": Parameter("float", ("scaleRadius", "rscale")),
    "scale_height": Parameter("float", ("scaleHeight", "scaleRadius2")),
    "inner_cutoff_radius": Parameter("float", ("innerCutoffRadius",)),
    "outer_cutoff_radius": Parameter("float", ("outerCutoffRadius",)),
    "v0": Parameter("float", ("v0",)),
    "omega": Parameter("float", ("Omega",)),
    "axis_ratio_y": Parameter("float", ("axisRatioY", "p")),
    "axis_ratio_z": Parameter("float", ("axisRatioZ", "q")),
    "alpha": Parameter("float", ("alpha",)),
    "beta": Parameter("float", ("beta",)),
    "gamma": Parameter("float", ("gamma",)),
    "modulation_amplitude": Parameter("float", ("modulationAmplitude",)),
    "cutoff_strength": Parameter("float", ("cutoffStrength", "xi")),
    "sersic_index": Parameter("float", ("sersicIndex",)),
    "w0": Parameter("float", ("W0",)),
    "trunc": Parameter("float", ("trunc",)),
    "binary_q": Parameter("float", ("binary_q",)),
    "binary_sma": Parameter("float", ("binary_sma",)),
    "binary_ecc": Parameter("float", ("binary_ecc",)),
    "binary_phase": Parameter("float", ("binary_phase",)),
    "grid_size_r": Parameter("int", ("gridSizeR",)),
    "grid_size_z": Parameter("int", ("gridSizeZ",)),
    "nmax": Parameter("int", ("nmax",)),
    "lmax": Parameter("int", ("lmax",)),
    "mmax": Parameter("int", ("mmax",)),
    "smoothing": Parameter("float", ("smoothing",)),
    "rmin": Parameter("float", ("rmin",)),
    "rmax": Parameter("float", ("rmax",)),
    "zmin": Parameter("float", ("zmin",)),
    "zmax": Parameter("float", ("zmax",)),
    "eta": Parameter("float", ("eta",)),
    "r0": Parameter("float", ("r0",)),
    "fix_order": Parameter("bool", ("fixOrder",)),
    "interp_linear": Parameter("bool", ("interpLinear", "linearInterp")),
}

MODIFIERS = {
    "center": "Sequence[float] | str",
    "orientation": "Sequence[float]",
    "rotation": "float | Sequence[float] | str",
    "scale": "Sequence[float] | str",
    "symmetry": "_Symmetry",
}

EXPANSION_PARAMETERS = (
    "grid_size_r",
    "grid_size_z",
    "nmax",
    "lmax",
    "mmax",
    "smoothing",
    "rmin",
    "rmax",
    "zmin",
    "zmax",
    "eta",
    "r0",
    "fix_order",
)

POTENTIALS = (
    PotentialKind(
        ("Logarithmic", "logarithmic"),
        ("v0", "scale_radius", "axis_ratio_y", "axis_ratio_z"),
    ),
    PotentialKind(("Harmonic", "harmonic"), ("omega", "axis_ratio_y", "axis_ratio_z")),
    PotentialKind(
        ("KeplerBinary", "keplerbinary"),
        ("mass", "binary_q", "binary_sma", "binary_ecc", "binary_phase"),
    ),
    PotentialKind(("NFW", "nfw"), ("mass", "scale_radius")),
    PotentialKind(("Plummer", "plummer"), ("mass", "scale_radius")),
    PotentialKind(
        ("Dehnen", "dehnen"),
        ("mass", "scale_radius", "gamma", "axis_ratio_y", "axis_ratio_z"),
    ),
    PotentialKind(
        ("Ferrers", "ferrers"), ("mass", "scale_radius", "axis_ratio_y", "axis_ratio_z")
    ),
    PotentialKind(("Isochrone", "isochrone"), ("mass", "scale_radius")),
    PotentialKind(
        ("MiyamotoNagai", "miyamotonagai"), ("mass", "scale_radius", "scale_height")
    ),
    PotentialKind(("King", "king"), ("mass", "scale_radius", "w0", "trunc")),
    PotentialKind(
        ("PerfectEllipsoid", "perfectellipsoid"),
        ("mass", "scale_radius", "axis_ratio_z"),
    ),
    PotentialKind(
        ("Disk", "disk"),
        (
            "mass",
            "surface_density",
            "scale_radius",
            "scale_height",
            "inner_cutoff_radius",
            "modulation_amplitude",
            "sersic_index",
            "lmax",
            "mmax",
        ),
        (("mass", "surface_density"),),
    ),
    PotentialKind(
        ("Spheroid", "spheroid"),
        (
            "mass",
            "density_norm",
            "scale_radius",
            "outer_cutoff_radius",
            "axis_ratio_y",
            "axis_ratio_z",
            "alpha",
            "beta",
            "gamma",
            "cutoff_strength",
            "lmax",
            "mmax",
        ),
        (("mass", "density_norm"),),
    ),
    PotentialKind(
        ("Nuker", "nuker"),
        (
            "mass",
            "surface_density",
            "scale_radius",
            "outer_cutoff_radius",
            "axis_ratio_y",
            "axis_ratio_z",
            "alpha",
            "beta",
            "gamma",
            "cutoff_strength",
            "lmax",
            "mmax",
        ),
        (("mass", "surface_density"),),
    ),
    PotentialKind(
        ("Sersic", "sersic"),
        (
            "mass",
            "surface_density",
            "scale_radius",
            "axis_ratio_y",
            "axis_ratio_z",
            "sersic_index",
            "lmax",
            "mmax",
        ),
        (("mass", "surface_density"),),
    ),
    PotentialKind(
        ("BasisSet", "basisset"),
        EXPANSION_PARAMETERS,
        sources=("density", "potential", "file", "particles"),
    ),
    PotentialKind(
        ("Multipole", "multipole"),
        EXPANSION_PARAMETERS,
        sources=("density", "potential", "file", "particles"),
    ),
    PotentialKind(
        ("CylSpline", "cylspline"),
        EXPANSION_PARAMETERS,
        sources=("density", "potential", "file", "particles"),
    ),
    PotentialKind(("UniformAcceleration", "uniformacceleration"), sources=("file",)),
    PotentialKind(("Evolving", "evolving"), ("interp_linear",), sources=("file",)),
)
