from collections.abc import Sequence, Callable
from typing import Any, Final, overload, override, Literal

import numpy as np
from optype import numpy as onp

__all__ = [
    "ActionFinder",
    "ActionMapper",
    "Component",
    "Density",
    "DistributionFunction",
    "G",
    "GalaxyModel",
    "Potential",
    "SelectionFunction",
    "SelfConsistentModel",
    "Spline",
    "Target",
    "__version__",
    "actions",
    "getUnits",
    "ghMoments",
    "integrateNdim",
    "orbit",
    "readSnapshot",
    "sampleNdim",
    "setNumThreads",
    "setRandomSeed",
    "setUnits",
    "solveOpt",
    "splineApprox",
    "splineLogDensity",
    "writeSnapshot",
]

__version__: Final[str] = "1.0"
G: Final[float] = 1.0

type _AgamaCallable = Callable[
    [onp.Array2D[np.float64]], onp.Array1D[np.float32 | np.float64 | np.bool_]
]
type _ToPotential = Potential | _AgamaCallable
type _ToDensity = Density | _AgamaCallable
type _ToDistributionFunction = (
    DistributionFunction | _AgamaCallable | Sequence[_ToDistributionFunction]
)

class Density:
    @overload
    def __init__(self, cumulmass: onp.ToJustFloat64_2D) -> None: ...
    @overload
    def __init__(self, filename: str) -> None: ...
    @overload
    def __init__(self, *args: "Density") -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: str | None = None,
        density: str | None = None,
        mass: float | None = None,
        scaleradius: float | None = None,
        scaleheight: float | None = None,
        p: float | None = None,
        q: float | None = None,
        gamma: float | None = None,
        beta: float | None = None,
        alpha: float | None = None,
        sersicIndex: float | None = None,
        innercutoffradius: float | None = None,
        outercutoffradius: float | None = None,
        cutoffstrength: float | None = None,
        surfacedensity: float | None = None,
        densitynorm: float | None = None,
        w0: float | None = None,
        trunc: float | None = None,
        center: tuple[float, float, float] | str | None = None,
        orientation: tuple[float, float, float] | None = None,
        rotation: float | str | None = None,
        scale: tuple[float, float] | str | None = None,
    ) -> None: ...
    def density(
        self,
        xyz: tuple[float, float, float] | onp.ToJustFloat64_2D,
        t: float | onp.ToJustFloat64_1D | None = None,
    ) -> float | onp.Array1D[np.float64]: ...
    def projectedDensity(
        self, xyz: float | onp.ToJustFloat64_1D
    ) -> float | onp.Array1D[np.float64]: ...
    def export(self, filename: str) -> None: ...
    def sample(
        self,
        n: int,
        potential: "Potential | None" = None,
        beta: float | None = None,
        kappa: float | None = None,
    ) -> tuple[list[list[float]], list[float]]: ...
    def totalMass(self) -> float: ...
    def enclosedMass(self, r: float | Sequence[float]) -> float | list[float]: ...
    def principalAxes(
        self, r: float | onp.ToJustFloat64_1D | None = None
    ) -> tuple[list[float], list[float]]: ...
    def name(self) -> str: ...
    def __getitem__(self, index: int) -> "Density | Potential": ...
    def __len__(self) -> int: ...
    def __add__(self, other: "Density") -> "Density": ...

class Potential(Density):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def potential(self, *args: Any, **kwargs: Any) -> Any: ...
    def force(self, *args: Any, **kwargs: Any) -> Any: ...

