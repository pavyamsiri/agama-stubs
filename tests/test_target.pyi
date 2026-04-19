import agama
from typing import assert_type
from optype import numpy as onp
import numpy as np

# Initialization tests
gridr = np.array([0.1, 1.0, 10.0])
gridz = np.array([0.0, 1.0, 5.0])
gridv = np.linspace(-500, 500, 101)
gridx = np.linspace(-10, 10, 21)
aperture = np.array([[0,0], [0,1], [1,1], [1,0]], dtype=float)

t1 = agama.Target(type="DensityClassicTopHat", gridr=gridr, stripsPerPane=4)
assert_type(t1, agama.Target)

t2 = agama.Target(type="DensitySphHarm", gridr=gridr, lmax=2, mmax=2)
assert_type(t2, agama.Target)

t3 = agama.Target(type="DensityCylindricalLinear", gridr=gridr, gridz=gridz, mmax=4)
assert_type(t3, agama.Target)

t4 = agama.Target(type="KinemShell", gridr=gridr, degree=3)
assert_type(t4, agama.Target)

t5 = agama.Target(
    type="LOSVD",
    gridv=gridv,
    gridx=gridx,
    apertures=[aperture],
    degree=2,
    psf=0.5
)
assert_type(t5, agama.Target)

# Method tests
assert_type(t1.name(), str)
assert_type(len(t1), int)
assert_type(t1[0], str)

# Call tests
dens = agama.Density(type="dehnen", mass=1.0, scaleradius=1.0)
assert_type(t1(dens), onp.Array1D[np.float64])

# Orbit and GalaxyModel (mocking them as we only care about types)
gm: agama.GalaxyModel
assert_type(t1(gm), onp.Array1D[np.float64])

orb: agama.Orbit
assert_type(t1(orb), onp.Array1D[np.float64])

orbs = np.array([orb, orb], dtype=object)
assert_type(t1(orbs), onp.Array2D[np.float64])

# Particle array input
particles = (np.zeros((10, 6)), np.ones(10))
assert_type(t1(particles), onp.Array1D[np.float64])
