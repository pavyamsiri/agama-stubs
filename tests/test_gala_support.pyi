from typing import Any, assert_type

import agama
import numpy as np
from agama._pygama import GalaPotential as PygamaPotential
from optype import numpy as onp

positions: onp.Array2D[np.float64]
source: agama.Potential

assert_type(agama.GalaPotential(type="Plummer", mass=1.0), agama.GalaPotential)
assert_type(agama.GalaPotential(source), agama.GalaPotential)
assert_type(agama.GalaPotential("potential.ini"), agama.GalaPotential)
assert_type(PygamaPotential(type="Plummer", units=None), agama.GalaPotential)

wrapped: agama.GalaPotential

def accepts_agama(potential: agama.Potential) -> None: ...

accepts_agama(wrapped)
assert_type(wrapped.__name__, str)
assert_type(wrapped.potential((1.0, 0.0, 0.0)), float)
assert_type(wrapped.potential(positions), onp.Array1D[np.float64])
assert_type(wrapped.force(positions), onp.Array2D[np.float64])
assert_type(wrapped.agamadensity((1.0, 0.0, 0.0)), float)
assert_type(wrapped.agamadensity(1.0, 0.0, 0.0, t=0.0), float)
assert_type(wrapped.agamadensity(positions), onp.Array1D[np.float64])
# Gala density returns a quantity, not the inherited AGAMA result type.
assert_type(wrapped.density(positions), Any)
