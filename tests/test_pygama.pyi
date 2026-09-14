from typing import Any, assert_type

import agama
import numpy as np
from optype import numpy as onp

type _Vector = onp.Array1D[np.float64]
type _Matrix = onp.Array2D[np.float64]
type _Triple = tuple[_Vector, _Vector, _Vector]
type _Six = tuple[_Vector, _Vector, _Vector, _Vector, _Vector, _Vector]
type _Angles = tuple[np.float64, np.float64, np.float64]

v: _Vector
m: _Matrix
orbits: onp.Array1D[np.object_]

# Unit-system overloads and optional astropy quantities.
assert_type(agama.setUnits(), None)
assert_type(agama.setUnits(mass=1.0, length=1.0, velocity=1.0), None)
assert_type(agama.setUnits(mass=1.0, length=1.0, time=1.0), None)
assert_type(agama.setUnits(mass=1.0, velocity=1.0, time=1.0), None)
assert_type(agama.getUnits(), dict[str, float] | dict[str, Any])

# Deprecated spline factory: values, derivatives, boundary conditions, and amplitudes.
assert_type(agama.CubicSpline(v, v), agama.Spline)
assert_type(agama.CubicSpline(v, y=v), agama.Spline)
assert_type(agama.CubicSpline(v, y=v, der=v, quintic=True), agama.Spline)
assert_type(agama.CubicSpline(v, y=v, left=0.0, right=0.0, reg=True), agama.Spline)
assert_type(agama.CubicSpline(v, ampl=v), agama.Spline)

assert_type(agama.nonuniformGrid(10, 0.1), _Vector)
assert_type(agama.nonuniformGrid(10, 0.1, 10.0), _Vector)
assert_type(agama.symmetricGrid(11, 0.1), _Vector)
assert_type(agama.symmetricGrid(11, 0.1, xmax=10.0), _Vector)
assert_type(agama.makeRotationMatrix(0.1, 0.2, 0.3), _Matrix)
assert_type(agama.getEulerAngles(m), _Angles)
assert_type(agama.makeCelestialRotationMatrix(0.1, 0.2, 0.3), _Matrix)
assert_type(agama.fromICRStoGalactic, _Matrix)
assert_type(agama.fromGalactictoICRS, _Matrix)

# Coordinates alone, with proper motions, and with their uncertainties.
assert_type(agama.transformCelestialCoords(m, v, v), tuple[_Vector, _Vector])
assert_type(
    agama.transformCelestialCoords(m, v, v, pmlon=v, pmlat=v),
    tuple[_Vector, _Vector, _Vector, _Vector],
)
assert_type(
    agama.transformCelestialCoords(m, v, v, v, v, v, v, v),
    tuple[_Vector, _Vector, _Vector, _Vector, _Vector, _Vector, _Vector],
)
assert_type(agama.transformCelestialCoords(m, m, m), tuple[_Matrix, _Matrix])
assert_type(agama.getCelestialCoords(v, v, v), _Triple)
assert_type(agama.getCelestialCoords(v, v, v, vx=v, vy=v, vz=v), _Six)
assert_type(agama.getCartesianCoords(v, v, v), _Triple)
assert_type(agama.getCartesianCoords(v, v, v, pmlon=v, pmlat=v, vlos=v), _Six)
assert_type(agama.getGalacticFromGalactocentric(v, v, v), _Triple)
assert_type(
    agama.getGalacticFromGalactocentric(
        v,
        v,
        v,
        v,
        v,
        v,
        galcen_distance=8.0,
        galcen_v_sun=(10.0, 240.0, 8.0),
        z_sun=0.02,
    ),
    _Six,
)
assert_type(agama.getGalactocentricFromGalactic(v, v, v), _Triple)
assert_type(
    agama.getGalactocentricFromGalactic(v, v, v, v, v, v, galcen_distance=8.0), _Six
)
assert_type(agama.getCartesianCoords(m, m, m), tuple[_Matrix, _Matrix, _Matrix])
assert_type(agama.getCelestialCoords(m, m, m), tuple[_Matrix, _Matrix, _Matrix])

assert_type(agama.getProjectedEllipse(3.0, 2.0, 1.0, 0.2, 0.4, 0.6), _Angles)
assert_type(agama.getIntrinsicShape(2.5, 1.5, 0.2, 0.3, 0.4, 0.5), _Angles)
assert_type(
    agama.getViewingAngles(2.5, 1.5, 0.2, 3.0, 2.0, 1.0),
    tuple[_Angles, _Angles, _Angles, _Angles],
)

assert_type(agama.bsplineInterp(1, v, v, 0.5), np.floating)
assert_type(agama.bsplineInterp(1, v, v, v), _Vector)
assert_type(agama.bsplineIntegrals(3, v), _Vector)
assert_type(agama.bsplineIntegrals(3, v, power=2), _Vector)
assert_type(agama.bsplineMatrix(3, v), _Matrix)
assert_type(agama.bsplineMatrix(3, v, 1, v), _Matrix)
assert_type(
    agama.ghInterp(1.0, 0.0, 1.0, None, v),
    onp.Array0D[np.floating] | onp.Array1D[np.floating],
)
assert_type(
    agama.ghInterp(1.0, 0.0, 1.0, v, v),
    onp.Array0D[np.floating] | onp.Array1D[np.floating],
)
assert_type(agama.sampleOrbitLibrary(100, orbits, v), tuple[_Matrix, _Vector])
assert_type(agama.sampleOrbitLibrary(100, orbits, v, False), tuple[_Matrix, _Vector])
assert_type(
    agama.sampleOrbitLibrary(100, orbits, v, returnIndices=True),
    tuple[_Matrix, _Vector, onp.Array1D[np.int_]],
)
