import agama
from typing import assert_type
from optype import numpy as onp
import numpy as np

gm: agama.GalaxyModel
point: onp.Array1D[np.float64]
x, y, z = 1.0, 2.0, 3.0

# single point as array, separate = False

# dens = True, vel = False, vel2 = True (default)
assert_type(gm.moments(point), tuple[float, onp.Array1D[np.float64]])
assert_type(
    gm.moments(point, dens=True, vel=False, vel2=True, separate=False),
    tuple[float, onp.Array1D[np.float64]],
)

# dens = True, vel = False, vel2 = False
assert_type(gm.moments(point, vel2=False), float)
assert_type(gm.moments(point, dens=True, vel=False, vel2=False, separate=False), float)

# dens = False, vel = False, vel2 = True
assert_type(
    gm.moments(point, dens=False, vel=False, vel2=True, separate=False),
    onp.Array1D[np.float64],
)

# dens = True, vel = True, vel2 = True
assert_type(
    gm.moments(point, vel=True),
    tuple[float, onp.Array1D[np.float64], onp.Array1D[np.float64]],
)
assert_type(
    gm.moments(point, dens=True, vel=True, vel2=True, separate=False),
    tuple[float, onp.Array1D[np.float64], onp.Array1D[np.float64]],
)

# dens = False, vel = True, vel2 = True
assert_type(
    gm.moments(point, dens=False, vel=True),
    tuple[onp.Array1D[np.float64], onp.Array1D[np.float64]],
)
assert_type(
    gm.moments(point, dens=False, vel=True, vel2=True, separate=False),
    tuple[onp.Array1D[np.float64], onp.Array1D[np.float64]],
)

# dens = True, vel = True, vel2 = False
assert_type(
    gm.moments(point, vel=True, vel2=False), tuple[float, onp.Array1D[np.float64]]
)
assert_type(
    gm.moments(point, dens=True, vel=True, vel2=False, separate=False),
    tuple[float, onp.Array1D[np.float64]],
)

# dens = False, vel = True, vel2 = False
assert_type(
    gm.moments(point, dens=False, vel=True, vel2=False), onp.Array1D[np.float64]
)
assert_type(
    gm.moments(point, dens=False, vel=True, vel2=False, separate=False),
    onp.Array1D[np.float64],
)

# single point as unpacked arguments (3 args), separate = False

# dens = True, vel = False, vel2 = True (default)
assert_type(gm.moments(x, y, z), tuple[float, onp.Array1D[np.float64]])
assert_type(
    gm.moments(x, y, z, dens=True, vel=False, vel2=True, separate=False),
    tuple[float, onp.Array1D[np.float64]],
)

# dens = True, vel = False, vel2 = False
assert_type(gm.moments(x, y, z, vel2=False), float)
assert_type(
    gm.moments(x, y, z, dens=True, vel=False, vel2=False, separate=False), float
)

# dens = False, vel = False, vel2 = True
assert_type(
    gm.moments(x, y, z, dens=False, vel=False, vel2=True, separate=False),
    onp.Array1D[np.float64],
)

# dens = True, vel = True, vel2 = True
assert_type(
    gm.moments(x, y, z, vel=True),
    tuple[float, onp.Array1D[np.float64], onp.Array1D[np.float64]],
)
assert_type(
    gm.moments(x, y, z, dens=True, vel=True, vel2=True, separate=False),
    tuple[float, onp.Array1D[np.float64], onp.Array1D[np.float64]],
)

# dens = False, vel = True, vel2 = True
assert_type(
    gm.moments(x, y, z, dens=False, vel=True),
    tuple[onp.Array1D[np.float64], onp.Array1D[np.float64]],
)
assert_type(
    gm.moments(x, y, z, dens=False, vel=True, vel2=True, separate=False),
    tuple[onp.Array1D[np.float64], onp.Array1D[np.float64]],
)

# dens = True, vel = True, vel2 = False
assert_type(
    gm.moments(x, y, z, vel=True, vel2=False), tuple[float, onp.Array1D[np.float64]]
)
assert_type(
    gm.moments(x, y, z, dens=True, vel=True, vel2=False, separate=False),
    tuple[float, onp.Array1D[np.float64]],
)

# dens = False, vel = True, vel2 = False
assert_type(
    gm.moments(x, y, z, dens=False, vel=True, vel2=False), onp.Array1D[np.float64]
)
assert_type(
    gm.moments(x, y, z, dens=False, vel=True, vel2=False, separate=False),
    onp.Array1D[np.float64],
)

# single point as unpacked arguments (2 args), separate = False

