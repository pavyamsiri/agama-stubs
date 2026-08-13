from typing import Literal, overload, override

import numpy as np
from optype import numpy as onp

from ._potential import _ToPotential

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
