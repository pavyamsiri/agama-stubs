from collections.abc import Callable, Sequence
from typing import Any, Literal, overload

import numpy as np
from optype import numpy as onp

type _AgamaCallable = Callable[
    [onp.Array2D[np.float64]], onp.Array1D[np.float32 | np.float64 | np.bool_]
]
type _Symmetry = Literal[
    "spherical",
    "axisymmetric",
    "triaxial",
    "bisymmetric",
    "reflection",
    "none",
    "s",
    "a",
    "t",
    "b",
    "r",
    "n",
]
type _ToPotential = Potential | _AgamaCallable
type _ToDensity = Density | _AgamaCallable

# NOTE: `Any` is necessary as AGAMA can take in a dictionary of parameters that can be float, str, int etc.
type _PotentialParams = dict[str, Any]

class Density:
    # BEGIN GENERATED DENSITY INIT OVERLOADS
    @overload
    def __init__(self, cumulmass: onp.ToJustFloat64_2D) -> None: ...
    @overload
    def __init__(self, filename: str) -> None: ...
    @overload
    def __init__(self, component: Density, /, *components: Density) -> None: ...
    @overload
    def __init__(self, density: _AgamaCallable, /, *, symmetry: _Symmetry) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Plummer", "plummer", "NFW", "nfw", "Isochrone", "isochrone"],
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Plummer", "plummer", "NFW", "nfw", "Isochrone", "isochrone"],
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Plummer", "plummer", "NFW", "nfw", "Isochrone", "isochrone"],
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Dehnen", "dehnen"],
        mass: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Dehnen", "dehnen"],
        mass: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Dehnen", "dehnen"],
        mass: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Dehnen", "dehnen"],
        mass: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Dehnen", "dehnen"],
        mass: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Dehnen", "dehnen"],
        mass: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Dehnen", "dehnen"],
        mass: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Dehnen", "dehnen"],
        mass: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Dehnen", "dehnen"],
        mass: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Dehnen", "dehnen"],
        mass: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Dehnen", "dehnen"],
        mass: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Dehnen", "dehnen"],
        mass: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Ferrers", "ferrers"],
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Ferrers", "ferrers"],
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Ferrers", "ferrers"],
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Ferrers", "ferrers"],
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Ferrers", "ferrers"],
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Ferrers", "ferrers"],
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Ferrers", "ferrers"],
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Ferrers", "ferrers"],
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Ferrers", "ferrers"],
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Ferrers", "ferrers"],
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Ferrers", "ferrers"],
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Ferrers", "ferrers"],
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["MiyamotoNagai", "miyamotonagai"],
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        scaleHeight: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["MiyamotoNagai", "miyamotonagai"],
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        scaleRadius2: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["MiyamotoNagai", "miyamotonagai"],
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        scaleHeight: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["MiyamotoNagai", "miyamotonagai"],
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        scaleRadius2: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["MiyamotoNagai", "miyamotonagai"],
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        scaleHeight: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["MiyamotoNagai", "miyamotonagai"],
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        scaleRadius2: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["King", "king"],
        mass: onp.ToFloat = ...,
        W0: onp.ToFloat = ...,
        trunc: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["King", "king"],
        mass: onp.ToFloat = ...,
        W0: onp.ToFloat = ...,
        trunc: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["King", "king"],
        mass: onp.ToFloat = ...,
        W0: onp.ToFloat = ...,
        trunc: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["PerfectEllipsoid", "perfectellipsoid"],
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["PerfectEllipsoid", "perfectellipsoid"],
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["PerfectEllipsoid", "perfectellipsoid"],
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["PerfectEllipsoid", "perfectellipsoid"],
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["PerfectEllipsoid", "perfectellipsoid"],
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["PerfectEllipsoid", "perfectellipsoid"],
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        innerCutoffRadius: onp.ToFloat = ...,
        modulationAmplitude: onp.ToFloat = ...,
        sersicIndex: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        scaleHeight: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        innerCutoffRadius: onp.ToFloat = ...,
        modulationAmplitude: onp.ToFloat = ...,
        sersicIndex: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        scaleRadius2: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        innerCutoffRadius: onp.ToFloat = ...,
        modulationAmplitude: onp.ToFloat = ...,
        sersicIndex: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        scaleHeight: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        innerCutoffRadius: onp.ToFloat = ...,
        modulationAmplitude: onp.ToFloat = ...,
        sersicIndex: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        scaleRadius2: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        innerCutoffRadius: onp.ToFloat = ...,
        modulationAmplitude: onp.ToFloat = ...,
        sersicIndex: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        scaleHeight: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        innerCutoffRadius: onp.ToFloat = ...,
        modulationAmplitude: onp.ToFloat = ...,
        sersicIndex: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        scaleRadius2: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        innerCutoffRadius: onp.ToFloat = ...,
        modulationAmplitude: onp.ToFloat = ...,
        sersicIndex: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        scaleHeight: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        innerCutoffRadius: onp.ToFloat = ...,
        modulationAmplitude: onp.ToFloat = ...,
        sersicIndex: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        scaleRadius2: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        innerCutoffRadius: onp.ToFloat = ...,
        modulationAmplitude: onp.ToFloat = ...,
        sersicIndex: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        scaleHeight: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        innerCutoffRadius: onp.ToFloat = ...,
        modulationAmplitude: onp.ToFloat = ...,
        sersicIndex: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        scaleRadius2: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        innerCutoffRadius: onp.ToFloat = ...,
        modulationAmplitude: onp.ToFloat = ...,
        sersicIndex: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        scaleHeight: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        innerCutoffRadius: onp.ToFloat = ...,
        modulationAmplitude: onp.ToFloat = ...,
        sersicIndex: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        scaleRadius2: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        innerCutoffRadius: onp.ToFloat = ...,
        modulationAmplitude: onp.ToFloat = ...,
        sersicIndex: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        scaleHeight: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        innerCutoffRadius: onp.ToFloat = ...,
        modulationAmplitude: onp.ToFloat = ...,
        sersicIndex: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        scaleRadius2: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        innerCutoffRadius: onp.ToFloat = ...,
        modulationAmplitude: onp.ToFloat = ...,
        sersicIndex: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        scaleHeight: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        innerCutoffRadius: onp.ToFloat = ...,
        modulationAmplitude: onp.ToFloat = ...,
        sersicIndex: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        scaleRadius2: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        innerCutoffRadius: onp.ToFloat = ...,
        modulationAmplitude: onp.ToFloat = ...,
        sersicIndex: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        scaleHeight: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        innerCutoffRadius: onp.ToFloat = ...,
        modulationAmplitude: onp.ToFloat = ...,
        sersicIndex: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        scaleRadius2: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        densityNorm: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        rho0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        cutoffStrength: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        outerCutoffRadius: onp.ToFloat = ...,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        xi: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        mass: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        surfaceDensity: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleRadius: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        scaleradius: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        axisRatioY: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        axisRatioZ: onp.ToFloat = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        sersicIndex: onp.ToFloat = ...,
        Sigma0: onp.ToFloat = ...,
        rscale: onp.ToFloat = ...,
        p: onp.ToFloat = ...,
        q: onp.ToFloat = ...,
    ) -> None: ...
    # END GENERATED DENSITY INIT OVERLOADS
    @overload
    def density(
        self,
        xyz: tuple[onp.ToFloat, onp.ToFloat, onp.ToFloat] | onp.Array1D[np.inexact],
        /,
        *,
        t: onp.ToFloat = ...,
    ) -> float: ...
    @overload
    def density(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        t: onp.ToFloat = ...,
    ) -> float: ...
    @overload
    def density(
        self,
        xyz: onp.ToFloat2D,
        /,
        *,
        t: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def projectedDensity(
        self,
        xy: tuple[onp.ToFloat, onp.ToFloat] | onp.Array1D[np.inexact],
        /,
        *,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        t: onp.ToFloat = ...,
    ) -> float: ...
    @overload
    def projectedDensity(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        /,
        *,
        alpha: onp.ToFloat = ...,
        beta: onp.ToFloat = ...,
        gamma: onp.ToFloat = ...,
        t: onp.ToFloat = ...,
    ) -> float: ...
    @overload
    def projectedDensity(
        self,
        xy: onp.ToFloat2D,
        /,
        *,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
        t: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array1D[np.float64]: ...
    def export(self, filename: str) -> None: ...
    def sample(
        self,
        n: int,
        potential: Potential | None = None,
        beta: float | None = None,
        kappa: float | None = None,
    ) -> tuple[list[list[float]], list[float]]: ...
    def totalMass(self) -> float: ...
    @overload
    def enclosedMass(self, r: onp.ToFloat, /) -> float: ...
    @overload
    def enclosedMass(self, r: onp.ToFloat1D, /) -> onp.Array1D[np.float64]: ...
    @overload
    def principalAxes(
        self, r: onp.ToFloat | None = ..., /
    ) -> tuple[onp.Array1D[np.float64], onp.Array1D[np.float64]]: ...
    @overload
    def principalAxes(
        self, r: onp.ToFloat1D, /
    ) -> tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]]: ...
    def name(self) -> str: ...
    def __getitem__(self, index: int) -> Density | Potential: ...
    def __len__(self) -> int: ...
    def __add__(self, other: Density) -> Density: ...

