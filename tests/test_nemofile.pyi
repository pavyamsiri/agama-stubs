from array import array
from pathlib import Path
from typing import assert_type

import agama
import numpy as np
from agama._nemofile import _Snapshot
from optype import numpy as onp

positions: onp.Array2D[np.float32]
dtype: np.dtype[np.float32]
with agama.NemoFile(Path("snapshot.nemo"), "w") as output:
    assert_type(output, agama.NemoFile)
    output.write({"Position": positions})
    output.write({"Time": 1.0, "Position": [[1.0, 2.0, 3.0]]})

with agama.NemoFile("snapshot.nemo") as source:
    assert_type(iter(source), agama.NemoFile)
    assert_type(next(source), _Snapshot)
    assert_type(source.next(), _Snapshot)
    assert_type(source.read(), _Snapshot | None)
    for snapshot in source:
        assert_type(snapshot, _Snapshot)
    assert_type(source.read_array("i"), array[int])
    assert_type(source.read_array("d"), array[float])
    assert_type(source.read_fixed_array(dtype, 3), onp.Array1D[np.float32])
    assert_type(source.read_magic_number(), int | None)
    assert_type(source.read_string(), str)
    source.write_array("i", [1, 2, 3])
    source.write_fixed_array(positions, np.float32)
