"""Declarative schemas for APIs whose flags and input rank control results."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Result:
    flag: str
    scalar: str
    batch: str


POTENTIAL_EVAL_RESULTS = (
    Result("pot", "float", "onp.Array1D[np.float64]"),
    Result("acc", "onp.Array1D[np.float64]", "onp.Array2D[np.float64]"),
    Result("der", "onp.Array1D[np.float64]", "onp.Array2D[np.float64]"),
)

POTENTIAL_PROJECTED_EVAL_RESULTS = (
    Result("pot", "float", "onp.Array1D[np.float64]"),
    Result("acc", "onp.Array1D[np.float64]", "onp.Array2D[np.float64]"),
    Result("der", "onp.Array1D[np.float64]", "onp.Array2D[np.float64]"),
)

ACTION_RESULTS = (
    Result("actions", "onp.Array1D[np.float64]", "onp.Array2D[np.float64]"),
    Result("angles", "onp.Array1D[np.float64]", "onp.Array2D[np.float64]"),
    Result("frequencies", "onp.Array1D[np.float64]", "onp.Array2D[np.float64]"),
)

MOMENT_RESULTS = (
    Result("dens", "float", "onp.Array1D[np.float64]"),
    Result("vel", "onp.Array1D[np.float64]", "onp.Array2D[np.float64]"),
    Result("vel2", "onp.Array1D[np.float64]", "onp.Array2D[np.float64]"),
)
