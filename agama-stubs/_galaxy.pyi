from collections.abc import Sequence
from typing import Literal, overload, override

import numpy as np
from optype import numpy as onp

from ._actions import ActionFinder
from ._potential import Density, Potential, _AgamaCallable, _ToDensity, _ToPotential

type _ToDistributionFunction = (
    DistributionFunction | _AgamaCallable | Sequence[_ToDistributionFunction]
)
type _CallableSelectionFunction = SelectionFunction | _AgamaCallable

class Component:
    @override
    def __repr__(self) -> str: ...
    # BEGIN GENERATED COMPONENT INIT OVERLOADS
    @overload
    def __init__(self, *, potential: _ToPotential) -> None: ...
    @overload
    def __init__(
        self, *, density: _ToDensity, disklike: bool, potential: _ToPotential = ...
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        df: _ToDistributionFunction,
        disklike: Literal[False],
        density: _ToDensity = ...,
        rminSph: onp.ToFloat,
        rmaxSph: onp.ToFloat,
        sizeRadialSph: onp.ToInt,
        lmaxAngularSph: onp.ToInt = ...,
        mmaxAngularSph: onp.ToInt = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        df: _ToDistributionFunction,
        disklike: Literal[True],
        density: _ToDensity = ...,
        RminCyl: onp.ToFloat,
        RmaxCyl: onp.ToFloat,
        zminCyl: onp.ToFloat,
        zmaxCyl: onp.ToFloat,
        sizeRadialCyl: onp.ToInt,
        sizeVerticalCyl: onp.ToInt,
        mmaxAngularCyl: onp.ToInt = ...,
    ) -> None: ...
    # END GENERATED COMPONENT INIT OVERLOADS
    # Properties
    @property
    def potential(self) -> Potential | None: ...
    @property
    def density(self) -> Density | None: ...
    @property
    def df(self) -> DistributionFunction | None: ...

