from typing import assert_type

import agama
import numpy as np
from optype import numpy as onp

# Canonical names and the commonly used lowercase spellings are supported.
agama.Potential(type="Plummer", mass=1.0, scaleRadius=2.0, symmetry="spherical")
agama.Potential(type="plummer", mass=1.0, rscale=2.0)
agama.Potential(type="Logarithmic", v0=220.0, p=0.9, axisRatioZ=0.8)
agama.Potential(type="MiyamotoNagai", mass=1.0, scaleRadius=2.0, scaleRadius2=0.2)
agama.Potential(type="Plummer", symmetry="bisymmetric")
agama.Potential(type="Plummer", symmetry="reflection")
agama.Potential(type="Plummer", symmetry="none")

# Normalization aliases and mutually exclusive normalization families expand
# into distinct overloads.
agama.Potential(type="Disk", Sigma0=1.0, rscale=2.0, scaleHeight=0.2)
agama.Potential(type="Spheroid", rho0=1.0, scaleRadius=2.0, p=0.9, q=0.8)

# Expansion inputs are mutually exclusive source overloads.
density: agama.Density
potential: agama.Potential
agama.Potential(type="Multipole", density=density, lmax=4)
agama.Potential(type="Multipole", potential=potential, lmax=4)
agama.Potential(type="Multipole", file="coefficients.ini", lmax=4)

# Existing potentials and INI files can also be wrapped without a type.
agama.Potential(file="potential.ini", center=(1.0, 2.0, 3.0), symmetry="axisymmetric")
agama.Potential(potential=potential, rotation=0.5, symmetry="triaxial")

# eval results follow the selected flags and scalar/batched input rank.
point: onp.Array1D[np.float64]
points: onp.ToFloat2D
assert_type(potential.eval(point, pot=True), float)
assert_type(potential.eval(1, 2, 3, acc=True), onp.Array1D[np.float64])
assert_type(potential.eval(point, der=True), onp.Array1D[np.float64])
assert_type(
    potential.eval(point, pot=True, acc=True),
    tuple[float, onp.Array1D[np.float64]],
)
assert_type(
    potential.eval(point, pot=True, der=True),
    tuple[float, onp.Array1D[np.float64]],
)
assert_type(
    potential.eval(point, acc=True, der=True),
    tuple[onp.Array1D[np.float64], onp.Array1D[np.float64]],
)
assert_type(
    potential.eval(point, pot=True, acc=True, der=True),
    tuple[float, onp.Array1D[np.float64], onp.Array1D[np.float64]],
)
assert_type(potential.eval(points, pot=True), onp.Array1D[np.float64])
assert_type(potential.eval(points, acc=True, t=[0, 1]), onp.Array2D[np.float64])
assert_type(
    potential.eval(points, pot=True, acc=True, der=True),
    tuple[
        onp.Array1D[np.float64],
        onp.Array2D[np.float64],
        onp.Array2D[np.float64],
    ],
)