# dens = True, vel = False, vel2 = True (default)
assert_type(gm.moments(x, y), tuple[float, onp.Array1D[np.float64]])
assert_type(
    gm.moments(x, y, dens=True, vel=False, vel2=True, separate=False),
    tuple[float, onp.Array1D[np.float64]],
)

# dens = True, vel = False, vel2 = False
assert_type(gm.moments(x, y, vel2=False), float)
assert_type(gm.moments(x, y, dens=True, vel=False, vel2=False, separate=False), float)

# dens = False, vel = False, vel2 = True
assert_type(
    gm.moments(x, y, dens=False, vel=False, vel2=True, separate=False),
    onp.Array1D[np.float64],
)

# dens = True, vel = True, vel2 = True
assert_type(
    gm.moments(x, y, vel=True),
    tuple[float, onp.Array1D[np.float64], onp.Array1D[np.float64]],
)
assert_type(
    gm.moments(x, y, dens=True, vel=True, vel2=True, separate=False),
    tuple[float, onp.Array1D[np.float64], onp.Array1D[np.float64]],
)

# dens = False, vel = True, vel2 = True
assert_type(
    gm.moments(x, y, dens=False, vel=True),
    tuple[onp.Array1D[np.float64], onp.Array1D[np.float64]],
)
assert_type(
    gm.moments(x, y, dens=False, vel=True, vel2=True, separate=False),
    tuple[onp.Array1D[np.float64], onp.Array1D[np.float64]],
)

# dens = True, vel = True, vel2 = False
assert_type(
    gm.moments(x, y, vel=True, vel2=False), tuple[float, onp.Array1D[np.float64]]
)
assert_type(
    gm.moments(x, y, dens=True, vel=True, vel2=False, separate=False),
    tuple[float, onp.Array1D[np.float64]],
)

# dens = False, vel = True, vel2 = False
assert_type(gm.moments(x, y, dens=False, vel=True, vel2=False), onp.Array1D[np.float64])
assert_type(
    gm.moments(x, y, dens=False, vel=True, vel2=False, separate=False),
    onp.Array1D[np.float64],
)

# single point as array, separate = True

# dens = True, vel = False, vel2 = True (default)
assert_type(
    gm.moments(point, separate=True),
    tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]],
)
assert_type(
    gm.moments(point, dens=True, vel=False, vel2=True, separate=True),
    tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]],
)

# dens = True, vel = False, vel2 = False
assert_type(gm.moments(point, vel2=False, separate=True), onp.Array1D[np.float64])
assert_type(
    gm.moments(point, dens=True, vel=False, vel2=False, separate=True),
    onp.Array1D[np.float64],
)

# dens = False, vel = False, vel2 = True
assert_type(gm.moments(point, dens=False, separate=True), onp.Array2D[np.float64])
assert_type(
    gm.moments(point, dens=False, vel=False, vel2=True, separate=True),
    onp.Array2D[np.float64],
)

# dens = True, vel = True, vel2 = True
assert_type(
    gm.moments(point, vel=True, separate=True),
    tuple[onp.Array1D[np.float64], onp.Array2D[np.float64], onp.Array2D[np.float64]],
)
assert_type(
    gm.moments(point, dens=True, vel=True, vel2=True, separate=True),
    tuple[onp.Array1D[np.float64], onp.Array2D[np.float64], onp.Array2D[np.float64]],
)

# dens = False, vel = True, vel2 = True
assert_type(
    gm.moments(point, dens=False, vel=True, separate=True),
    tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]],
)
assert_type(
    gm.moments(point, dens=False, vel=True, vel2=True, separate=True),
    tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]],
)

# dens = True, vel = True, vel2 = False
assert_type(
    gm.moments(point, vel=True, vel2=False, separate=True),
    tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]],
)
assert_type(
    gm.moments(point, dens=True, vel=True, vel2=False, separate=True),
    tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]],
)

# dens = False, vel = True, vel2 = False
assert_type(
    gm.moments(point, dens=False, vel=True, vel2=False, separate=True),
    onp.Array2D[np.float64],
)
assert_type(
    gm.moments(point, dens=False, vel=True, vel2=False, separate=True),
    onp.Array2D[np.float64],
)

# single point as unpacked arguments (3 args), separate = True

# dens = True, vel = False, vel2 = True (default)
assert_type(
    gm.moments(x, y, z, separate=True),
    tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]],
)
assert_type(
    gm.moments(x, y, z, dens=True, vel=False, vel2=True, separate=True),
    tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]],
)

# dens = True, vel = False, vel2 = False
assert_type(gm.moments(x, y, z, vel2=False, separate=True), onp.Array1D[np.float64])
assert_type(
    gm.moments(x, y, z, dens=True, vel=False, vel2=False, separate=True),
    onp.Array1D[np.float64],
)

