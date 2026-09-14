from collections.abc import Callable, Sequence
from typing import Any, Literal, overload

import numpy as np
from optype import numpy as onp

from ._actions import ActionFinder
from ._galaxy import Target
from ._orbit import Orbit
from ._potential import _ToPotential

type _OrbitTargetScalar = onp.Array1D[np.float32]
type _OrbitTargetBatch = onp.Array2D[np.float32]
type _OrbitObjectScalar = onp.Array1D[np.object_]
type _OrbitObjectVector = onp.Array1D[np.object_]
type _OrbitObjectBatch = onp.Array2D[np.object_]
type _OrbitLyapunovScalar = onp.Array1D[np.float64]
type _OrbitLyapunovBatch = onp.Array2D[np.float64]
type _OrbitResultScalar = (
    _OrbitTargetScalar | Orbit | _OrbitObjectScalar | _OrbitLyapunovScalar
)
type _OrbitResultBatch = (
    _OrbitTargetBatch | _OrbitObjectVector | _OrbitObjectBatch | _OrbitLyapunovBatch
)

def readSnapshot(
    filename: str, /
) -> tuple[onp.Array2D[np.float64], onp.Array1D[np.float64]]: ...
def writeSnapshot(
    filename: str,
    particles: tuple[onp.ToFloat2D, onp.ToFloat1D],
    format: str = "t",
) -> None: ...
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
def getUnits() -> dict[str, float]: ...
def setRandomSeed(seed: int) -> None: ...

type _NdimCallable = Callable[[onp.Array2D[np.float64]], onp.ToFloat | onp.ToFloat1D]
type _SampleResult = tuple[onp.Array2D[np.float64], float, float, int]

@overload
def sampleNdim(fnc: _NdimCallable, nsamples: int, lower: int) -> _SampleResult: ...
@overload
def sampleNdim(
    fnc: _NdimCallable,
    nsamples: int,
    lower: onp.ToFloat1D,
    upper: onp.ToFloat1D,
) -> _SampleResult: ...
@overload
def integrateNdim(
    fnc: _NdimCallable,
    lower: int,
    *,
    toler: onp.ToFloat = ...,
    maxeval: onp.ToInt = ...,
) -> tuple[float, float, int]: ...
@overload
def integrateNdim(
    fnc: _NdimCallable,
    lower: onp.ToFloat1D,
    upper: onp.ToFloat1D,
    *,
    toler: onp.ToFloat = ...,
    maxeval: onp.ToInt = ...,
) -> tuple[float, float, int]: ...

