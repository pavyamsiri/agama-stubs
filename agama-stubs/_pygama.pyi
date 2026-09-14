from collections.abc import Sequence
from typing import Any, Final, overload

import numpy as np
import optype as op
from optype import numpy as onp

from ._gala_support import GalaPotential as GalaPotential
from ._galaxy import Spline
from ._galpy_support import GalpyPotential as GalpyPotential

# NOTE: Should be astropy.units.Quantity but that will require a dependency on astropy.
# As astropy has relatively poor typing support we will not make that a mandatory dependency yet.
type _Quantity = Any

__all__: list[str] = [
    "CubicSpline",
    "GalaPotential",
    "GalpyPotential",
    "bsplineIntegrals",
    "bsplineInterp",
    "bsplineMatrix",
    "fromGalactictoICRS",
    "fromICRStoGalactic",
    "getCartesianCoords",
    "getCelestialCoords",
    "getEulerAngles",
    "getGalacticFromGalactocentric",
    "getGalactocentricFromGalactic",
    "getIntrinsicShape",
    "getProjectedEllipse",
    "getUnits",
    "getViewingAngles",
    "ghInterp",
    "makeCelestialRotationMatrix",
    "makeRotationMatrix",
    "nonuniformGrid",
    "sampleOrbitLibrary",
    "setUnits",
    "symmetricGrid",
    "transformCelestialCoords",
]

@overload
def setUnits() -> None: ...
@overload
def setUnits(
    *, mass: onp.ToFloat, length: onp.ToFloat, velocity: onp.ToFloat
) -> None: ...
@overload
def setUnits(*, mass: onp.ToFloat, length: onp.ToFloat, time: onp.ToFloat) -> None: ...
@overload
def setUnits(
    *, mass: onp.ToFloat, velocity: onp.ToFloat, time: onp.ToFloat
) -> None: ...
def getUnits() -> dict[str, float] | dict[str, _Quantity]: ...

# ``CubicSpline`` is a deprecated alias for ``Spline``.
# We just copied over ``Spline``'s `__init__` declarations to here.
# x and y values are ziven
# - der is optional
# - quintic is optional
@overload
def CubicSpline(
    x: onp.ToFloat1D,
    *,
    y: onp.ToFloat1D,
    der: onp.ToFloat1D = ...,
    quintic: onp.ToBool = ...,
) -> Spline: ...

# x and y values are given
# - der is not given
# - if quintic is given it must be falsy
@overload
def CubicSpline(
    x: onp.ToFloat1D,
    *,
    y: onp.ToFloat1D,
    left: onp.ToFloat = ...,
    right: onp.ToFloat = ...,
    reg: onp.ToFloat = ...,
    quintic: onp.ToFalse = ...,
) -> Spline: ...

# Given ampl values
@overload
def CubicSpline(
    x: onp.ToFloat1D,
    *,
    ampl: onp.ToFloat1D,
) -> Spline: ...

# Default overload: Needed for when not explicitly using named arguments
@overload
def CubicSpline(
    x: onp.ToFloat1D,
    y: onp.ToFloat1D = ...,
    der: onp.ToFloat1D = ...,
    ampl: onp.ToFloat1D = ...,
    left: onp.ToFloat = ...,
    right: onp.ToFloat = ...,
    reg: onp.ToInt = ...,
    quintic: onp.ToBool = ...,
) -> Spline: ...

# Grids
def nonuniformGrid(
    nnodes: onp.ToInt, xmin: onp.ToFloat, xmax: onp.ToFloat | None = None
) -> onp.Array1D[np.float64]: ...
def symmetricGrid(
    nnodes: onp.ToInt, xmin: onp.ToFloat, xmax: onp.ToFloat | None = None
) -> onp.Array1D[np.float64]: ...

# Routines for coordinate transformations
def makeRotationMatrix(
    alpha: onp.ToFloat, beta: onp.ToFloat, gamma: onp.ToFloat
) -> onp.Array2D[np.float64]: ...
def getEulerAngles(
    mat: onp.Array2D[np.floating],
) -> tuple[np.float64, np.float64, np.float64]: ...
def makeCelestialRotationMatrix(
    lon: onp.ToFloat, lat: onp.ToFloat, psi: onp.ToFloat
) -> onp.Array2D[np.float64]: ...

fromICRStoGalactic: Final[onp.Array2D[np.float64]]
fromGalactictoICRS: Final[onp.Array2D[np.float64]]

# No proper motions and no dispersion
@overload
def transformCelestialCoords[S: tuple[Any, ...]](
    rotationMatrix: onp.Array2D[np.floating],
    lon: onp.ArrayND[np.floating, S],
    lat: onp.ArrayND[np.floating, S],
    pmlon: None = None,
    pmlat: None = None,
    sigmalon: None = None,
    sigmalat: None = None,
    sigmacorr: None = None,
) -> tuple[
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
]: ...