# dens = False, vel = False, vel2 = True
assert_type(gm.moments(x, y, z, dens=False, separate=True), onp.Array2D[np.float64])
assert_type(
    gm.moments(x, y, z, dens=False, vel=False, vel2=True, separate=True),
    onp.Array2D[np.float64],
)

# dens = True, vel = True, vel2 = True
assert_type(
    gm.moments(x, y, z, vel=True, separate=True),
    tuple[onp.Array1D[np.float64], onp.Array2D[np.float64], onp.Array2D[np.float64]],
)
assert_type(
    gm.moments(x, y, z, dens=True, vel=True, vel2=True, separate=True),
    tuple[onp.Array1D[np.float64], onp.Array2D[np.float64], onp.Array2D[np.float64]],
)

# dens = False, vel = True, vel2 = True
assert_type(
    gm.moments(x, y, z, dens=False, vel=True, separate=True),
    tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]],
)
assert_type(
    gm.moments(x, y, z, dens=False, vel=True, vel2=True, separate=True),
    tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]],
)

# dens = True, vel = True, vel2 = False
assert_type(
    gm.moments(x, y, z, vel=True, vel2=False, separate=True),
    tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]],
)
assert_type(
    gm.moments(x, y, z, dens=True, vel=True, vel2=False, separate=True),
    tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]],
)

# dens = False, vel = True, vel2 = False
assert_type(
    gm.moments(x, y, z, dens=False, vel=True, vel2=False, separate=True),
    onp.Array2D[np.float64],
)
assert_type(
    gm.moments(x, y, z, dens=False, vel=True, vel2=False, separate=True),
    onp.Array2D[np.float64],
)

# single point as unpacked arguments (2 args), separate = True

# dens = True, vel = False, vel2 = True (default)
assert_type(
    gm.moments(x, y, separate=True),
    tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]],
)
assert_type(
    gm.moments(x, y, dens=True, vel=False, vel2=True, separate=True),
    tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]],
)

# dens = True, vel = False, vel2 = False
assert_type(gm.moments(x, y, vel2=False, separate=True), onp.Array1D[np.float64])
assert_type(
    gm.moments(x, y, dens=True, vel=False, vel2=False, separate=True),
    onp.Array1D[np.float64],
)

# dens = False, vel = False, vel2 = True
assert_type(gm.moments(x, y, dens=False, separate=True), onp.Array2D[np.float64])
assert_type(
    gm.moments(x, y, dens=False, vel=False, vel2=True, separate=True),
    onp.Array2D[np.float64],
)

# dens = True, vel = True, vel2 = True
assert_type(
    gm.moments(x, y, vel=True, separate=True),
    tuple[onp.Array1D[np.float64], onp.Array2D[np.float64], onp.Array2D[np.float64]],
)
assert_type(
    gm.moments(x, y, dens=True, vel=True, vel2=True, separate=True),
    tuple[onp.Array1D[np.float64], onp.Array2D[np.float64], onp.Array2D[np.float64]],
)

# dens = False, vel = True, vel2 = True
assert_type(
    gm.moments(x, y, dens=False, vel=True, separate=True),
    tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]],
)
assert_type(
    gm.moments(x, y, dens=False, vel=True, vel2=True, separate=True),
    tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]],
)

# dens = True, vel = True, vel2 = False
assert_type(
    gm.moments(x, y, vel=True, vel2=False, separate=True),
    tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]],
)
assert_type(
    gm.moments(x, y, dens=True, vel=True, vel2=False, separate=True),
    tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]],
)

# dens = False, vel = True, vel2 = False
assert_type(
    gm.moments(x, y, dens=False, vel=True, vel2=False, separate=True),
    onp.Array2D[np.float64],
)
assert_type(
    gm.moments(x, y, dens=False, vel=True, vel2=False, separate=True),
    onp.Array2D[np.float64],
)

# vdf

# single point as 3 separate arguments (x, y, z)
# separate = False (default)
assert_type(gm.vdf(x, y, z), tuple[agama.Spline, agama.Spline, agama.Spline])
assert_type(
    gm.vdf(x, y, z, dens=False, separate=False),
    tuple[agama.Spline, agama.Spline, agama.Spline],
)

# separate = False, dens = True
assert_type(
    gm.vdf(x, y, z, dens=True), tuple[agama.Spline, agama.Spline, agama.Spline, float]
)
assert_type(
    gm.vdf(x, y, z, dens=True, separate=False),
    tuple[agama.Spline, agama.Spline, agama.Spline, float],
)