class DistributionFunction:
    # BEGIN GENERATED DISTRIBUTION_FUNCTION INIT OVERLOADS
    @overload
    def __init__(
        self,
        component: _ToDistributionFunction,
        /,
        *components: _ToDistributionFunction,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["DoublePowerLaw"],
        J0: onp.ToFloat = ...,
        Jcutoff: onp.ToFloat = ...,
        Jphi0: onp.ToFloat = ...,
        Jcore: onp.ToFloat = ...,
        slopeIn: onp.ToFloat = ...,
        slopeOut: onp.ToFloat = ...,
        steepness: onp.ToFloat = ...,
        coefJrIn: onp.ToFloat = ...,
        coefJzIn: onp.ToFloat = ...,
        coefJrOut: onp.ToFloat = ...,
        coefJzOut: onp.ToFloat = ...,
        rotFrac: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        norm: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["DoublePowerLaw"],
        J0: onp.ToFloat = ...,
        Jcutoff: onp.ToFloat = ...,
        Jphi0: onp.ToFloat = ...,
        Jcore: onp.ToFloat = ...,
        slopeIn: onp.ToFloat = ...,
        slopeOut: onp.ToFloat = ...,
        steepness: onp.ToFloat = ...,
        coefJrIn: onp.ToFloat = ...,
        coefJzIn: onp.ToFloat = ...,
        coefJrOut: onp.ToFloat = ...,
        coefJzOut: onp.ToFloat = ...,
        rotFrac: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Exponential"],
        Jr0: onp.ToFloat = ...,
        Jz0: onp.ToFloat = ...,
        Jphi0: onp.ToFloat = ...,
        addJden: onp.ToFloat = ...,
        addJvel: onp.ToFloat = ...,
        coefJr: onp.ToFloat = ...,
        coefJz: onp.ToFloat = ...,
        qJr: onp.ToFloat = ...,
        qJz: onp.ToFloat = ...,
        qJphi: onp.ToFloat = ...,
        norm: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Exponential"],
        Jr0: onp.ToFloat = ...,
        Jz0: onp.ToFloat = ...,
        Jphi0: onp.ToFloat = ...,
        addJden: onp.ToFloat = ...,
        addJvel: onp.ToFloat = ...,
        coefJr: onp.ToFloat = ...,
        coefJz: onp.ToFloat = ...,
        qJr: onp.ToFloat = ...,
        qJz: onp.ToFloat = ...,
        qJphi: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["QuasiIsothermal"],
        potential: _ToPotential,
        Rdisk: onp.ToFloat = ...,
        Hdisk: onp.ToFloat = ...,
        sigmar0: onp.ToFloat = ...,
        sigmaz0: onp.ToFloat = ...,
        sigmamin: onp.ToFloat = ...,
        Rsigmar: onp.ToFloat = ...,
        Rsigmaz: onp.ToFloat = ...,
        coefJr: onp.ToFloat = ...,
        coefJz: onp.ToFloat = ...,
        Jmin: onp.ToFloat = ...,
        qJr: onp.ToFloat = ...,
        qJz: onp.ToFloat = ...,
        qJphi: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["QuasiIsothermal"],
        potential: _ToPotential,
        Rdisk: onp.ToFloat = ...,
        Hdisk: onp.ToFloat = ...,
        sigmar0: onp.ToFloat = ...,
        sigmaz0: onp.ToFloat = ...,
        sigmamin: onp.ToFloat = ...,
        Rsigmar: onp.ToFloat = ...,
        Rsigmaz: onp.ToFloat = ...,
        coefJr: onp.ToFloat = ...,
        coefJz: onp.ToFloat = ...,
        Jmin: onp.ToFloat = ...,
        qJr: onp.ToFloat = ...,
        qJz: onp.ToFloat = ...,
        qJphi: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["QuasiSpherical"],
        potential: _ToPotential,
        density: _ToDensity = ...,
        rotFrac: onp.ToFloat = ...,
        Jphi0: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        anisotropyRadius: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["QuasiSpherical"],
        potential: _ToPotential,
        density: _ToDensity = ...,
        rotFrac: onp.ToFloat = ...,
        Jphi0: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        r_a: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["QuasiSpherical"],
        potential: _ToPotential,
        density: _ToDensity = ...,
        rotFrac: onp.ToFloat = ...,
        Jphi0: onp.ToFloat = ...,
        beta0: onp.ToFloat = ...,
        anisotropyRadius: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["QuasiSpherical"],
        potential: _ToPotential,
        density: _ToDensity = ...,
        rotFrac: onp.ToFloat = ...,
        Jphi0: onp.ToFloat = ...,
        beta0: onp.ToFloat = ...,
        r_a: onp.ToFloat = ...,
    ) -> None: ...
    # END GENERATED DISTRIBUTION_FUNCTION INIT OVERLOADS
    # Sequence methods
    def __len__(self) -> int: ...
    def __getitem__(self) -> int: ...

    # Hash
    @override
    def __hash__(self) -> int: ...

    # BEGIN GENERATED DISTRIBUTION FUNCTION CALL OVERLOADS
    @overload
    def __call__(
        self,
        jr: onp.ToFloat,
        jz: onp.ToFloat,
        jphi: onp.ToFloat,
        *,
        der: Literal[False] = ...,
    ) -> float: ...
    @overload
    def __call__(
        self,
        jr: onp.ToFloat,
        jz: onp.ToFloat,
        jphi: onp.ToFloat,
        *,
        der: Literal[True],
    ) -> tuple[float, onp.Array1D[np.float64]]: ...
    @overload
    def __call__(
        self,
        act: onp.Array1D[np.inexact],
        *,
        der: Literal[False] = ...,
    ) -> float: ...
    @overload
    def __call__(
        self,
        act: onp.Array1D[np.inexact],
        *,
        der: Literal[True],
    ) -> tuple[float, onp.Array1D[np.float64]]: ...
    @overload
    def __call__(
        self,
        act: onp.Array2D[np.inexact],
        *,
        der: Literal[False] = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def __call__(
        self,
        act: onp.Array2D[np.inexact],
        *,
        der: Literal[True],
    ) -> tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]]: ...
    # END GENERATED DISTRIBUTION FUNCTION CALL OVERLOADS
    # Methods
    def totalMass(self) -> float: ...
    def totalEntropy(self) -> float: ...

    # Comparison
    @override
    def __eq__(self, other: object) -> bool: ...
    @override
    def __ne__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...