class ActionFinder:
    def __init__(self, potential: _ToPotential, interp: bool = False) -> None: ...
    @override
    def __repr__(self) -> str: ...

    # Call overloads
    # Default-compatible overloads
    @overload
    def __call__(
        self,
        point: onp.Array2D[np.inexact],
        actions: Literal[True] = ...,
        angles: Literal[False] = ...,
        frequencies: Literal[False] = ...,
    ) -> onp.Array2D[np.float64]: ...
    @overload
    def __call__(
        self,
        point: onp.Array2D[np.inexact],
        actions: Literal[False],
        angles: Literal[False] = ...,
        frequencies: Literal[False] = ...,
    ) -> None: ...
    # 3. actions = False, angles = True, frequencies = `angles`
    @overload
    def __call__(
        self,
        point: onp.Array2D[np.inexact],
        actions: Literal[False],
        angles: Literal[True],
        frequencies: Literal[True] = ...,
    ) -> tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]]: ...
    # 4. actions = True, angles = True, frequencies = `angles`
    @overload
    def __call__(
        self,
        point: onp.Array2D[np.inexact],
        actions: Literal[True],
        angles: Literal[True],
        frequencies: Literal[True] = ...,
    ) -> tuple[
        onp.Array2D[np.float64], onp.Array2D[np.float64], onp.Array2D[np.float64]
    ]: ...
    # 5. actions = False, angles = False, frequencies = True
    @overload
    def __call__(
        self,
        point: onp.Array2D[np.inexact],
        actions: Literal[False],
        angles: Literal[False],
        frequencies: Literal[True],
    ) -> onp.Array2D[np.float64]: ...
    # 6. actions = True, angles = False, frequencies = True
    @overload
    def __call__(
        self,
        point: onp.Array2D[np.inexact],
        actions: Literal[True],
        angles: Literal[False],
        frequencies: Literal[True],
    ) -> tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]]: ...
    # 7. actions = False, angles = True, frequencies = False
    @overload
    def __call__(
        self,
        point: onp.Array2D[np.inexact],
        actions: Literal[False],
        angles: Literal[True],
        frequencies: Literal[False],
    ) -> onp.Array2D[np.float64]: ...
    # 8. actions = True, angles = True, frequencies = False
    @overload
    def __call__(
        self,
        point: onp.Array2D[np.inexact],
        actions: Literal[True],
        angles: Literal[True],
        frequencies: Literal[False],
    ) -> tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]]: ...
    @overload
    def __call__(
        self,
        point: onp.Array2D[np.inexact],
        actions: Literal[False],
        *,
        frequencies: Literal[True],
        angles: Literal[True] = ...,
    ) -> onp.Array2D[np.float64]: ...
    @overload
    def __call__(
        self,
        point: onp.Array2D[np.inexact],
        actions: Literal[True],
        *,
        frequencies: Literal[True],
        angles: Literal[True] = ...,
    ) -> tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]]: ...

class ActionMapper:
    def __init__(self, potential: _ToPotential, tol: float = ...) -> None: ...
    @override
    def __repr__(self) -> str: ...
    def __call__(
        self, point: onp.Array2D[np.inexact], frequencies: bool = False
    ) -> None: ...

class Component:
    @override
    def __repr__(self) -> str: ...
    # Only potential
    @overload
    def __init__(self, *, potential: _ToPotential) -> None: ...
    # Potential + density
    @overload
    def __init__(
        self, *, potential: _ToPotential, density: _ToDensity, disklike: bool
    ) -> None: ...
    # Spheroidal distribution function with optional density
    @overload
    def __init__(
        self,
        *,
        df: _ToDistributionFunction,
        disklike: Literal[False],
        density: _ToDensity = ...,
        rminSph: onp.ToFloat = ...,
        rmaxSph: onp.ToFloat = ...,
        sizeRadialSph: onp.ToInt = ...,
        lmaxAngularSph: onp.ToInt = ...,
        mmaxAngularSph: onp.ToInt = ...,
    ) -> None: ...
    # Disk-like distribution function with optional density
    @overload
    def __init__(
        self,
        *,
        df: _ToDistributionFunction,
        disklike: Literal[True],
        density: _ToDensity = ...,
        RminCyl: onp.ToFloat = ...,
        RmaxCyl: onp.ToFloat = ...,
        zminCyl: onp.ToFloat = ...,
        zmaxCyl: onp.ToFloat = ...,
        sizeRadialCyl: onp.ToInt = ...,
        sizeVerticalCyl: onp.ToInt = ...,
        mmaxAngularCyl: onp.ToInt = ...,
    ) -> None: ...
    # Spheroidal or disk-like (runtime) distribution function with optional density
    @overload
    def __init__(
        self,
        *,
        df: _ToDistributionFunction,
        disklike: bool,
        density: _ToDensity = ...,
        rminSph: onp.ToFloat = ...,
        rmaxSph: onp.ToFloat = ...,
        sizeRadialSph: onp.ToInt = ...,
        lmaxAngularSph: onp.ToInt = ...,
        mmaxAngularSph: onp.ToInt = ...,
        RminCyl: onp.ToFloat = ...,
        RmaxCyl: onp.ToFloat = ...,
        zminCyl: onp.ToFloat = ...,
        zmaxCyl: onp.ToFloat = ...,
        sizeRadialCyl: onp.ToInt = ...,
        sizeVerticalCyl: onp.ToInt = ...,
        mmaxAngularCyl: onp.ToInt = ...,
    ) -> None: ...

    # Properties
    @property
    def potential(self) -> Potential | None: ...
    @property
    def density(self) -> Density | None: ...
    @property
    def df(self) -> DistributionFunction | None: ...