# BEGIN GENERATED ORBIT OVERLOADS
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    trajsize: onp.ToInt,
    dtype: str | type[np.generic] = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> _OrbitObjectScalar: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    targets: Target,
    trajsize: onp.ToInt,
    dtype: str | type[np.generic] = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitTargetScalar, _OrbitObjectScalar]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    targets: Sequence[Target],
    trajsize: onp.ToInt,
    dtype: str | type[np.generic] = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitResultScalar, ...]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    trajsize: onp.ToInt,
    dtype: str | type[np.generic] = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitObjectScalar, _OrbitLyapunovScalar]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    targets: Target,
    trajsize: onp.ToInt,
    dtype: str | type[np.generic] = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitTargetScalar, _OrbitObjectScalar, _OrbitLyapunovScalar]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    targets: Sequence[Target],
    trajsize: onp.ToInt,
    dtype: str | type[np.generic] = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitResultScalar, ...]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    trajsize: onp.ToInt,
    dtype: str | type[np.generic] = ...,
    der: Literal[True],
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitObjectScalar, _OrbitObjectScalar]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    targets: Target,
    trajsize: onp.ToInt,
    dtype: str | type[np.generic] = ...,
    der: Literal[True],
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitTargetScalar, _OrbitObjectScalar, _OrbitObjectScalar]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    targets: Sequence[Target],
    trajsize: onp.ToInt,
    dtype: str | type[np.generic] = ...,
    der: Literal[True],
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitResultScalar, ...]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    trajsize: onp.ToInt,
    dtype: str | type[np.generic] = ...,
    der: Literal[True],
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitObjectScalar, _OrbitObjectScalar, _OrbitLyapunovScalar]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    targets: Target,
    trajsize: onp.ToInt,
    dtype: str | type[np.generic] = ...,
    der: Literal[True],
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[
    _OrbitTargetScalar, _OrbitObjectScalar, _OrbitObjectScalar, _OrbitLyapunovScalar
]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    targets: Sequence[Target],
    trajsize: onp.ToInt,
    dtype: str | type[np.generic] = ...,
    der: Literal[True],
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitResultScalar, ...]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    dtype: type[object],
    trajsize: onp.ToInt = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> Orbit: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    targets: Target,
    dtype: type[object],
    trajsize: onp.ToInt = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitTargetScalar, Orbit]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    targets: Sequence[Target],
    dtype: type[object],
    trajsize: onp.ToInt = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitResultScalar, ...]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    dtype: type[object],
    trajsize: onp.ToInt = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[Orbit, _OrbitLyapunovScalar]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    targets: Target,
    dtype: type[object],
    trajsize: onp.ToInt = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitTargetScalar, Orbit, _OrbitLyapunovScalar]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    targets: Sequence[Target],
    dtype: type[object],
    trajsize: onp.ToInt = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitResultScalar, ...]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    dtype: type[object],
    trajsize: onp.ToInt = ...,
    der: Literal[True],
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[Orbit, _OrbitObjectScalar]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    targets: Target,
    dtype: type[object],
    trajsize: onp.ToInt = ...,
    der: Literal[True],
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitTargetScalar, Orbit, _OrbitObjectScalar]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    targets: Sequence[Target],
    dtype: type[object],
    trajsize: onp.ToInt = ...,
    der: Literal[True],
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitResultScalar, ...]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    dtype: type[object],
    trajsize: onp.ToInt = ...,
    der: Literal[True],
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[Orbit, _OrbitObjectScalar, _OrbitLyapunovScalar]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    targets: Target,
    dtype: type[object],
    trajsize: onp.ToInt = ...,
    der: Literal[True],
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitTargetScalar, Orbit, _OrbitObjectScalar, _OrbitLyapunovScalar]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array1D[np.inexact] | Sequence[float],
    time: onp.ToFloat,
    targets: Sequence[Target],
    dtype: type[object],
    trajsize: onp.ToInt = ...,
    der: Literal[True],
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitResultScalar, ...]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    trajsize: onp.ToInt | onp.ToInt1D,
    dtype: str | type[np.generic] = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> _OrbitObjectBatch: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    targets: Target,
    trajsize: onp.ToInt | onp.ToInt1D,
    dtype: str | type[np.generic] = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitTargetBatch, _OrbitObjectBatch]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    targets: Sequence[Target],
    trajsize: onp.ToInt | onp.ToInt1D,
    dtype: str | type[np.generic] = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitResultBatch, ...]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    trajsize: onp.ToInt | onp.ToInt1D,
    dtype: str | type[np.generic] = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitObjectBatch, _OrbitLyapunovBatch]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    targets: Target,
    trajsize: onp.ToInt | onp.ToInt1D,
    dtype: str | type[np.generic] = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitTargetBatch, _OrbitObjectBatch, _OrbitLyapunovBatch]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    targets: Sequence[Target],
    trajsize: onp.ToInt | onp.ToInt1D,
    dtype: str | type[np.generic] = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitResultBatch, ...]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    trajsize: onp.ToInt | onp.ToInt1D,
    dtype: str | type[np.generic] = ...,
    der: Literal[True],
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitObjectBatch, _OrbitObjectBatch]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    targets: Target,
    trajsize: onp.ToInt | onp.ToInt1D,
    dtype: str | type[np.generic] = ...,
    der: Literal[True],
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitTargetBatch, _OrbitObjectBatch, _OrbitObjectBatch]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    targets: Sequence[Target],
    trajsize: onp.ToInt | onp.ToInt1D,
    dtype: str | type[np.generic] = ...,
    der: Literal[True],
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitResultBatch, ...]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    trajsize: onp.ToInt | onp.ToInt1D,
    dtype: str | type[np.generic] = ...,
    der: Literal[True],
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitObjectBatch, _OrbitObjectBatch, _OrbitLyapunovBatch]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    targets: Target,
    trajsize: onp.ToInt | onp.ToInt1D,
    dtype: str | type[np.generic] = ...,
    der: Literal[True],
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[
    _OrbitTargetBatch, _OrbitObjectBatch, _OrbitObjectBatch, _OrbitLyapunovBatch
]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    targets: Sequence[Target],
    trajsize: onp.ToInt | onp.ToInt1D,
    dtype: str | type[np.generic] = ...,
    der: Literal[True],
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitResultBatch, ...]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    dtype: type[object],
    trajsize: onp.ToInt | onp.ToInt1D = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> _OrbitObjectVector: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    targets: Target,
    dtype: type[object],
    trajsize: onp.ToInt | onp.ToInt1D = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitTargetBatch, _OrbitObjectVector]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    targets: Sequence[Target],
    dtype: type[object],
    trajsize: onp.ToInt | onp.ToInt1D = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitResultBatch, ...]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    dtype: type[object],
    trajsize: onp.ToInt | onp.ToInt1D = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitObjectVector, _OrbitLyapunovBatch]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    targets: Target,
    dtype: type[object],
    trajsize: onp.ToInt | onp.ToInt1D = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitTargetBatch, _OrbitObjectVector, _OrbitLyapunovBatch]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    targets: Sequence[Target],
    dtype: type[object],
    trajsize: onp.ToInt | onp.ToInt1D = ...,
    der: Literal[False] = ...,
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitResultBatch, ...]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    dtype: type[object],
    trajsize: onp.ToInt | onp.ToInt1D = ...,
    der: Literal[True],
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitObjectVector, _OrbitObjectBatch]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    targets: Target,
    dtype: type[object],
    trajsize: onp.ToInt | onp.ToInt1D = ...,
    der: Literal[True],
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitTargetBatch, _OrbitObjectVector, _OrbitObjectBatch]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    targets: Sequence[Target],
    dtype: type[object],
    trajsize: onp.ToInt | onp.ToInt1D = ...,
    der: Literal[True],
    lyapunov: Literal[False] = ...,
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitResultBatch, ...]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    dtype: type[object],
    trajsize: onp.ToInt | onp.ToInt1D = ...,
    der: Literal[True],
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitObjectVector, _OrbitObjectBatch, _OrbitLyapunovBatch]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    targets: Target,
    dtype: type[object],
    trajsize: onp.ToInt | onp.ToInt1D = ...,
    der: Literal[True],
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[
    _OrbitTargetBatch, _OrbitObjectVector, _OrbitObjectBatch, _OrbitLyapunovBatch
]: ...
@overload
def orbit(
    *,
    potential: _ToPotential,
    ic: onp.Array2D[np.inexact],
    time: onp.ToFloat | onp.ToFloat1D,
    targets: Sequence[Target],
    dtype: type[object],
    trajsize: onp.ToInt | onp.ToInt1D = ...,
    der: Literal[True],
    lyapunov: Literal[True],
    Omega: onp.ToFloat = ...,
    timestart: onp.ToFloat | onp.ToFloat1D = ...,
    accuracy: onp.ToFloat = ...,
    maxNumSteps: onp.ToInt = ...,
    method: Literal["dop853", "dprkn8", "hermite"] = ...,
    verbose: onp.ToBool = ...,
) -> tuple[_OrbitResultBatch, ...]: ...