class Potential(Density):
    # BEGIN GENERATED POTENTIAL INIT OVERLOADS
    @overload
    def __init__(self, filename: str, /) -> None: ...
    @overload
    def __init__(
        self,
        component: _ToPotential | _PotentialParams,
        /,
        *components: _ToPotential | _PotentialParams,
    ) -> None: ...
    @overload
    def __init__(
        self, potential: _AgamaCallable, /, *, symmetry: _Symmetry
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        file: str,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        potential: _ToPotential,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Logarithmic", "logarithmic"],
        v0: float = ...,
        scaleRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Logarithmic", "logarithmic"],
        v0: float = ...,
        scaleRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Logarithmic", "logarithmic"],
        v0: float = ...,
        scaleRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Logarithmic", "logarithmic"],
        v0: float = ...,
        scaleRadius: float = ...,
        p: float = ...,
        q: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Logarithmic", "logarithmic"],
        v0: float = ...,
        rscale: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Logarithmic", "logarithmic"],
        v0: float = ...,
        rscale: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Logarithmic", "logarithmic"],
        v0: float = ...,
        rscale: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Logarithmic", "logarithmic"],
        v0: float = ...,
        rscale: float = ...,
        p: float = ...,
        q: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Harmonic", "harmonic"],
        Omega: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Harmonic", "harmonic"],
        Omega: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Harmonic", "harmonic"],
        Omega: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Harmonic", "harmonic"],
        Omega: float = ...,
        p: float = ...,
        q: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["KeplerBinary", "keplerbinary"],
        mass: float = ...,
        binary_q: float = ...,
        binary_sma: float = ...,
        binary_ecc: float = ...,
        binary_phase: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["NFW", "nfw"],
        mass: float = ...,
        scaleRadius: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["NFW", "nfw"],
        mass: float = ...,
        rscale: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Plummer", "plummer"],
        mass: float = ...,
        scaleRadius: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Plummer", "plummer"],
        mass: float = ...,
        rscale: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Dehnen", "dehnen"],
        mass: float = ...,
        scaleRadius: float = ...,
        gamma: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Dehnen", "dehnen"],
        mass: float = ...,
        scaleRadius: float = ...,
        gamma: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Dehnen", "dehnen"],
        mass: float = ...,
        scaleRadius: float = ...,
        gamma: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Dehnen", "dehnen"],
        mass: float = ...,
        scaleRadius: float = ...,
        gamma: float = ...,
        p: float = ...,
        q: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Dehnen", "dehnen"],
        mass: float = ...,
        rscale: float = ...,
        gamma: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Dehnen", "dehnen"],
        mass: float = ...,
        rscale: float = ...,
        gamma: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Dehnen", "dehnen"],
        mass: float = ...,
        rscale: float = ...,
        gamma: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Dehnen", "dehnen"],
        mass: float = ...,
        rscale: float = ...,
        gamma: float = ...,
        p: float = ...,
        q: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Ferrers", "ferrers"],
        mass: float = ...,
        scaleRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Ferrers", "ferrers"],
        mass: float = ...,
        scaleRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Ferrers", "ferrers"],
        mass: float = ...,
        scaleRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Ferrers", "ferrers"],
        mass: float = ...,
        scaleRadius: float = ...,
        p: float = ...,
        q: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Ferrers", "ferrers"],
        mass: float = ...,
        rscale: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Ferrers", "ferrers"],
        mass: float = ...,
        rscale: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Ferrers", "ferrers"],
        mass: float = ...,
        rscale: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Ferrers", "ferrers"],
        mass: float = ...,
        rscale: float = ...,
        p: float = ...,
        q: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Isochrone", "isochrone"],
        mass: float = ...,
        scaleRadius: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Isochrone", "isochrone"],
        mass: float = ...,
        rscale: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["MiyamotoNagai", "miyamotonagai"],
        mass: float = ...,
        scaleRadius: float = ...,
        scaleHeight: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["MiyamotoNagai", "miyamotonagai"],
        mass: float = ...,
        scaleRadius: float = ...,
        scaleRadius2: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["MiyamotoNagai", "miyamotonagai"],
        mass: float = ...,
        rscale: float = ...,
        scaleHeight: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["MiyamotoNagai", "miyamotonagai"],
        mass: float = ...,
        rscale: float = ...,
        scaleRadius2: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["King", "king"],
        mass: float = ...,
        scaleRadius: float = ...,
        W0: float = ...,
        trunc: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["King", "king"],
        mass: float = ...,
        rscale: float = ...,
        W0: float = ...,
        trunc: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["PerfectEllipsoid", "perfectellipsoid"],
        mass: float = ...,
        scaleRadius: float = ...,
        axisRatioZ: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["PerfectEllipsoid", "perfectellipsoid"],
        mass: float = ...,
        scaleRadius: float = ...,
        q: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["PerfectEllipsoid", "perfectellipsoid"],
        mass: float = ...,
        rscale: float = ...,
        axisRatioZ: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["PerfectEllipsoid", "perfectellipsoid"],
        mass: float = ...,
        rscale: float = ...,
        q: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        scaleRadius: float = ...,
        scaleHeight: float = ...,
        innerCutoffRadius: float = ...,
        modulationAmplitude: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        scaleRadius: float = ...,
        scaleRadius2: float = ...,
        innerCutoffRadius: float = ...,
        modulationAmplitude: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        rscale: float = ...,
        scaleHeight: float = ...,
        innerCutoffRadius: float = ...,
        modulationAmplitude: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        rscale: float = ...,
        scaleRadius2: float = ...,
        innerCutoffRadius: float = ...,
        modulationAmplitude: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        scaleRadius: float = ...,
        scaleHeight: float = ...,
        innerCutoffRadius: float = ...,
        modulationAmplitude: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        scaleRadius: float = ...,
        scaleHeight: float = ...,
        innerCutoffRadius: float = ...,
        modulationAmplitude: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        scaleRadius: float = ...,
        scaleRadius2: float = ...,
        innerCutoffRadius: float = ...,
        modulationAmplitude: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        scaleRadius: float = ...,
        scaleRadius2: float = ...,
        innerCutoffRadius: float = ...,
        modulationAmplitude: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        rscale: float = ...,
        scaleHeight: float = ...,
        innerCutoffRadius: float = ...,
        modulationAmplitude: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        rscale: float = ...,
        scaleHeight: float = ...,
        innerCutoffRadius: float = ...,
        modulationAmplitude: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        rscale: float = ...,
        scaleRadius2: float = ...,
        innerCutoffRadius: float = ...,
        modulationAmplitude: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Disk", "disk"],
        rscale: float = ...,
        scaleRadius2: float = ...,
        innerCutoffRadius: float = ...,
        modulationAmplitude: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        densityNorm: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        rho0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        densityNorm: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        rho0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        densityNorm: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        rho0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        densityNorm: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        rho0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        densityNorm: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        rho0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        densityNorm: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        rho0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        densityNorm: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        rho0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        densityNorm: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        rho0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        densityNorm: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        rho0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        densityNorm: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        rho0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        densityNorm: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        rho0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        densityNorm: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        rho0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        densityNorm: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        rho0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        densityNorm: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        rho0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        densityNorm: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        rho0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        densityNorm: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Spheroid", "spheroid"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        rho0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        scaleRadius: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        cutoffStrength: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Nuker", "nuker"],
        rscale: float = ...,
        outerCutoffRadius: float = ...,
        p: float = ...,
        q: float = ...,
        alpha: float = ...,
        beta: float = ...,
        gamma: float = ...,
        xi: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        scaleRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        scaleRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        scaleRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        scaleRadius: float = ...,
        p: float = ...,
        q: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        rscale: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        rscale: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        rscale: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        rscale: float = ...,
        p: float = ...,
        q: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        mass: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        scaleRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        scaleRadius: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        scaleRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        scaleRadius: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        scaleRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        scaleRadius: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        scaleRadius: float = ...,
        p: float = ...,
        q: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        scaleRadius: float = ...,
        p: float = ...,
        q: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        rscale: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        rscale: float = ...,
        axisRatioY: float = ...,
        axisRatioZ: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        rscale: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        rscale: float = ...,
        axisRatioY: float = ...,
        q: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        rscale: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        rscale: float = ...,
        p: float = ...,
        axisRatioZ: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        rscale: float = ...,
        p: float = ...,
        q: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        surfaceDensity: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Sersic", "sersic"],
        rscale: float = ...,
        p: float = ...,
        q: float = ...,
        sersicIndex: float = ...,
        lmax: int = ...,
        mmax: int = ...,
        Sigma0: float = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["BasisSet", "basisset"],
        density: _ToDensity,
        gridSizeR: int = ...,
        gridSizeZ: int = ...,
        nmax: int = ...,
        lmax: int = ...,
        mmax: int = ...,
        smoothing: float = ...,
        rmin: float = ...,
        rmax: float = ...,
        zmin: float = ...,
        zmax: float = ...,
        eta: float = ...,
        r0: float = ...,
        fixOrder: bool = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["BasisSet", "basisset"],
        potential: _ToPotential,
        gridSizeR: int = ...,
        gridSizeZ: int = ...,
        nmax: int = ...,
        lmax: int = ...,
        mmax: int = ...,
        smoothing: float = ...,
        rmin: float = ...,
        rmax: float = ...,
        zmin: float = ...,
        zmax: float = ...,
        eta: float = ...,
        r0: float = ...,
        fixOrder: bool = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["BasisSet", "basisset"],
        file: str,
        gridSizeR: int = ...,
        gridSizeZ: int = ...,
        nmax: int = ...,
        lmax: int = ...,
        mmax: int = ...,
        smoothing: float = ...,
        rmin: float = ...,
        rmax: float = ...,
        zmin: float = ...,
        zmax: float = ...,
        eta: float = ...,
        r0: float = ...,
        fixOrder: bool = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["BasisSet", "basisset"],
        particles: tuple[onp.ToJustFloat64_2D, onp.ToJustFloat64_1D],
        gridSizeR: int = ...,
        gridSizeZ: int = ...,
        nmax: int = ...,
        lmax: int = ...,
        mmax: int = ...,
        smoothing: float = ...,
        rmin: float = ...,
        rmax: float = ...,
        zmin: float = ...,
        zmax: float = ...,
        eta: float = ...,
        r0: float = ...,
        fixOrder: bool = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Multipole", "multipole"],
        density: _ToDensity,
        gridSizeR: int = ...,
        gridSizeZ: int = ...,
        nmax: int = ...,
        lmax: int = ...,
        mmax: int = ...,
        smoothing: float = ...,
        rmin: float = ...,
        rmax: float = ...,
        zmin: float = ...,
        zmax: float = ...,
        eta: float = ...,
        r0: float = ...,
        fixOrder: bool = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Multipole", "multipole"],
        potential: _ToPotential,
        gridSizeR: int = ...,
        gridSizeZ: int = ...,
        nmax: int = ...,
        lmax: int = ...,
        mmax: int = ...,
        smoothing: float = ...,
        rmin: float = ...,
        rmax: float = ...,
        zmin: float = ...,
        zmax: float = ...,
        eta: float = ...,
        r0: float = ...,
        fixOrder: bool = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Multipole", "multipole"],
        file: str,
        gridSizeR: int = ...,
        gridSizeZ: int = ...,
        nmax: int = ...,
        lmax: int = ...,
        mmax: int = ...,
        smoothing: float = ...,
        rmin: float = ...,
        rmax: float = ...,
        zmin: float = ...,
        zmax: float = ...,
        eta: float = ...,
        r0: float = ...,
        fixOrder: bool = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Multipole", "multipole"],
        particles: tuple[onp.ToJustFloat64_2D, onp.ToJustFloat64_1D],
        gridSizeR: int = ...,
        gridSizeZ: int = ...,
        nmax: int = ...,
        lmax: int = ...,
        mmax: int = ...,
        smoothing: float = ...,
        rmin: float = ...,
        rmax: float = ...,
        zmin: float = ...,
        zmax: float = ...,
        eta: float = ...,
        r0: float = ...,
        fixOrder: bool = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["CylSpline", "cylspline"],
        density: _ToDensity,
        gridSizeR: int = ...,
        gridSizeZ: int = ...,
        nmax: int = ...,
        lmax: int = ...,
        mmax: int = ...,
        smoothing: float = ...,
        rmin: float = ...,
        rmax: float = ...,
        zmin: float = ...,
        zmax: float = ...,
        eta: float = ...,
        r0: float = ...,
        fixOrder: bool = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["CylSpline", "cylspline"],
        potential: _ToPotential,
        gridSizeR: int = ...,
        gridSizeZ: int = ...,
        nmax: int = ...,
        lmax: int = ...,
        mmax: int = ...,
        smoothing: float = ...,
        rmin: float = ...,
        rmax: float = ...,
        zmin: float = ...,
        zmax: float = ...,
        eta: float = ...,
        r0: float = ...,
        fixOrder: bool = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["CylSpline", "cylspline"],
        file: str,
        gridSizeR: int = ...,
        gridSizeZ: int = ...,
        nmax: int = ...,
        lmax: int = ...,
        mmax: int = ...,
        smoothing: float = ...,
        rmin: float = ...,
        rmax: float = ...,
        zmin: float = ...,
        zmax: float = ...,
        eta: float = ...,
        r0: float = ...,
        fixOrder: bool = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["CylSpline", "cylspline"],
        particles: tuple[onp.ToJustFloat64_2D, onp.ToJustFloat64_1D],
        gridSizeR: int = ...,
        gridSizeZ: int = ...,
        nmax: int = ...,
        lmax: int = ...,
        mmax: int = ...,
        smoothing: float = ...,
        rmin: float = ...,
        rmax: float = ...,
        zmin: float = ...,
        zmax: float = ...,
        eta: float = ...,
        r0: float = ...,
        fixOrder: bool = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["UniformAcceleration", "uniformacceleration"],
        file: str,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Evolving", "evolving"],
        file: str,
        interpLinear: bool = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        type: Literal["Evolving", "evolving"],
        file: str,
        linearInterp: bool = ...,
        center: Sequence[float] | str = ...,
        orientation: Sequence[float] = ...,
        rotation: float | Sequence[float] | str = ...,
        scale: Sequence[float] | str = ...,
        symmetry: _Symmetry = ...,
    ) -> None: ...
    # END GENERATED POTENTIAL INIT OVERLOADS
    # BEGIN GENERATED POTENTIAL EVAL OVERLOADS
    @overload
    def eval(
        self,
        point: tuple[onp.ToFloat, onp.ToFloat, onp.ToFloat] | onp.Array1D[np.inexact],
        /,
        *,
        pot: Literal[True],
        acc: Literal[False] = ...,
        der: Literal[False] = ...,
        t: onp.ToFloat = ...,
    ) -> float: ...
    @overload
    def eval(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        pot: Literal[True],
        acc: Literal[False] = ...,
        der: Literal[False] = ...,
        t: onp.ToFloat = ...,
    ) -> float: ...
    @overload
    def eval(
        self,
        points: onp.ToFloat2D,
        /,
        *,
        pot: Literal[True],
        acc: Literal[False] = ...,
        der: Literal[False] = ...,
        t: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def eval(
        self,
        point: tuple[onp.ToFloat, onp.ToFloat, onp.ToFloat] | onp.Array1D[np.inexact],
        /,
        *,
        pot: Literal[False] = ...,
        acc: Literal[True],
        der: Literal[False] = ...,
        t: onp.ToFloat = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def eval(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        pot: Literal[False] = ...,
        acc: Literal[True],
        der: Literal[False] = ...,
        t: onp.ToFloat = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def eval(
        self,
        points: onp.ToFloat2D,
        /,
        *,
        pot: Literal[False] = ...,
        acc: Literal[True],
        der: Literal[False] = ...,
        t: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array2D[np.float64]: ...
    @overload
    def eval(
        self,
        point: tuple[onp.ToFloat, onp.ToFloat, onp.ToFloat] | onp.Array1D[np.inexact],
        /,
        *,
        pot: Literal[False] = ...,
        acc: Literal[False] = ...,
        der: Literal[True],
        t: onp.ToFloat = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def eval(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        pot: Literal[False] = ...,
        acc: Literal[False] = ...,
        der: Literal[True],
        t: onp.ToFloat = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def eval(
        self,
        points: onp.ToFloat2D,
        /,
        *,
        pot: Literal[False] = ...,
        acc: Literal[False] = ...,
        der: Literal[True],
        t: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array2D[np.float64]: ...
    @overload
    def eval(
        self,
        point: tuple[onp.ToFloat, onp.ToFloat, onp.ToFloat] | onp.Array1D[np.inexact],
        /,
        *,
        pot: Literal[True],
        acc: Literal[True],
        der: Literal[False] = ...,
        t: onp.ToFloat = ...,
    ) -> tuple[float, onp.Array1D[np.float64]]: ...
    @overload
    def eval(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        pot: Literal[True],
        acc: Literal[True],
        der: Literal[False] = ...,
        t: onp.ToFloat = ...,
    ) -> tuple[float, onp.Array1D[np.float64]]: ...
    @overload
    def eval(
        self,
        points: onp.ToFloat2D,
        /,
        *,
        pot: Literal[True],
        acc: Literal[True],
        der: Literal[False] = ...,
        t: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]]: ...
    @overload
    def eval(
        self,
        point: tuple[onp.ToFloat, onp.ToFloat, onp.ToFloat] | onp.Array1D[np.inexact],
        /,
        *,
        pot: Literal[True],
        acc: Literal[False] = ...,
        der: Literal[True],
        t: onp.ToFloat = ...,
    ) -> tuple[float, onp.Array1D[np.float64]]: ...
    @overload
    def eval(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        pot: Literal[True],
        acc: Literal[False] = ...,
        der: Literal[True],
        t: onp.ToFloat = ...,
    ) -> tuple[float, onp.Array1D[np.float64]]: ...
    @overload
    def eval(
        self,
        points: onp.ToFloat2D,
        /,
        *,
        pot: Literal[True],
        acc: Literal[False] = ...,
        der: Literal[True],
        t: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]]: ...
    @overload
    def eval(
        self,
        point: tuple[onp.ToFloat, onp.ToFloat, onp.ToFloat] | onp.Array1D[np.inexact],
        /,
        *,
        pot: Literal[False] = ...,
        acc: Literal[True],
        der: Literal[True],
        t: onp.ToFloat = ...,
    ) -> tuple[onp.Array1D[np.float64], onp.Array1D[np.float64]]: ...
    @overload
    def eval(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        pot: Literal[False] = ...,
        acc: Literal[True],
        der: Literal[True],
        t: onp.ToFloat = ...,
    ) -> tuple[onp.Array1D[np.float64], onp.Array1D[np.float64]]: ...
    @overload
    def eval(
        self,
        points: onp.ToFloat2D,
        /,
        *,
        pot: Literal[False] = ...,
        acc: Literal[True],
        der: Literal[True],
        t: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]]: ...
    @overload
    def eval(
        self,
        point: tuple[onp.ToFloat, onp.ToFloat, onp.ToFloat] | onp.Array1D[np.inexact],
        /,
        *,
        pot: Literal[True],
        acc: Literal[True],
        der: Literal[True],
        t: onp.ToFloat = ...,
    ) -> tuple[float, onp.Array1D[np.float64], onp.Array1D[np.float64]]: ...
    @overload
    def eval(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        z: onp.ToFloat,
        /,
        *,
        pot: Literal[True],
        acc: Literal[True],
        der: Literal[True],
        t: onp.ToFloat = ...,
    ) -> tuple[float, onp.Array1D[np.float64], onp.Array1D[np.float64]]: ...
    @overload
    def eval(
        self,
        points: onp.ToFloat2D,
        /,
        *,
        pot: Literal[True],
        acc: Literal[True],
        der: Literal[True],
        t: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[
        onp.Array1D[np.float64], onp.Array2D[np.float64], onp.Array2D[np.float64]
    ]: ...
    # END GENERATED POTENTIAL EVAL OVERLOADS
    # BEGIN GENERATED POTENTIAL PROJECTED EVAL OVERLOADS
    @overload
    def projectedEval(
        self,
        point: tuple[onp.ToFloat, onp.ToFloat] | onp.Array1D[np.inexact],
        /,
        *,
        pot: Literal[True],
        acc: Literal[False] = ...,
        der: Literal[False] = ...,
        t: onp.ToFloat = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> float: ...
    @overload
    def projectedEval(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        /,
        *,
        pot: Literal[True],
        acc: Literal[False] = ...,
        der: Literal[False] = ...,
        t: onp.ToFloat = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> float: ...
    @overload
    def projectedEval(
        self,
        points: onp.ToFloat2D,
        /,
        *,
        pot: Literal[True],
        acc: Literal[False] = ...,
        der: Literal[False] = ...,
        t: onp.ToFloat | onp.ToFloat1D = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def projectedEval(
        self,
        point: tuple[onp.ToFloat, onp.ToFloat] | onp.Array1D[np.inexact],
        /,
        *,
        pot: Literal[False] = ...,
        acc: Literal[True],
        der: Literal[False] = ...,
        t: onp.ToFloat = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def projectedEval(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        /,
        *,
        pot: Literal[False] = ...,
        acc: Literal[True],
        der: Literal[False] = ...,
        t: onp.ToFloat = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def projectedEval(
        self,
        points: onp.ToFloat2D,
        /,
        *,
        pot: Literal[False] = ...,
        acc: Literal[True],
        der: Literal[False] = ...,
        t: onp.ToFloat | onp.ToFloat1D = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array2D[np.float64]: ...
    @overload
    def projectedEval(
        self,
        point: tuple[onp.ToFloat, onp.ToFloat] | onp.Array1D[np.inexact],
        /,
        *,
        pot: Literal[False] = ...,
        acc: Literal[False] = ...,
        der: Literal[True],
        t: onp.ToFloat = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def projectedEval(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        /,
        *,
        pot: Literal[False] = ...,
        acc: Literal[False] = ...,
        der: Literal[True],
        t: onp.ToFloat = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def projectedEval(
        self,
        points: onp.ToFloat2D,
        /,
        *,
        pot: Literal[False] = ...,
        acc: Literal[False] = ...,
        der: Literal[True],
        t: onp.ToFloat | onp.ToFloat1D = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> onp.Array2D[np.float64]: ...
    @overload
    def projectedEval(
        self,
        point: tuple[onp.ToFloat, onp.ToFloat] | onp.Array1D[np.inexact],
        /,
        *,
        pot: Literal[True],
        acc: Literal[True],
        der: Literal[False] = ...,
        t: onp.ToFloat = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[float, onp.Array1D[np.float64]]: ...
    @overload
    def projectedEval(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        /,
        *,
        pot: Literal[True],
        acc: Literal[True],
        der: Literal[False] = ...,
        t: onp.ToFloat = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[float, onp.Array1D[np.float64]]: ...
    @overload
    def projectedEval(
        self,
        points: onp.ToFloat2D,
        /,
        *,
        pot: Literal[True],
        acc: Literal[True],
        der: Literal[False] = ...,
        t: onp.ToFloat | onp.ToFloat1D = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]]: ...
    @overload
    def projectedEval(
        self,
        point: tuple[onp.ToFloat, onp.ToFloat] | onp.Array1D[np.inexact],
        /,
        *,
        pot: Literal[True],
        acc: Literal[False] = ...,
        der: Literal[True],
        t: onp.ToFloat = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[float, onp.Array1D[np.float64]]: ...
    @overload
    def projectedEval(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        /,
        *,
        pot: Literal[True],
        acc: Literal[False] = ...,
        der: Literal[True],
        t: onp.ToFloat = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[float, onp.Array1D[np.float64]]: ...
    @overload
    def projectedEval(
        self,
        points: onp.ToFloat2D,
        /,
        *,
        pot: Literal[True],
        acc: Literal[False] = ...,
        der: Literal[True],
        t: onp.ToFloat | onp.ToFloat1D = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array1D[np.float64], onp.Array2D[np.float64]]: ...
    @overload
    def projectedEval(
        self,
        point: tuple[onp.ToFloat, onp.ToFloat] | onp.Array1D[np.inexact],
        /,
        *,
        pot: Literal[False] = ...,
        acc: Literal[True],
        der: Literal[True],
        t: onp.ToFloat = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array1D[np.float64], onp.Array1D[np.float64]]: ...
    @overload
    def projectedEval(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        /,
        *,
        pot: Literal[False] = ...,
        acc: Literal[True],
        der: Literal[True],
        t: onp.ToFloat = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array1D[np.float64], onp.Array1D[np.float64]]: ...
    @overload
    def projectedEval(
        self,
        points: onp.ToFloat2D,
        /,
        *,
        pot: Literal[False] = ...,
        acc: Literal[True],
        der: Literal[True],
        t: onp.ToFloat | onp.ToFloat1D = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]]: ...
    @overload
    def projectedEval(
        self,
        point: tuple[onp.ToFloat, onp.ToFloat] | onp.Array1D[np.inexact],
        /,
        *,
        pot: Literal[True],
        acc: Literal[True],
        der: Literal[True],
        t: onp.ToFloat = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[float, onp.Array1D[np.float64], onp.Array1D[np.float64]]: ...
    @overload
    def projectedEval(
        self,
        x: onp.ToFloat,
        y: onp.ToFloat,
        /,
        *,
        pot: Literal[True],
        acc: Literal[True],
        der: Literal[True],
        t: onp.ToFloat = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[float, onp.Array1D[np.float64], onp.Array1D[np.float64]]: ...
    @overload
    def projectedEval(
        self,
        points: onp.ToFloat2D,
        /,
        *,
        pot: Literal[True],
        acc: Literal[True],
        der: Literal[True],
        t: onp.ToFloat | onp.ToFloat1D = ...,
        alpha: onp.ToFloat | onp.ToFloat1D = ...,
        beta: onp.ToFloat | onp.ToFloat1D = ...,
        gamma: onp.ToFloat | onp.ToFloat1D = ...,
    ) -> tuple[
        onp.Array1D[np.float64], onp.Array2D[np.float64], onp.Array2D[np.float64]
    ]: ...
    # END GENERATED POTENTIAL PROJECTED EVAL OVERLOADS
    @overload
    def potential(
        self,
        xyz: tuple[onp.ToFloat, onp.ToFloat, onp.ToFloat] | onp.Array1D[np.inexact],
        /,
        *,
        t: onp.ToFloat = ...,
    ) -> float: ...
    @overload
    def potential(
        self, x: onp.ToFloat, y: onp.ToFloat, z: onp.ToFloat, /, *, t: onp.ToFloat = ...
    ) -> float: ...
    @overload
    def potential(
        self, xyz: onp.ToFloat2D, /, *, t: onp.ToFloat | onp.ToFloat1D = ...
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def force(
        self,
        xyz: tuple[onp.ToFloat, onp.ToFloat, onp.ToFloat] | onp.Array1D[np.inexact],
        /,
        *,
        t: onp.ToFloat = ...,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def force(
        self, x: onp.ToFloat, y: onp.ToFloat, z: onp.ToFloat, /, *, t: onp.ToFloat = ...
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def force(
        self, xyz: onp.ToFloat2D, /, *, t: onp.ToFloat | onp.ToFloat1D = ...
    ) -> onp.Array2D[np.float64]: ...
    @overload
    def forceDeriv(
        self,
        xyz: tuple[onp.ToFloat, onp.ToFloat, onp.ToFloat] | onp.Array1D[np.inexact],
        /,
        *,
        t: onp.ToFloat = ...,
    ) -> tuple[onp.Array1D[np.float64], onp.Array1D[np.float64]]: ...
    @overload
    def forceDeriv(
        self, x: onp.ToFloat, y: onp.ToFloat, z: onp.ToFloat, /, *, t: onp.ToFloat = ...
    ) -> tuple[onp.Array1D[np.float64], onp.Array1D[np.float64]]: ...
    @overload
    def forceDeriv(
        self, xyz: onp.ToFloat2D, /, *, t: onp.ToFloat | onp.ToFloat1D = ...
    ) -> tuple[onp.Array2D[np.float64], onp.Array2D[np.float64]]: ...
    @overload
    def Rcirc(self, *, L: onp.ToFloat) -> float: ...
    @overload
    def Rcirc(self, *, L: onp.ToFloat1D) -> onp.Array1D[np.float64]: ...
    @overload
    def Rcirc(self, *, E: onp.ToFloat) -> float: ...
    @overload
    def Rcirc(self, *, E: onp.ToFloat1D) -> onp.Array1D[np.float64]: ...
    @overload
    def Tcirc(self, value: onp.ToFloat, /) -> float: ...
    @overload
    def Tcirc(
        self,
        value: tuple[
            onp.ToFloat, onp.ToFloat, onp.ToFloat, onp.ToFloat, onp.ToFloat, onp.ToFloat
        ],
        /,
    ) -> float: ...
    @overload
    def Tcirc(
        self, value: onp.Array1D[np.inexact], /
    ) -> float | onp.Array1D[np.float64]: ...
    @overload
    def Tcirc(self, value: onp.Array2D[np.inexact], /) -> onp.Array1D[np.float64]: ...
    @overload
    def Rmax(self, E: onp.ToFloat, /) -> float: ...
    @overload
    def Rmax(self, E: onp.ToFloat1D, /) -> onp.Array1D[np.float64]: ...
    @overload
    def Rperiapo(
        self, E: onp.ToFloat, L: onp.ToFloat, /
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def Rperiapo(
        self,
        value: tuple[onp.ToFloat, onp.ToFloat]
        | tuple[
            onp.ToFloat, onp.ToFloat, onp.ToFloat, onp.ToFloat, onp.ToFloat, onp.ToFloat
        ]
        | onp.Array1D[np.inexact],
        /,
    ) -> onp.Array1D[np.float64]: ...
    @overload
    def Rperiapo(self, value: onp.ToFloat2D, /) -> onp.Array2D[np.float64]: ...
