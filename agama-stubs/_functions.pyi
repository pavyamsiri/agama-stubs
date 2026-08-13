from collections.abc import Sequence
from typing import Any, Literal, overload

import numpy as np
from optype import numpy as onp

from ._actions import ActionFinder
from ._galaxy import Target
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

class Orbit:
    def __new__(cls) -> Orbit: ...
    @overload
    def __call__(self, time: onp.ToFloat, /) -> onp.Array1D[np.float64]: ...
    @overload
    def __call__(self, time: onp.ToFloat1D, /) -> onp.Array2D[np.float64]: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> float: ...

def readSnapshot(filename: str, /) -> Any: ...
def writeSnapshot(filename: str, particles: Any, format: str = "t") -> None: ...
def setUnits(**kwargs: Any) -> None: ...
def getUnits() -> dict[str, float]: ...
def setRandomSeed(seed: int) -> None: ...
def sampleNdim(fnc: Any, nsamples: int, **kwargs: Any) -> Any: ...
def integrateNdim(fnc: Any, nsamples: int, **kwargs: Any) -> Any: ...

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
def solveOpt(**kwargs: Any) -> Any: ...
def ghMoments(
    degree: int, gridv: Any, matrix: Any, ghorder: int, **kwargs: Any
) -> Any: ...

class setNumThreads:
    def __init__(self, num_threads: int) -> None: ...
    def __enter__(self) -> setNumThreads: ...
    def __exit__(self, *args: Any) -> None: ...

actions: ActionFinder
