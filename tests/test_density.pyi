import numpy as np
import agama
from typing import assert_type
from optype import numpy as onp

# Test different initialization methods
d1 = agama.Density(type="dehnen", mass=1.0, scaleradius=1.0)
assert_type(d1, agama.Density)

d2 = agama.Density(filename="some_file.ini")
assert_type(d2, agama.Density)

# Test with array-like (list of lists)
cumul_mass = [[0.1, 1.0], [0.2, 2.0]]
d3 = agama.Density(cumul_mass)
assert_type(d3, agama.Density)

# Test with numpy array
# Note: In .pyi files, we don't have runtime values, 
# so we declare variables with types to simulate them.
cumul_mass_np: onp.Array2D[np.float64]
d4 = agama.Density(cumul_mass_np)
assert_type(d4, agama.Density)

# Test adding densities
d5 = d1 + d2
assert_type(d5, agama.Density)

# --- Methods ---

d = agama.Density(type="plummer", mass=1.0, scaleradius=1.0)

# Scalar input
xyz_scalar: tuple[float, float, float]
rho_scalar = d.density(xyz_scalar)
# Based on the stub, this returns float | onp.Array1D[np.float64]
assert_type(rho_scalar, float | onp.Array1D[np.float64])

# Array input
xyz_array: onp.Array2D[np.float64]
rho_array = d.density(xyz_array)
assert_type(rho_array, float | onp.Array1D[np.float64])

# projectedDensity
rho_proj = d.projectedDensity(1.0)
assert_type(rho_proj, float | onp.Array1D[np.float64])

rho_proj_arr_in: onp.Array1D[np.float64]
rho_proj_arr = d.projectedDensity(rho_proj_arr_in)
assert_type(rho_proj_arr, float | onp.Array1D[np.float64])

# --- Properties ---

m_total = d.totalMass()
assert_type(m_total, float)

name = d.name()
assert_type(name, str)

length = len(d)
assert_type(length, int)