class GalaxyModel:
    def __init__(
        self,
        potential: _ToPotential,
        df: _ToDistributionFunction,
        af: ActionFinder = ...,
        sf: _CallableSelectionFunction = ...,
    ) -> None: ...

    # Methods

    # BEGIN GENERATED GALAXY MODEL TOTAL MASS OVERLOADS
    @overload
    def totalMass(self, separate: Literal[False] = ...) -> float: ...
    @overload
    def totalMass(self, separate: Literal[True]) -> onp.Array1D[np.float64]: ...
    @overload
    def totalMass(self, separate: onp.ToBool) -> float | onp.Array1D[np.float64]: ...
    # END GENERATED GALAXY MODEL TOTAL MASS OVERLOADS
    # sample
    def sample(
        self, n: int, /
    ) -> tuple[onp.Array2D[np.float64], onp.Array1D[np.float64]]: ...
    # BEGIN GENERATED GALAXY MODEL MOMENTS OVERLOADS
    @overload
    def moments(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[False] = ...,
        vel2: Literal[False],
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> float: ...
    @overload
    def moments(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        dens: Literal[False],
        vel: Literal[True],
        vel2: Literal[False],
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def moments(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        dens: Literal[False],
        vel: Literal[False] = ...,
        vel2: Literal[True] = ...,
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def moments(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[True],
        vel2: Literal[False],
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[float, onp.Array1D[np.float64]]: ...
    @overload
    def moments(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[False] = ...,
        vel2: Literal[True] = ...,
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[float, onp.Array1D[np.float64]]: ...
    @overload
    def moments(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        dens: Literal[False],
        vel: Literal[True],
        vel2: Literal[True] = ...,
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array1D[np.float64], onp.Array1D[np.float64]]: ...
    @overload
    def moments(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[True],
        vel2: Literal[True] = ...,
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[float, onp.Array1D[np.float64], onp.Array1D[np.float64]]: ...
    @overload
    def moments(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[False] = ...,
        vel2: Literal[False],
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def moments(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        dens: Literal[False],
        vel: Literal[True],
        vel2: Literal[False],
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array2D[np.float64]: ...
    @overload
    def moments(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        dens: Literal[False],
        vel: Literal[False] = ...,
        vel2: Literal[True] = ...,
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array2D[np.float64]: ...
    @overload
    def moments(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[True],
        vel2: Literal[False],
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]]: ...
    @overload
    def moments(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[False] = ...,
        vel2: Literal[True] = ...,
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]]: ...
    @overload
    def moments(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        dens: Literal[False],
        vel: Literal[True],
        vel2: Literal[True] = ...,
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]]: ...
    @overload
    def moments(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[True],
        vel2: Literal[True] = ...,
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[
        onp.Array1D[np.float64], onp.Array2D[np.float64], onp.Array2D[np.float64]
    ]: ...
    @overload
    def moments(
        self,
        point: onp.Array1D[np.inexact] | Sequence[float],
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[False] = ...,
        vel2: Literal[False],
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> float: ...
    @overload
    def moments(
        self,
        point: onp.Array1D[np.inexact] | Sequence[float],
        /,
        *,
        dens: Literal[False],
        vel: Literal[True],
        vel2: Literal[False],
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def moments(
        self,
        point: onp.Array1D[np.inexact] | Sequence[float],
        /,
        *,
        dens: Literal[False],
        vel: Literal[False] = ...,
        vel2: Literal[True] = ...,
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def moments(
        self,
        point: onp.Array1D[np.inexact] | Sequence[float],
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[True],
        vel2: Literal[False],
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[float, onp.Array1D[np.float64]]: ...
    @overload
    def moments(
        self,
        point: onp.Array1D[np.inexact] | Sequence[float],
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[False] = ...,
        vel2: Literal[True] = ...,
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[float, onp.Array1D[np.float64]]: ...
    @overload
    def moments(
        self,
        point: onp.Array1D[np.inexact] | Sequence[float],
        /,
        *,
        dens: Literal[False],
        vel: Literal[True],
        vel2: Literal[True] = ...,
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array1D[np.float64], onp.Array1D[np.float64]]: ...
    @overload
    def moments(
        self,
        point: onp.Array1D[np.inexact] | Sequence[float],
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[True],
        vel2: Literal[True] = ...,
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[float, onp.Array1D[np.float64], onp.Array1D[np.float64]]: ...
    @overload
    def moments(
        self,
        point: onp.Array1D[np.inexact] | Sequence[float],
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[False] = ...,
        vel2: Literal[False],
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def moments(
        self,
        point: onp.Array1D[np.inexact] | Sequence[float],
        /,
        *,
        dens: Literal[False],
        vel: Literal[True],
        vel2: Literal[False],
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array2D[np.float64]: ...
    @overload
    def moments(
        self,
        point: onp.Array1D[np.inexact] | Sequence[float],
        /,
        *,
        dens: Literal[False],
        vel: Literal[False] = ...,
        vel2: Literal[True] = ...,
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array2D[np.float64]: ...
    @overload
    def moments(
        self,
        point: onp.Array1D[np.inexact] | Sequence[float],
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[True],
        vel2: Literal[False],
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]]: ...
    @overload
    def moments(
        self,
        point: onp.Array1D[np.inexact] | Sequence[float],
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[False] = ...,
        vel2: Literal[True] = ...,
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]]: ...
    @overload
    def moments(
        self,
        point: onp.Array1D[np.inexact] | Sequence[float],
        /,
        *,
        dens: Literal[False],
        vel: Literal[True],
        vel2: Literal[True] = ...,
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]]: ...
    @overload
    def moments(
        self,
        point: onp.Array1D[np.inexact] | Sequence[float],
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[True],
        vel2: Literal[True] = ...,
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[
        onp.Array1D[np.float64], onp.Array2D[np.float64], onp.Array2D[np.float64]
    ]: ...
    @overload
    def moments(
        self,
        points: onp.Array2D[np.inexact],
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[False] = ...,
        vel2: Literal[False],
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def moments(
        self,
        points: onp.Array2D[np.inexact],
        /,
        *,
        dens: Literal[False],
        vel: Literal[True],
        vel2: Literal[False],
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array2D[np.float64]: ...
    @overload
    def moments(
        self,
        points: onp.Array2D[np.inexact],
        /,
        *,
        dens: Literal[False],
        vel: Literal[False] = ...,
        vel2: Literal[True] = ...,
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array2D[np.float64]: ...
    @overload
    def moments(
        self,
        points: onp.Array2D[np.inexact],
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[True],
        vel2: Literal[False],
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]]: ...
    @overload
    def moments(
        self,
        points: onp.Array2D[np.inexact],
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[False] = ...,
        vel2: Literal[True] = ...,
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]]: ...
    @overload
    def moments(
        self,
        points: onp.Array2D[np.inexact],
        /,
        *,
        dens: Literal[False],
        vel: Literal[True],
        vel2: Literal[True] = ...,
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]]: ...
    @overload
    def moments(
        self,
        points: onp.Array2D[np.inexact],
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[True],
        vel2: Literal[True] = ...,
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[
        onp.Array1D[np.float64], onp.Array2D[np.float64], onp.Array2D[np.float64]
    ]: ...
    @overload
    def moments(
        self,
        points: onp.Array2D[np.inexact],
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[False] = ...,
        vel2: Literal[False],
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array2D[np.float64]: ...
    @overload
    def moments(
        self,
        points: onp.Array2D[np.inexact],
        /,
        *,
        dens: Literal[False],
        vel: Literal[True],
        vel2: Literal[False],
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array3D[np.float64]: ...
    @overload
    def moments(
        self,
        points: onp.Array2D[np.inexact],
        /,
        *,
        dens: Literal[False],
        vel: Literal[False] = ...,
        vel2: Literal[True] = ...,
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array3D[np.float64]: ...
    @overload
    def moments(
        self,
        points: onp.Array2D[np.inexact],
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[True],
        vel2: Literal[False],
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array2D[np.float64], onp.Array3D[np.float64]]: ...
    @overload
    def moments(
        self,
        points: onp.Array2D[np.inexact],
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[False] = ...,
        vel2: Literal[True] = ...,
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array2D[np.float64], onp.Array3D[np.float64]]: ...
    @overload
    def moments(
        self,
        points: onp.Array2D[np.inexact],
        /,
        *,
        dens: Literal[False],
        vel: Literal[True],
        vel2: Literal[True] = ...,
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array3D[np.float64], onp.Array3D[np.float64]]: ...
    @overload
    def moments(
        self,
        points: onp.Array2D[np.inexact],
        /,
        *,
        dens: Literal[True] = ...,
        vel: Literal[True],
        vel2: Literal[True] = ...,
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[
        onp.Array2D[np.float64], onp.Array3D[np.float64], onp.Array3D[np.float64]
    ]: ...
    # END GENERATED GALAXY MODEL MOMENTS OVERLOADS
    # BEGIN GENERATED GALAXY MODEL VDF OVERLOADS
    @overload
    def vdf(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        gridv: int | onp.ToFloat1D = ...,
        dens: Literal[False] = ...,
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[Spline, Spline, Spline]: ...
    @overload
    def vdf(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        gridv: int | onp.ToFloat1D = ...,
        dens: Literal[True],
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[Spline, Spline, Spline, float]: ...
    @overload
    def vdf(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        gridv: int | onp.ToFloat1D = ...,
        dens: Literal[False] = ...,
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[
        onp.Array1D[np.object_], onp.Array1D[np.object_], onp.Array1D[np.object_]
    ]: ...
    @overload
    def vdf(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        gridv: int | onp.ToFloat1D = ...,
        dens: Literal[True],
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[
        onp.Array1D[np.object_],
        onp.Array1D[np.object_],
        onp.Array1D[np.object_],
        onp.Array1D[np.float64],
    ]: ...
    @overload
    def vdf(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        /,
        *,
        gridv: int | onp.ToFloat1D = ...,
        dens: Literal[False] = ...,
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[Spline, Spline, Spline]: ...
    @overload
    def vdf(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        /,
        *,
        gridv: int | onp.ToFloat1D = ...,
        dens: Literal[True],
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[Spline, Spline, Spline, float]: ...
    @overload
    def vdf(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        /,
        *,
        gridv: int | onp.ToFloat1D = ...,
        dens: Literal[False] = ...,
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[
        onp.Array1D[np.object_], onp.Array1D[np.object_], onp.Array1D[np.object_]
    ]: ...
    @overload
    def vdf(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        /,
        *,
        gridv: int | onp.ToFloat1D = ...,
        dens: Literal[True],
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[
        onp.Array1D[np.object_],
        onp.Array1D[np.object_],
        onp.Array1D[np.object_],
        onp.Array1D[np.float64],
    ]: ...
    @overload
    def vdf(
        self,
        point: onp.Array1D[np.float64] | Sequence[float],
        /,
        *,
        gridv: int | onp.ToFloat1D = ...,
        dens: Literal[False] = ...,
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[Spline, Spline, Spline]: ...
    @overload
    def vdf(
        self,
        point: onp.Array1D[np.float64] | Sequence[float],
        /,
        *,
        gridv: int | onp.ToFloat1D = ...,
        dens: Literal[True],
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[Spline, Spline, Spline, float]: ...
    @overload
    def vdf(
        self,
        point: onp.Array1D[np.float64] | Sequence[float],
        /,
        *,
        gridv: int | onp.ToFloat1D = ...,
        dens: Literal[False] = ...,
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[
        onp.Array1D[np.object_], onp.Array1D[np.object_], onp.Array1D[np.object_]
    ]: ...
    @overload
    def vdf(
        self,
        point: onp.Array1D[np.float64] | Sequence[float],
        /,
        *,
        gridv: int | onp.ToFloat1D = ...,
        dens: Literal[True],
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[
        onp.Array1D[np.object_],
        onp.Array1D[np.object_],
        onp.Array1D[np.object_],
        onp.Array1D[np.float64],
    ]: ...
    @overload
    def vdf(
        self,
        points: onp.Array2D[np.float64],
        /,
        *,
        gridv: int | onp.ToFloat1D = ...,
        dens: Literal[False] = ...,
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[
        onp.Array1D[np.object_], onp.Array1D[np.object_], onp.Array1D[np.object_]
    ]: ...
    @overload
    def vdf(
        self,
        points: onp.Array2D[np.float64],
        /,
        *,
        gridv: int | onp.ToFloat1D = ...,
        dens: Literal[True],
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[
        onp.Array1D[np.object_],
        onp.Array1D[np.object_],
        onp.Array1D[np.object_],
        onp.Array1D[np.float64],
    ]: ...
    @overload
    def vdf(
        self,
        points: onp.Array2D[np.float64],
        /,
        *,
        gridv: int | onp.ToFloat1D = ...,
        dens: Literal[False] = ...,
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[
        onp.Array2D[np.object_], onp.Array2D[np.object_], onp.Array2D[np.object_]
    ]: ...
    @overload
    def vdf(
        self,
        points: onp.Array2D[np.float64],
        /,
        *,
        gridv: int | onp.ToFloat1D = ...,
        dens: Literal[True],
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[
        onp.Array2D[np.object_],
        onp.Array2D[np.object_],
        onp.Array2D[np.object_],
        onp.Array2D[np.float64],
    ]: ...
    # END GENERATED GALAXY MODEL VDF OVERLOADS
    # BEGIN GENERATED GALAXY MODEL PROJECTED DF OVERLOADS
    @overload
    def projectedDF(
        self,
        points: onp.Array2D[np.float64],
        /,
        *,
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def projectedDF(
        self,
        points: onp.Array2D[np.float64],
        /,
        *,
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array2D[np.float64]: ...
    @overload
    def projectedDF(
        self,
        X: onp.ToFloat,
        Y: onp.ToFloat,
        vX: onp.ToFloat,
        vY: onp.ToFloat,
        vZ: onp.ToFloat,
        evX: onp.ToFloat,
        evY: onp.ToFloat,
        evZ: onp.ToFloat,
        /,
        *,
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> float: ...
    @overload
    def projectedDF(
        self,
        X: onp.ToFloat,
        Y: onp.ToFloat,
        vX: onp.ToFloat,
        vY: onp.ToFloat,
        vZ: onp.ToFloat,
        evX: onp.ToFloat,
        evY: onp.ToFloat,
        evZ: onp.ToFloat,
        /,
        *,
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def projectedDF(
        self,
        point: onp.Array1D[np.float64] | Sequence[float],
        /,
        *,
        separate: Literal[False] = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> float: ...
    @overload
    def projectedDF(
        self,
        point: onp.Array1D[np.float64] | Sequence[float],
        /,
        *,
        separate: Literal[True],
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array1D[np.float64]: ...
    # END GENERATED GALAXY MODEL PROJECTED DF OVERLOADS
    # Properties
    @property
    def potential(self) -> Potential: ...
    @property
    def af(self) -> ActionFinder: ...
    @property
    def df(self) -> DistributionFunction: ...
    @property
    def sf(self) -> SelectionFunction: ...

class SelectionFunction:
    def __init__(
        self,
        point: onp.Array1D[np.float64] | Sequence[float],
        radius: onp.ToFloat,
        steepness: onp.ToFloat = ...,
    ) -> None: ...
    # Single point with single argument
    @overload
    def __call__(self, posvel: onp.Array1D[np.inexact]) -> float: ...
    # Single point with multiple arguments
    @overload
    def __call__(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        vx: onp.ToFloat,
        vy: onp.ToFloat,
        vz: onp.ToFloat,
    ) -> float: ...
    # Multiple points via 2D array
    @overload
    def __call__(self, posvel: onp.Array2D[np.inexact]) -> onp.Array1D[np.float64]: ...
    # Fallback
    @overload
    def __call__(
        self, posvel: onp.ToFloat1D | onp.ToFloat2D
    ) -> float | onp.Array1D[np.float64]: ...

class SelfConsistentModel: ...

class Spline:
    # x and y values are ziven
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

class Target:
    # BEGIN GENERATED TARGET INIT OVERLOADS
    @overload
    def __init__(
        self,
        *,
        type: Literal["DensityClassicTopHat", "DensityClassicLinear"],
        gridr: onp.ToFloat1D,
        stripsPerPane: onp.ToInt = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["DensitySphHarm"],
        gridr: onp.ToFloat1D,
        lmax: onp.ToInt = ...,
        mmax: onp.ToInt = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["DensityCylindricalTopHat", "DensityCylindricalLinear"],
        gridr: onp.ToFloat1D,
        gridz: onp.ToFloat1D,
        mmax: onp.ToInt = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["KinemShell"],
        gridr: onp.ToFloat1D,
        degree: Literal[0, 1, 2, 3],
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["LOSVD"],
        gridx: onp.ToFloat1D,
        gridv: onp.ToFloat1D,
        apertures: onp.ToFloat3D | Sequence[onp.ToFloat2D],
        degree: Literal[0, 1, 2, 3],
        gridy: onp.ToFloat1D = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        symmetry: str = ...,
        psf: onp.ToFloat | onp.ToFloat2D = ...,
        velpsf: onp.ToFloat = ...,
    ) -> None: ...
    # END GENERATED TARGET INIT OVERLOADS