# Proper motions but no dispersion
@overload
def transformCelestialCoords[S: tuple[Any, ...]](
    rotationMatrix: onp.Array2D[np.floating],
    lon: onp.ArrayND[np.floating, S],
    lat: onp.ArrayND[np.floating, S],
    pmlon: onp.ArrayND[np.floating, S],
    pmlat: onp.ArrayND[np.floating, S],
    sigmalon: None = None,
    sigmalat: None = None,
    sigmacorr: None = None,
) -> tuple[
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
]: ...

# Proper motions and dispersion provided
@overload
def transformCelestialCoords[S: tuple[Any, ...]](
    rotationMatrix: onp.Array2D[np.floating],
    lon: onp.ArrayND[np.floating, S],
    lat: onp.ArrayND[np.floating, S],
    pmlon: onp.ArrayND[np.floating, S],
    pmlat: onp.ArrayND[np.floating, S],
    sigmalon: onp.ArrayND[np.floating, S],
    sigmalat: onp.ArrayND[np.floating, S],
    sigmacorr: onp.ArrayND[np.floating, S],
) -> tuple[
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
]: ...

# Functions to transform between coordinate systems
@overload
def getCelestialCoords[S: tuple[Any, ...]](
    x: onp.ArrayND[np.floating, S],
    y: onp.ArrayND[np.floating, S],
    z: onp.ArrayND[np.floating, S],
    vx: None = None,
    vy: None = None,
    vz: None = None,
) -> tuple[
    onp.ArrayND[np.float64, S], onp.ArrayND[np.float64, S], onp.ArrayND[np.float64, S]
]: ...
@overload
def getCelestialCoords[S: tuple[Any, ...]](
    x: onp.ArrayND[np.floating, S],
    y: onp.ArrayND[np.floating, S],
    z: onp.ArrayND[np.floating, S],
    vx: onp.ArrayND[np.floating, S],
    vy: onp.ArrayND[np.floating, S],
    vz: onp.ArrayND[np.floating, S],
) -> tuple[
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
]: ...
@overload
def getCartesianCoords[S: tuple[Any, ...]](
    lon: onp.ArrayND[np.floating, S],
    lat: onp.ArrayND[np.floating, S],
    dist: onp.ArrayND[np.floating, S],
    pmlon: None = None,
    pmlat: None = None,
    vlos: None = None,
) -> tuple[
    onp.ArrayND[np.float64, S], onp.ArrayND[np.float64, S], onp.ArrayND[np.float64, S]
]: ...
@overload
def getCartesianCoords[S: tuple[Any, ...]](
    lon: onp.ArrayND[np.floating, S],
    lat: onp.ArrayND[np.floating, S],
    dist: onp.ArrayND[np.floating, S],
    pmlon: onp.ArrayND[np.floating, S],
    pmlat: onp.ArrayND[np.floating, S],
    vlos: onp.ArrayND[np.floating, S],
) -> tuple[
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
]: ...
@overload
def getGalacticFromGalactocentric[S: tuple[Any, ...]](
    x: onp.ArrayND[np.floating, S],
    y: onp.ArrayND[np.floating, S],
    z: onp.ArrayND[np.floating, S],
    vx: None = None,
    vy: None = None,
    vz: None = None,
    galcen_distance: onp.ToFloat = 8.122,
    galcen_v_sun: Sequence[onp.ToFloat] = (12.9, 245.6, 7.78),
    z_sun: onp.ToFloat = 0.0208,
) -> tuple[
    onp.ArrayND[np.float64, S], onp.ArrayND[np.float64, S], onp.ArrayND[np.float64, S]
]: ...
@overload
def getGalacticFromGalactocentric[S: tuple[Any, ...]](
    x: onp.ArrayND[np.floating, S],
    y: onp.ArrayND[np.floating, S],
    z: onp.ArrayND[np.floating, S],
    vx: onp.ArrayND[np.floating, S],
    vy: onp.ArrayND[np.floating, S],
    vz: onp.ArrayND[np.floating, S],
    galcen_distance: onp.ToFloat = 8.122,
    galcen_v_sun: Sequence[onp.ToFloat] = (12.9, 245.6, 7.78),
    z_sun: onp.ToFloat = 0.0208,
) -> tuple[
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
]: ...
@overload
def getGalactocentricFromGalactic[S: tuple[Any, ...]](
    lon: onp.ArrayND[np.floating, S],
    lat: onp.ArrayND[np.floating, S],
    dist: onp.ArrayND[np.floating, S],
    pmlon: None = None,
    pmlat: None = None,
    vlos: None = None,
    galcen_distance: onp.ToFloat = 8.122,
    galcen_v_sun: Sequence[onp.ToFloat] = (12.9, 245.6, 7.78),
    z_sun: onp.ToFloat = 0.0208,
) -> tuple[
    onp.ArrayND[np.float64, S], onp.ArrayND[np.float64, S], onp.ArrayND[np.float64, S]
]: ...
@overload
def getGalactocentricFromGalactic[S: tuple[Any, ...]](
    lon: onp.ArrayND[np.floating, S],
    lat: onp.ArrayND[np.floating, S],
    dist: onp.ArrayND[np.floating, S],
    pmlon: onp.ArrayND[np.floating, S],
    pmlat: onp.ArrayND[np.floating, S],
    vlos: onp.ArrayND[np.floating, S],
    galcen_distance: onp.ToFloat = 8.122,
    galcen_v_sun: Sequence[onp.ToFloat] = (12.9, 245.6, 7.78),
    z_sun: onp.ToFloat = 0.0208,
) -> tuple[
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
    onp.ArrayND[np.float64, S],
]: ...

