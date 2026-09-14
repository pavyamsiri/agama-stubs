from typing import Any

from ._potential import Potential

__all__: list[str] = ["GalaPotential"]

class GalaPotential(Potential):
    __name__: str
    # Gala and its unit/quantity types are deliberately not dependencies.
    units: Any
    # Gala's runtime base overrides the inherited AGAMA density method.
    density: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    agamadensity = Potential.density
