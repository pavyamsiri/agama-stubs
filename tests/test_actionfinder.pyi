import agama
from typing import assert_type
from optype import numpy as onp
import numpy as np

type _Array2D_f64 = onp.Array2D[np.float64]
af: agama.ActionFinder
_arr_f64_2d: onp.Array2D[np.float64]

# actions
assert_type(af(_arr_f64_2d, True, False, False), _Array2D_f64)
assert_type(af(_arr_f64_2d, True, False), _Array2D_f64)
assert_type(af(_arr_f64_2d, True), _Array2D_f64)
assert_type(af(_arr_f64_2d, actions=True), _Array2D_f64)
assert_type(af(_arr_f64_2d, actions=True, angles=False), _Array2D_f64)
assert_type(
    af(_arr_f64_2d, actions=True, angles=False, frequencies=False), _Array2D_f64
)
assert_type(af(_arr_f64_2d, actions=True, frequencies=False), _Array2D_f64)
assert_type(af(_arr_f64_2d, True, angles=False), _Array2D_f64)
assert_type(af(_arr_f64_2d, True, angles=False, frequencies=False), _Array2D_f64)
assert_type(af(_arr_f64_2d, True, frequencies=False), _Array2D_f64)

# angles + frequencies
assert_type(af(_arr_f64_2d, False, True, True), tuple[_Array2D_f64, _Array2D_f64])
assert_type(af(_arr_f64_2d, False, True), tuple[_Array2D_f64, _Array2D_f64])
assert_type(
    af(_arr_f64_2d, actions=False, angles=True), tuple[_Array2D_f64, _Array2D_f64]
)
assert_type(
    af(_arr_f64_2d, actions=False, angles=True, frequencies=True),
    tuple[_Array2D_f64, _Array2D_f64],
)

# frequencies
assert_type(af(_arr_f64_2d, False, False, True), _Array2D_f64)
assert_type(
    af(_arr_f64_2d, actions=False, angles=False, frequencies=True), _Array2D_f64
)
assert_type(af(_arr_f64_2d, actions=False, frequencies=True), _Array2D_f64)
assert_type(af(_arr_f64_2d, False, frequencies=True), _Array2D_f64)

# actions + angles (default frequencies)
assert_type(
    af(_arr_f64_2d, True, True, True), tuple[_Array2D_f64, _Array2D_f64, _Array2D_f64]
)
assert_type(
    af(_arr_f64_2d, True, True), tuple[_Array2D_f64, _Array2D_f64, _Array2D_f64]
)
assert_type(
    af(_arr_f64_2d, actions=True, angles=True),
    tuple[_Array2D_f64, _Array2D_f64, _Array2D_f64],
)
assert_type(
    af(_arr_f64_2d, actions=True, angles=True, frequencies=True),
    tuple[_Array2D_f64, _Array2D_f64, _Array2D_f64],
)

# actions + frequencies
assert_type(af(_arr_f64_2d, True, False, True), tuple[_Array2D_f64, _Array2D_f64])
assert_type(
    af(_arr_f64_2d, actions=True, angles=False, frequencies=True),
    tuple[_Array2D_f64, _Array2D_f64],
)
assert_type(
    af(_arr_f64_2d, actions=True, frequencies=True), tuple[_Array2D_f64, _Array2D_f64]
)
assert_type(af(_arr_f64_2d, True, frequencies=True), tuple[_Array2D_f64, _Array2D_f64])

# angles
assert_type(af(_arr_f64_2d, False, True, False), _Array2D_f64)
assert_type(
    af(_arr_f64_2d, actions=False, angles=True, frequencies=False), _Array2D_f64
)

# actions + angles, frequencies = False
assert_type(af(_arr_f64_2d, True, True, False), tuple[_Array2D_f64, _Array2D_f64])
assert_type(
    af(_arr_f64_2d, actions=True, angles=True, frequencies=False),
    tuple[_Array2D_f64, _Array2D_f64],
)

# none
assert_type(af(_arr_f64_2d), _Array2D_f64)  # actions defaults to True
assert_type(af(_arr_f64_2d, False), None)
assert_type(af(_arr_f64_2d, False, False), None)
assert_type(af(_arr_f64_2d, False, False, False), None)
assert_type(af(_arr_f64_2d, actions=False), None)
assert_type(af(_arr_f64_2d, actions=False, angles=False), None)
assert_type(af(_arr_f64_2d, actions=False, angles=False, frequencies=False), None)
assert_type(af(_arr_f64_2d, actions=False, frequencies=False), None)
assert_type(af(_arr_f64_2d, False, frequencies=False), None)
assert_type(af(_arr_f64_2d, False, angles=False), None)
assert_type(af(_arr_f64_2d, False, angles=False, frequencies=False), None)