# END GENERATED ORBIT OVERLOADS
def splineApprox(knots: Any, x: Any, y: Any, **kwargs: Any) -> Any: ...
def splineLogDensity(knots: Any, x: Any, **kwargs: Any) -> Any: ...
@overload
def solveOpt(
    matrix: onp.ToFloat2D,
    rhs: onp.ToFloat1D,
    *,
    xpenl: onp.ToFloat1D = ...,
    xpenq: onp.ToFloat2D = ...,
    rpenl: onp.ToFloat1D = ...,
    rpenq: onp.ToFloat1D = ...,
    xmin: onp.ToFloat1D = ...,
    xmax: onp.ToFloat1D = ...,
) -> onp.Array1D[np.float64]: ...
@overload
def solveOpt(
    matrix: Sequence[onp.ToFloat2D],
    rhs: Sequence[onp.ToFloat1D],
    *,
    xpenl: Sequence[onp.ToFloat1D] = ...,
    xpenq: Sequence[onp.ToFloat2D] = ...,
    rpenl: Sequence[onp.ToFloat1D] = ...,
    rpenq: Sequence[onp.ToFloat1D] = ...,
    xmin: onp.ToFloat1D = ...,
    xmax: onp.ToFloat1D = ...,
) -> onp.Array1D[np.float64]: ...
@overload
def ghMoments(
    *,
    degree: Literal[0, 1, 2, 3],
    gridv: onp.ToFloat1D,
    matrix: onp.Array1D[np.inexact],
    ghorder: onp.ToInt,
    ghbasis: onp.ToFloat2D = ...,
) -> onp.Array1D[np.float32]: ...
@overload
def ghMoments(
    *,
    degree: Literal[0, 1, 2, 3],
    gridv: onp.ToFloat1D,
    matrix: onp.Array2D[np.inexact],
    ghorder: onp.ToInt,
    ghbasis: onp.ToFloat2D = ...,
) -> onp.Array2D[np.float32]: ...

class setNumThreads:
    def __init__(self, num_threads: int) -> None: ...
    def __enter__(self) -> setNumThreads: ...
    def __exit__(self, *args: Any) -> None: ...

actions: ActionFinder