# separate = True, dens = False
assert_type(
    gm.vdf(x, y, z, separate=True),
    tuple[onp.Array1D[np.object_], onp.Array1D[np.object_], onp.Array1D[np.object_]],
)
assert_type(
    gm.vdf(x, y, z, separate=True, dens=False),
    tuple[onp.Array1D[np.object_], onp.Array1D[np.object_], onp.Array1D[np.object_]],
)

# separate = True, dens = True
assert_type(
    gm.vdf(x, y, z, separate=True, dens=True),
    tuple[
        onp.Array1D[np.object_],
        onp.Array1D[np.object_],
        onp.Array1D[np.object_],
        onp.Array1D[np.float64],
    ],
)

# single point as 2 separate arguments (x, y)
# separate = False (default)
assert_type(gm.vdf(x, y), tuple[agama.Spline, agama.Spline, agama.Spline])
assert_type(
    gm.vdf(x, y, dens=False, separate=False),
    tuple[agama.Spline, agama.Spline, agama.Spline],
)

# separate = False, dens = True
assert_type(
    gm.vdf(x, y, dens=True), tuple[agama.Spline, agama.Spline, agama.Spline, float]
)
assert_type(
    gm.vdf(x, y, dens=True, separate=False),
    tuple[agama.Spline, agama.Spline, agama.Spline, float],
)

# separate = True, dens = False
assert_type(
    gm.vdf(x, y, separate=True),
    tuple[onp.Array1D[np.object_], onp.Array1D[np.object_], onp.Array1D[np.object_]],
)
assert_type(
    gm.vdf(x, y, separate=True, dens=False),
    tuple[onp.Array1D[np.object_], onp.Array1D[np.object_], onp.Array1D[np.object_]],
)

# separate = True, dens = True
assert_type(
    gm.vdf(x, y, separate=True, dens=True),
    tuple[
        onp.Array1D[np.object_],
        onp.Array1D[np.object_],
        onp.Array1D[np.object_],
        onp.Array1D[np.float64],
    ],
)

# single point as 1D array
# separate = False (default)
assert_type(gm.vdf(point), tuple[agama.Spline, agama.Spline, agama.Spline])
assert_type(
    gm.vdf(point, dens=False, separate=False),
    tuple[agama.Spline, agama.Spline, agama.Spline],
)

# separate = False, dens = True
assert_type(
    gm.vdf(point, dens=True), tuple[agama.Spline, agama.Spline, agama.Spline, float]
)
assert_type(
    gm.vdf(point, dens=True, separate=False),
    tuple[agama.Spline, agama.Spline, agama.Spline, float],
)

# separate = True, dens = False
assert_type(
    gm.vdf(point, separate=True),
    tuple[onp.Array1D[np.object_], onp.Array1D[np.object_], onp.Array1D[np.object_]],
)
assert_type(
    gm.vdf(point, separate=True, dens=False),
    tuple[onp.Array1D[np.object_], onp.Array1D[np.object_], onp.Array1D[np.object_]],
)

# separate = True, dens = True
assert_type(
    gm.vdf(point, separate=True, dens=True),
    tuple[
        onp.Array1D[np.object_],
        onp.Array1D[np.object_],
        onp.Array1D[np.object_],
        onp.Array1D[np.float64],
    ],
)

# multiple points as 2D array
points: onp.Array2D[np.float64]
# separate = False (default)
assert_type(
    gm.vdf(points),
    tuple[onp.Array1D[np.object_], onp.Array1D[np.object_], onp.Array1D[np.object_]],
)
assert_type(
    gm.vdf(points, dens=False, separate=False),
    tuple[onp.Array1D[np.object_], onp.Array1D[np.object_], onp.Array1D[np.object_]],
)

# separate = False, dens = True
assert_type(
    gm.vdf(points, dens=True),
    tuple[
        onp.Array1D[np.object_],
        onp.Array1D[np.object_],
        onp.Array1D[np.object_],
        onp.Array1D[np.float64],
    ],
)
assert_type(
    gm.vdf(points, dens=True, separate=False),
    tuple[
        onp.Array1D[np.object_],
        onp.Array1D[np.object_],
        onp.Array1D[np.object_],
        onp.Array1D[np.float64],
    ],
)

# separate = True, dens = False
assert_type(
    gm.vdf(points, separate=True),
    tuple[onp.Array2D[np.object_], onp.Array2D[np.object_], onp.Array2D[np.object_]],
)
assert_type(
    gm.vdf(points, separate=True, dens=False),
    tuple[onp.Array2D[np.object_], onp.Array2D[np.object_], onp.Array2D[np.object_]],
)

# separate = True, dens = True
assert_type(
    gm.vdf(points, separate=True, dens=True),
    tuple[
        onp.Array2D[np.object_],
        onp.Array2D[np.object_],
        onp.Array2D[np.object_],
        onp.Array2D[np.float64],
    ],
)
