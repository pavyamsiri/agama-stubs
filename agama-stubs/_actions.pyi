from typing import Literal, overload, override

import numpy as np
from optype import numpy as onp

from ._potential import _ToPotential

class ActionFinder:
    def __init__(self, potential: _ToPotential, interp: bool = False) -> None: ...
    @override
    def __repr__(self) -> str: ...

    # BEGIN GENERATED ACTION FINDER CALL OVERLOADS
    @overload
    def __call__(
        self,
        point: onp.Array1D[np.inexact],
        actions: Literal[False],
        angles: Literal[False] = ...,
        frequencies: Literal[False] = ...,
    ) -> None: ...
    @overload
    def __call__(
        self,
        point: onp.Array1D[np.inexact],
        actions: Literal[False],
        angles: Literal[False],
        frequencies: Literal[True],
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def __call__(
        self,
        point: onp.Array1D[np.inexact],
        actions: Literal[False],
        angles: Literal[True],
        frequencies: Literal[False],
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def __call__(
        self,
        point: onp.Array1D[np.inexact],
        actions: Literal[False],
        angles: Literal[True],
        frequencies: Literal[True] = ...,
    ) -> tuple[onp.Array1D[np.float64], onp.Array1D[np.float64]]: ...
    @overload
    def __call__(
        self,
        point: onp.Array1D[np.inexact],
        actions: Literal[True] = ...,
        angles: Literal[False] = ...,
        frequencies: Literal[False] = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def __call__(
        self,
        point: onp.Array1D[np.inexact],
        actions: Literal[True],
        angles: Literal[False],
        frequencies: Literal[True],
    ) -> tuple[onp.Array1D[np.float64], onp.Array1D[np.float64]]: ...
    @overload
    def __call__(
        self,
        point: onp.Array1D[np.inexact],
        actions: Literal[True],
        angles: Literal[True],
        frequencies: Literal[False],
    ) -> tuple[onp.Array1D[np.float64], onp.Array1D[np.float64]]: ...
    @overload
    def __call__(
        self,
        point: onp.Array1D[np.inexact],
        actions: Literal[True],
        angles: Literal[True],
        frequencies: Literal[True] = ...,
    ) -> tuple[
        onp.Array1D[np.float64], onp.Array1D[np.float64], onp.Array1D[np.float64]
    ]: ...
    @overload
    def __call__(
        self,
        point: onp.Array1D[np.inexact],
        actions: Literal[False],
        *,
        frequencies: Literal[True],
        angles: Literal[False] = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def __call__(
        self,
        point: onp.Array1D[np.inexact],
        actions: Literal[True] = ...,
        *,
        frequencies: Literal[True],
        angles: Literal[False] = ...,
    ) -> tuple[onp.Array1D[np.float64], onp.Array1D[np.float64]]: ...
    @overload
    def __call__(
        self,
        point: onp.Array2D[np.inexact],
        actions: Literal[False],
        angles: Literal[False] = ...,
        frequencies: Literal[False] = ...,
    ) -> None: ...
    @overload
    def __call__(
        self,
        point: onp.Array2D[np.inexact],
        actions: Literal[False],
        angles: Literal[False],
        frequencies: Literal[True],
    ) -> onp.Array2D[np.float64]: ...
    @overload
    def __call__(
        self,
        point: onp.Array2D[np.inexact],
        actions: Literal[False],
        angles: Literal[True],
        frequencies: Literal[False],
    ) -> onp.Array2D[np.float64]: ...
    @overload
    def __call__(
        self,
        point: onp.Array2D[np.inexact],
        actions: Literal[False],
        angles: Literal[True],
        frequencies: Literal[True] = ...,
    ) -> tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]]: ...
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
        actions: Literal[True],
        angles: Literal[False],
        frequencies: Literal[True],
    ) -> tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]]: ...
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
        actions: Literal[True],
        angles: Literal[True],
        frequencies: Literal[True] = ...,
    ) -> tuple[
        onp.Array2D[np.float64], onp.Array2D[np.float64], onp.Array2D[np.float64]
    ]: ...
    @overload
    def __call__(
        self,
        point: onp.Array2D[np.inexact],
        actions: Literal[False],
        *,
        frequencies: Literal[True],
        angles: Literal[False] = ...,
    ) -> onp.Array2D[np.float64]: ...
    @overload
    def __call__(
        self,
        point: onp.Array2D[np.inexact],
        actions: Literal[True] = ...,
        *,
        frequencies: Literal[True],
        angles: Literal[False] = ...,
    ) -> tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]]: ...
    # END GENERATED ACTION FINDER CALL OVERLOADS

class ActionMapper:
    def __init__(self, potential: _ToPotential, tol: float = ...) -> None: ...
    @override
    def __repr__(self) -> str: ...
    # BEGIN GENERATED ACTION MAPPER CALL OVERLOADS
    @overload
    def __call__(
        self, point: onp.Array1D[np.inexact], frequencies: Literal[False] = ...
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def __call__(
        self, point: onp.Array1D[np.inexact], frequencies: Literal[True]
    ) -> tuple[onp.Array1D[np.float64], onp.Array1D[np.float64]]: ...
    @overload
    def __call__(
        self, point: onp.Array2D[np.inexact], frequencies: Literal[False] = ...
    ) -> onp.Array2D[np.float64]: ...
    @overload
    def __call__(
        self, point: onp.Array2D[np.inexact], frequencies: Literal[True]
    ) -> tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]]: ...
    # END GENERATED ACTION MAPPER CALL OVERLOADS
