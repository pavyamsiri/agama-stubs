from typing import assert_type

import agama
import numpy as np

potential: agama.Potential
density: agama.Density
df: agama.DistributionFunction

assert_type(agama.Density(type="Plummer", mass=1, scaleRadius=2), agama.Density)
assert_type(agama.Density(type="Dehnen", mass=1, rscale=2, p=0.9, q=0.8), agama.Density)
assert_type(
    agama.Density(type="Disk", Sigma0=1, rscale=2, scaleRadius2=0.2), agama.Density
)

assert_type(
    agama.DistributionFunction(type="DoublePowerLaw", norm=1),
    agama.DistributionFunction,
)
assert_type(
    agama.DistributionFunction(type="Exponential", mass=1), agama.DistributionFunction
)
assert_type(
    agama.DistributionFunction(type="QuasiIsothermal", potential=potential, Sigma0=1),
    agama.DistributionFunction,
)
assert_type(
    agama.DistributionFunction(
        type="QuasiSpherical", potential=potential, density=density, beta0=0, r_a=2
    ),
    agama.DistributionFunction,
)

assert_type(agama.Component(potential=potential), agama.Component)
assert_type(agama.Component(density=density, disklike=True), agama.Component)
assert_type(
    agama.Component(df=df, disklike=False, rminSph=0.1, rmaxSph=10, sizeRadialSph=20),
    agama.Component,
)
assert_type(
    agama.Component(
        df=df,
        disklike=True,
        RminCyl=0.1,
        RmaxCyl=10,
        zminCyl=0.1,
        zmaxCyl=5,
        sizeRadialCyl=20,
        sizeVerticalCyl=15,
    ),
    agama.Component,
)

grid = np.array([0.0, 1.0, 2.0])
apertures = np.array([[[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]]])
assert_type(agama.Target(type="DensityClassicTopHat", gridr=grid), agama.Target)
assert_type(agama.Target(type="DensitySphHarm", gridr=grid), agama.Target)
assert_type(
    agama.Target(type="DensityCylindricalLinear", gridr=grid, gridz=grid), agama.Target
)
assert_type(agama.Target(type="KinemShell", gridr=grid, degree=2), agama.Target)
assert_type(
    agama.Target(type="LOSVD", gridx=grid, gridv=grid, apertures=apertures, degree=1),
    agama.Target,
)