# Ellipse
def getProjectedEllipse(
    Sx: onp.ToFloat,
    Sy: onp.ToFloat,
    Sz: onp.ToFloat,
    alpha: onp.ToFloat,
    beta: onp.ToFloat,
    gamma: onp.ToFloat,
) -> tuple[np.float64, np.float64, np.float64]: ...
def getIntrinsicShape(
    SXp: onp.ToFloat,
    SYp: onp.ToFloat,
    eta: onp.ToFloat,
    alpha: onp.ToFloat,
    beta: onp.ToFloat,
    gamma: onp.ToFloat,
) -> tuple[np.float64, np.float64, np.float64]: ...
def getViewingAngles(
    SXp: onp.ToFloat,
    SYp: onp.ToFloat,
    eta: onp.ToFloat,
    Sx: onp.ToFloat,
    Sy: onp.ToFloat,
    Sz: onp.ToFloat,
) -> tuple[
    tuple[np.float64, np.float64, np.float64],
    tuple[np.float64, np.float64, np.float64],
    tuple[np.float64, np.float64, np.float64],
    tuple[np.float64, np.float64, np.float64],
]: ...

### ------------------------------------------------------------------------------
### routines for representing a function specified in terms of its coefficients of
### B-spline or Gauss-Hermite expansions
@overload
def bsplineInterp(
    degree: onp.ToInt,
    grid: onp.Array1D[np.floating],
    ampl: onp.Array1D[np.floating],
    x: onp.ToFloat,
) -> np.floating: ...
@overload
def bsplineInterp(
    degree: onp.ToInt,
    grid: onp.Array1D[np.floating],
    ampl: onp.Array1D[np.floating],
    x: onp.Array1D[np.floating],
) -> onp.Array1D[np.float64]: ...
def bsplineIntegrals(
    degree: onp.ToInt,
    grid: onp.Array1D[np.floating],
    power: onp.ToInt = 0,
) -> onp.Array1D[np.float64]: ...
@overload
def bsplineMatrix(
    degree1: onp.ToInt,
    grid1: onp.Array1D[np.floating],
    degree2: None = None,
    grid2: None = None,
) -> onp.Array2D[np.float64]: ...
@overload
def bsplineMatrix(
    degree1: onp.ToInt,
    grid1: onp.Array1D[np.floating],
    degree2: onp.ToInt,
    grid2: onp.Array1D[np.floating],
) -> onp.Array2D[np.float64]: ...

# Gauss-Hermite
def ghInterp(
    ampl: onp.ToFloat,
    center: onp.ToFloat,
    width: onp.ToFloat,
    coefs: onp.Array1D[np.floating] | None,
    x: onp.Array1D[np.floating],
) -> onp.Array0D[np.floating] | onp.Array1D[np.floating]: ...

# Orbit library
@overload
def sampleOrbitLibrary(
    nbody: op.CanInt,
    orbits: onp.Array1D[np.object_],
    weights: onp.Array1D[np.floating],
    returnIndices: onp.ToFalse = False,
) -> tuple[onp.Array2D[np.float64], onp.Array1D[np.float64]]: ...
@overload
def sampleOrbitLibrary(
    nbody: op.CanInt,
    orbits: onp.Array1D[np.object_],
    weights: onp.Array1D[np.floating],
    returnIndices: onp.ToTrue,
) -> tuple[onp.Array2D[np.float64], onp.Array1D[np.float64], onp.Array1D[np.int_]]: ...
