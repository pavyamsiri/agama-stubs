"""Declarative schemas for non-Potential dynamic constructors."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Argument:
    name: str
    annotation: str
    required: bool = False


@dataclass(frozen=True)
class ConstructorVariant:
    discriminator: tuple[str, ...]
    arguments: tuple[Argument, ...]
    exclusive_aliases: tuple[tuple[Argument, ...], ...] = ()


F = "onp.ToFloat"
INT = "onp.ToInt"

DENSITIES = (
    ConstructorVariant(
        ("Plummer", "plummer", "NFW", "nfw", "Isochrone", "isochrone"),
        (Argument("mass", F), Argument("scaleRadius", F)),
        (
            (
                Argument("scaleRadius", F),
                Argument("scaleradius", F),
                Argument("rscale", F),
            ),
        ),
    ),
    ConstructorVariant(
        ("Dehnen", "dehnen"),
        (
            Argument("mass", F),
            Argument("gamma", F),
            Argument("scaleRadius", F),
            Argument("axisRatioY", F),
            Argument("axisRatioZ", F),
        ),
        (
            (
                Argument("scaleRadius", F),
                Argument("scaleradius", F),
                Argument("rscale", F),
            ),
            (Argument("axisRatioY", F), Argument("p", F)),
            (Argument("axisRatioZ", F), Argument("q", F)),
        ),
    ),
    ConstructorVariant(
        ("Ferrers", "ferrers"),
        (
            Argument("mass", F),
            Argument("scaleRadius", F),
            Argument("axisRatioY", F),
            Argument("axisRatioZ", F),
        ),
        (
            (
                Argument("scaleRadius", F),
                Argument("scaleradius", F),
                Argument("rscale", F),
            ),
            (Argument("axisRatioY", F), Argument("p", F)),
            (Argument("axisRatioZ", F), Argument("q", F)),
        ),
    ),
    ConstructorVariant(
        ("MiyamotoNagai", "miyamotonagai"),
        (Argument("mass", F), Argument("scaleRadius", F), Argument("scaleHeight", F)),
        (
            (
                Argument("scaleRadius", F),
                Argument("scaleradius", F),
                Argument("rscale", F),
            ),
            (Argument("scaleHeight", F), Argument("scaleRadius2", F)),
        ),
    ),
    ConstructorVariant(
        ("King", "king"),
        (
            Argument("mass", F),
            Argument("scaleRadius", F),
            Argument("W0", F),
            Argument("trunc", F),
        ),
        (
            (
                Argument("scaleRadius", F),
                Argument("scaleradius", F),
                Argument("rscale", F),
            ),
        ),
    ),
    ConstructorVariant(
        ("PerfectEllipsoid", "perfectellipsoid"),
        (Argument("mass", F), Argument("scaleRadius", F), Argument("axisRatioZ", F)),
        (
            (
                Argument("scaleRadius", F),
                Argument("scaleradius", F),
                Argument("rscale", F),
            ),
            (Argument("axisRatioZ", F), Argument("q", F)),
        ),
    ),
    ConstructorVariant(
        ("Disk", "disk"),
        (
            Argument("scaleRadius", F),
            Argument("scaleHeight", F),
            Argument("innerCutoffRadius", F),
            Argument("modulationAmplitude", F),
            Argument("sersicIndex", F),
        ),
        (
            (Argument("mass", F), Argument("surfaceDensity", F), Argument("Sigma0", F)),
            (
                Argument("scaleRadius", F),
                Argument("scaleradius", F),
                Argument("rscale", F),
            ),
            (Argument("scaleHeight", F), Argument("scaleRadius2", F)),
        ),
    ),
    ConstructorVariant(
        ("Spheroid", "spheroid"),
        (
            Argument("scaleRadius", F),
            Argument("outerCutoffRadius", F),
            Argument("alpha", F),
            Argument("beta", F),
            Argument("gamma", F),
            Argument("cutoffStrength", F),
            Argument("axisRatioY", F),
            Argument("axisRatioZ", F),
        ),
        (
            (Argument("mass", F), Argument("densityNorm", F), Argument("rho0", F)),
            (
                Argument("scaleRadius", F),
                Argument("scaleradius", F),
                Argument("rscale", F),
            ),
            (Argument("cutoffStrength", F), Argument("xi", F)),
            (Argument("axisRatioY", F), Argument("p", F)),
            (Argument("axisRatioZ", F), Argument("q", F)),
        ),
    ),
    ConstructorVariant(
        ("Nuker", "nuker"),
        (
            Argument("scaleRadius", F),
            Argument("outerCutoffRadius", F),
            Argument("alpha", F),
            Argument("beta", F),
            Argument("gamma", F),
            Argument("cutoffStrength", F),
            Argument("axisRatioY", F),
            Argument("axisRatioZ", F),
        ),
        (
            (Argument("mass", F), Argument("surfaceDensity", F), Argument("Sigma0", F)),
            (
                Argument("scaleRadius", F),
                Argument("scaleradius", F),
                Argument("rscale", F),
            ),
            (Argument("cutoffStrength", F), Argument("xi", F)),
            (Argument("axisRatioY", F), Argument("p", F)),
            (Argument("axisRatioZ", F), Argument("q", F)),
        ),
    ),
    ConstructorVariant(
        ("Sersic", "sersic"),
        (
            Argument("scaleRadius", F),
            Argument("sersicIndex", F),
            Argument("axisRatioY", F),
            Argument("axisRatioZ", F),
        ),
        (
            (Argument("mass", F), Argument("surfaceDensity", F), Argument("Sigma0", F)),
            (
                Argument("scaleRadius", F),
                Argument("scaleradius", F),
                Argument("rscale", F),
            ),
            (Argument("axisRatioY", F), Argument("p", F)),
            (Argument("axisRatioZ", F), Argument("q", F)),
        ),
    ),
)

DFS = (
    ConstructorVariant(
        ("DoublePowerLaw",),
        tuple(
            Argument(n, F)
            for n in (
                "J0",
                "Jcutoff",
                "Jphi0",
                "Jcore",
                "slopeIn",
                "slopeOut",
                "steepness",
                "coefJrIn",
                "coefJzIn",
                "coefJrOut",
                "coefJzOut",
                "rotFrac",
                "cutoffStrength",
            )
        ),
        ((Argument("norm", F), Argument("mass", F)),),
    ),
    ConstructorVariant(
        ("Exponential",),
        tuple(
            Argument(n, F)
            for n in (
                "Jr0",
                "Jz0",
                "Jphi0",
                "addJden",
                "addJvel",
                "coefJr",
                "coefJz",
                "qJr",
                "qJz",
                "qJphi",
            )
        ),
        ((Argument("norm", F), Argument("mass", F)),),
    ),
    ConstructorVariant(
        ("QuasiIsothermal",),
        (Argument("potential", "_ToPotential", True),)
        + tuple(
            Argument(n, F)
            for n in (
                "Rdisk",
                "Hdisk",
                "sigmar0",
                "sigmaz0",
                "sigmamin",
                "Rsigmar",
                "Rsigmaz",
                "coefJr",
                "coefJz",
                "Jmin",
                "qJr",
                "qJz",
                "qJphi",
            )
        ),
        ((Argument("Sigma0", F), Argument("mass", F)),),
    ),
    ConstructorVariant(
        ("QuasiSpherical",),
        (
            Argument("potential", "_ToPotential", True),
            Argument("density", "_ToDensity"),
            Argument("rotFrac", F),
            Argument("Jphi0", F),
        ),
        (
            (Argument("beta", F), Argument("beta0", F)),
            (Argument("anisotropyRadius", F), Argument("r_a", F)),
        ),
    ),
)

TARGETS = (
    ConstructorVariant(
        ("DensityClassicTopHat", "DensityClassicLinear"),
        (
            Argument("gridr", "onp.ToFloat1D", True),
            Argument("stripsPerPane", INT),
            Argument("axisRatioY", F),
            Argument("axisRatioZ", F),
        ),
    ),
    ConstructorVariant(
        ("DensitySphHarm",),
        (
            Argument("gridr", "onp.ToFloat1D", True),
            Argument("lmax", INT),
            Argument("mmax", INT),
        ),
    ),
    ConstructorVariant(
        ("DensityCylindricalTopHat", "DensityCylindricalLinear"),
        (
            Argument("gridr", "onp.ToFloat1D", True),
            Argument("gridz", "onp.ToFloat1D", True),
            Argument("mmax", INT),
        ),
    ),
    ConstructorVariant(
        ("KinemShell",),
        (
            Argument("gridr", "onp.ToFloat1D", True),
            Argument("degree", "Literal[0, 1, 2, 3]", True),
        ),
    ),
    ConstructorVariant(
        ("LOSVD",),
        (
            Argument("gridx", "onp.ToFloat1D", True),
            Argument("gridv", "onp.ToFloat1D", True),
            Argument("apertures", "onp.ToFloat3D | Sequence[onp.ToFloat2D]", True),
            Argument("degree", "Literal[0, 1, 2, 3]", True),
            Argument("gridy", "onp.ToFloat1D"),
            Argument("alpha", F),
            Argument("beta", F),
            Argument("gamma", F),
            Argument("symmetry", "str"),
            Argument("psf", "onp.ToFloat | onp.ToFloat2D"),
            Argument("velpsf", F),
        ),
    ),
)
