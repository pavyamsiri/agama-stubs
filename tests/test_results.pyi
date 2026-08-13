from typing import assert_type

import agama
import numpy as np
from optype import numpy as onp

potential: agama.Potential
df: agama.DistributionFunction
mapper: agama.ActionMapper
model: agama.GalaxyModel
target: agama.Target

point2: onp.Array1D[np.float64]
points2: onp.Array2D[np.float64]
assert_type(potential.projectedEval(point2, pot=True), float)
assert_type(potential.projectedEval(1, 2, acc=True), onp.Array1D[np.float64])
assert_type(
    potential.projectedEval(points2, pot=True, acc=True, der=True),
    tuple[
        onp.Array1D[np.float64],
        onp.Array2D[np.float64],
        onp.Array2D[np.float64],
    ],
)

actions1: onp.Array1D[np.float64]
actions2: onp.Array2D[np.float64]
assert_type(mapper(actions1), onp.Array1D[np.float64])
assert_type(
    mapper(actions2, frequencies=True),
    tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]],
)
assert_type(df(actions1), float)
assert_type(
    df(actions2, der=True),
    tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]],
)

points3: onp.Array2D[np.float64]
assert_type(
    model.moments(points3),
    tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]],
)
assert_type(
    model.moments(points3, dens=False, vel=True, vel2=False, separate=True),
    onp.Array3D[np.float64],
)
assert_type(model.vdf(1, 2, 3), tuple[agama.Spline, agama.Spline, agama.Spline])
assert_type(
    model.vdf(points3, dens=True, separate=True),
    tuple[
        onp.Array2D[np.object_],
        onp.Array2D[np.object_],
        onp.Array2D[np.object_],
        onp.Array2D[np.float64],
    ],
)
projected_points: onp.Array2D[np.float64]
assert_type(model.projectedDF(projected_points), onp.Array1D[np.float64])
assert_type(model.projectedDF(projected_points, separate=True), onp.Array2D[np.float64])

ic: onp.Array1D[np.float64]
ics: onp.Array2D[np.float64]
assert_type(agama.orbit(potential=potential, ic=ic, time=1, dtype=object), agama.Orbit)
assert_type(
    agama.orbit(potential=potential, ic=ics, time=1, dtype=object),
    onp.Array1D[np.object_],
)
assert_type(
    agama.orbit(potential=potential, ic=ic, time=1, trajsize=10),
    onp.Array1D[np.object_],
)
assert_type(
    agama.orbit(
        potential=potential,
        ic=ics,
        time=[1, 2],
        trajsize=[10, 20],
        targets=target,
        der=True,
        lyapunov=True,
    ),
    tuple[
        onp.Array2D[np.float32],
        onp.Array2D[np.object_],
        onp.Array2D[np.object_],
        onp.Array2D[np.float64],
    ],
)
