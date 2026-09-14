from typing import assert_type

import agama
import numpy as np
from agama._pygama import GalpyPotential as PygamaPotential
from galpy.potential.PlummerPotential import PlummerPotential
from galpy.potential.Potential import Potential as GalpyBase
from optype import numpy as onp

type _GalpyResult = float | onp.ArrayND

native: GalpyBase
components: list[GalpyBase]
plummers: list[PlummerPotential]
positions: onp.Array2D[np.float64]
agama_potential: agama.Potential

assert_type(agama.GalpyPotential(native), agama.GalpyPotential)
assert_type(agama.GalpyPotential(native, symmetry="spherical"), agama.GalpyPotential)
assert_type(agama.GalpyPotential(components), agama.GalpyPotential)
assert_type(agama.GalpyPotential(plummers), agama.GalpyPotential)
assert_type(agama.GalpyPotential(components, symmetry=None), agama.GalpyPotential)
assert_type(PygamaPotential(native), agama.GalpyPotential)
assert_type(agama.GalpyPotential("potential.ini"), agama.GalpyPotential)
assert_type(agama.GalpyPotential(agama_potential), agama.GalpyPotential)
assert_type(
    agama.GalpyPotential(agama_potential, agama_potential), agama.GalpyPotential
)
assert_type(
    agama.GalpyPotential(type="Plummer", mass=1.0, scaleRadius=2.0),
    agama.GalpyPotential,
)
assert_type(agama.GalpyPotential(type="NFW", normalize=True), agama.GalpyPotential)
assert_type(agama.GalpyPotential(type="Plummer", normalize=0.5), agama.GalpyPotential)
assert_type(
    agama.GalpyPotential(agama_potential, normalize=False), agama.GalpyPotential
)
assert_type(
    agama.GalpyPotential(file="potential.ini", normalize=1.0), agama.GalpyPotential
)
assert_type(
    agama.GalpyPotential(type="Multipole", potential=agama_potential, lmax=4),
    agama.GalpyPotential,
)

wrapped: agama.GalpyPotential

def accepts_agama(potential: agama.Potential) -> None: ...
def accepts_galpy(potential: GalpyBase) -> None: ...

accepts_agama(wrapped)
accepts_galpy(wrapped)
assert_type(wrapped.__name__, str)
assert_type(wrapped.potential((1.0, 0.0, 0.0)), float)
assert_type(wrapped.potential(positions), onp.Array1D[np.float64])
assert_type(wrapped.force(positions), onp.Array2D[np.float64])
assert_type(wrapped.density(positions), onp.Array1D[np.float64])
assert_type(wrapped(1.0, 0.0), _GalpyResult)
assert_type(wrapped.Rforce(1.0, 0.0), _GalpyResult)
assert_type(wrapped.zforce(1.0, 0.1, phi=0.2, t=0.0), _GalpyResult)
assert_type(wrapped.dens(1.0, 0.0), _GalpyResult)
assert_type(wrapped.vcirc(1.0), _GalpyResult)
assert_type(wrapped.normalize(0.5), None)
assert_type(wrapped + native, object)