class DistributionFunction: ...
class GalaxyModel: ...
class SelectionFunction: ...
class SelfConsistentModel: ...

class Spline:
    # x and y values are given
    # - der is optional
    # - quintic is optional
    @overload
    def __init__(
        self,
        x: onp.ToFloat1D,
        *,
        y: onp.ToFloat1D,
        der: onp.ToFloat1D = ...,
        quintic: onp.ToBool = ...,
    ) -> None: ...
    # x and y values are given
    # - der is not given
    # - if quintic is given it must be falsy
    @overload
    def __init__(
        self,
        x: onp.ToFloat1D,
        *,
        y: onp.ToFloat1D,
        left: onp.ToFloat = ...,
        right: onp.ToFloat = ...,
        reg: onp.ToFloat = ...,
        quintic: onp.ToFalse = ...,
    ) -> None: ...
    # Given ampl values
    @overload
    def __init__(
        self,
        x: onp.ToFloat1D,
        *,
        ampl: onp.ToFloat1D,
    ) -> None: ...
    # Default overload: Needed for when not explicitly using named arguments
    @overload
    def __init__(
        self,
        x: onp.ToFloat1D,
        y: onp.ToFloat1D = ...,
        der: onp.ToFloat1D = ...,
        ampl: onp.ToFloat1D = ...,
        left: onp.ToFloat = ...,
        right: onp.ToFloat = ...,
        reg: onp.ToInt = ...,
        quintic: onp.ToBool = ...,
    ) -> None: ...

    # __call__
    # Input is single number:
    # - conv must be spline if given
    # - can't be given der or ext
    @overload
    def __call__(self, x: float | int, *, conv: Spline = ...) -> None: ...
    # Input is single number:
    # - if using der or ext then conv can't be given
    @overload
    def __call__(
        self, x: float | int, *, der: onp.ToInt = ..., ext: onp.ToFloat = ...
    ) -> None: ...
    # Input is array
    # - conv must be scalar or array with same shape as `x` or `Spline`
    @overload
    def __call__(
        self, x: onp.ToFloatND, *, conv: onp.ToFloatND | Spline = ...
    ) -> None: ...
    # Input is array
    # - if using der or ext then conv can't be given
    @overload
    def __call__(
        self, x: onp.ToFloatND, *, der: onp.ToInt = ..., ext: onp.ToFloat = ...
    ) -> None: ...
    # Fallback overload
    @overload
    def __call__(
        self,
        x: object,
        der: onp.ToInt,
        ext: object,
        conv: object,
    ) -> None: ...

    # Overrides
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> float: ...
    @override
    def __repr__(self) -> str: ...

    # Methods
    def integrate(self, x1: float, x2: float, n: int | Spline = 0) -> float: ...
    def roots(
        self, y: float = 0, x1: float = ..., x2: float = ...
    ) -> onp.Array1D[np.float64]: ...
    def extrema(self, x1: float = ..., x2: float = ...) -> onp.Array1D[np.float64]: ...

class Target: ...

def readSnapshot(filename: str, /) -> Any: ...
def writeSnapshot(filename: str, particles: Any, format: str = "t") -> None: ...
def setUnits(**kwargs: Any) -> None: ...
def getUnits() -> dict[str, float]: ...
def setRandomSeed(seed: int) -> None: ...
def sampleNdim(fnc: Any, nsamples: int, **kwargs: Any) -> Any: ...
def integrateNdim(fnc: Any, nsamples: int, **kwargs: Any) -> Any: ...
def orbit(**kwargs: Any) -> Any: ...
def splineApprox(knots: Any, x: Any, y: Any, **kwargs: Any) -> Any: ...
def splineLogDensity(knots: Any, x: Any, **kwargs: Any) -> Any: ...
def solveOpt(**kwargs: Any) -> Any: ...
def ghMoments(
    degree: int, gridv: Any, matrix: Any, ghorder: int, **kwargs: Any
) -> Any: ...

class setNumThreads:
    def __init__(self, num_threads: int) -> None: ...
    def __enter__(self) -> "setNumThreads": ...
    def __exit__(self, *args: Any) -> None: ...

actions: ActionFinder
