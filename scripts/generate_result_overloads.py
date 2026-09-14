"""Generate overloads for APIs with flag- and rank-dispatched results."""

from __future__ import annotations

import argparse
import itertools
from pathlib import Path

from scripts.result_dispatch_spec import (
    ACTION_RESULTS,
    MOMENT_RESULTS,
    POTENTIAL_EVAL_RESULTS,
    POTENTIAL_PROJECTED_EVAL_RESULTS,
    Result,
)

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "agama-stubs" / "_potential.pyi"
ACTION_TARGET = ROOT / "agama-stubs" / "_actions.pyi"
GALAXY_TARGET = ROOT / "agama-stubs" / "_galaxy.pyi"
FUNCTIONS_TARGET = ROOT / "agama-stubs" / "_functions.pyi"


class _Arguments(argparse.Namespace):
    check: bool = False


def _return_type(results: tuple[Result, ...], *, batch: bool) -> str:
    annotations = tuple(result.batch if batch else result.scalar for result in results)
    if len(annotations) == 1:
        return annotations[0]
    return "tuple[" + ", ".join(annotations) + "]"


def _render(
    enabled: tuple[Result, ...],
    *,
    method: str,
    results: tuple[Result, ...],
    input_lines: tuple[str, ...],
    batch: bool,
    extras: tuple[str, ...] = (),
) -> str:
    enabled_flags = {result.flag for result in enabled}
    lines = [
        "    @overload",
        f"    def {method}(",
        "        self,",
        *input_lines,
        "        *,",
    ]
    for result in results:
        if result.flag in enabled_flags:
            lines.append(f"        {result.flag}: Literal[True],")
        else:
            lines.append(f"        {result.flag}: Literal[False] = ...,")
    time = "onp.ToFloat | onp.ToFloat1D" if batch else "onp.ToFloat"
    return_type = _return_type(enabled, batch=batch)
    lines.append(f"        t: {time} = ...,")
    lines.extend(extras)
    if len(return_type) > 78:
        inner = return_type.removeprefix("tuple[").removesuffix("]")
        lines.extend(("    ) -> tuple[", f"        {inner}", "    ]: ..."))
    else:
        lines.append(f"    ) -> {return_type}: ...")
    return "\n".join(lines)


def generate(
    method: str,
    results: tuple[Result, ...],
    scalar_inputs: tuple[tuple[str, ...], ...],
    batch_input: tuple[str, ...],
    *,
    extras: tuple[str, ...] = (),
) -> str:
    blocks: list[str] = []
    for count in range(1, len(results) + 1):
        for enabled in itertools.combinations(results, count):
            for scalar_input in scalar_inputs:
                blocks.append(
                    _render(
                        enabled,
                        method=method,
                        results=results,
                        input_lines=scalar_input,
                        batch=False,
                        extras=extras,
                    )
                )
            blocks.append(
                _render(
                    enabled,
                    method=method,
                    results=results,
                    input_lines=batch_input,
                    batch=True,
                    extras=extras,
                )
            )
    return "\n".join(blocks) + "\n"


def generate_actions() -> str:
    blocks: list[str] = []
    for point, result_type in (
        ("onp.Array1D[np.inexact]", "onp.Array1D[np.float64]"),
        ("onp.Array2D[np.inexact]", "onp.Array2D[np.float64]"),
    ):
        for values in itertools.product((False, True), repeat=3):
            selected = tuple(
                result
                for result, value in zip(ACTION_RESULTS, values, strict=True)
                if value
            )
            result = "None" if not selected else result_type
            if len(selected) > 1:
                result = "tuple[" + ", ".join(result_type for _ in selected) + "]"
            lines = [
                "    @overload",
                "    def __call__(",
                "        self,",
                f"        point: {point},",
            ]
            defaults = (True, False, values[1])
            optional_from = len(values)
            while (
                optional_from
                and values[optional_from - 1] == defaults[optional_from - 1]
            ):
                optional_from -= 1
            for index, (descriptor, value) in enumerate(
                zip(ACTION_RESULTS, values, strict=True)
            ):
                suffix = " = ..." if index >= optional_from else ""
                lines.append(f"        {descriptor.flag}: Literal[{value}]{suffix},")
            if len(result) > 78:
                inner = result.removeprefix("tuple[").removesuffix("]")
                lines.extend(("    ) -> tuple[", f"        {inner}", "    ]: ..."))
            else:
                lines.append(f"    ) -> {result}: ...")
            blocks.append("\n".join(lines))
        for actions in (False, True):
            result = (
                result_type if not actions else f"tuple[{result_type}, {result_type}]"
            )
            default = " = ..." if actions else ""
            blocks.append(
                "\n".join(
                    (
                        "    @overload",
                        "    def __call__(",
                        "        self,",
                        f"        point: {point},",
                        f"        actions: Literal[{actions}]{default},",
                        "        *,",
                        "        frequencies: Literal[True],",
                        "        angles: Literal[False] = ... ,".replace(
                            " ... ,", " ...,"
                        ),
                        f"    ) -> {result}: ...",
                    )
                )
            )
    return "\n".join(blocks) + "\n"


def generate_action_mapper() -> str:
    blocks: list[str] = []
    for point, coords, freqs in (
        (
            "onp.Array1D[np.inexact]",
            "onp.Array1D[np.float64]",
            "onp.Array1D[np.float64]",
        ),
        (
            "onp.Array2D[np.inexact]",
            "onp.Array2D[np.float64]",
            "onp.Array2D[np.float64]",
        ),
    ):
        blocks.extend(
            (
                f"    @overload\n    def __call__(\n        self, point: {point}, frequencies: Literal[False] = ...\n    ) -> {coords}: ...",
                f"    @overload\n    def __call__(\n        self, point: {point}, frequencies: Literal[True]\n    ) -> tuple[{coords}, {freqs}]: ...",
            )
        )
    return "\n".join(blocks) + "\n"


def generate_df_call() -> str:
    blocks: list[str] = []
    inputs = (
        (
            (
                "        jr: onp.ToFloat,",
                "        jz: onp.ToFloat,",
                "        jphi: onp.ToFloat,",
            ),
            "float",
            "onp.Array1D[np.float64]",
        ),
        (
            ("        act: onp.Array1D[np.inexact],",),
            "float",
            "onp.Array1D[np.float64]",
        ),
        (
            ("        act: onp.Array2D[np.inexact],",),
            "onp.Array1D[np.float64]",
            "onp.Array2D[np.float64]",
        ),
    )
    for arguments, value, derivative in inputs:
        for der in (False, True):
            suffix = " = ..." if not der else ""
            result = f"tuple[{value}, {derivative}]" if der else value
            lines = [
                "    @overload",
                "    def __call__(",
                "        self,",
                *arguments,
                "        *,",
                f"        der: Literal[{der}]{suffix},",
                f"    ) -> {result}: ...",
            ]
            blocks.append("\n".join(lines))
    return "\n".join(blocks) + "\n"


def _format_return(lines: list[str], result: str) -> None:
    if len(result) > 78:
        inner = result.removeprefix("tuple[").removesuffix("]")
        parts = inner.split(", ")
        if len(parts) >= 4:
            lines.append("    ) -> tuple[")
            lines.extend(f"        {part}," for part in parts)
            lines.append("    ]: ...")
        else:
            lines.extend(("    ) -> tuple[", f"        {inner}", "    ]: ..."))
    else:
        lines.append(f"    ) -> {result}: ...")


def generate_moments() -> str:
    blocks: list[str] = []
    inputs = (
        (
            (
                "        x: onp.ToFloat,",
                "        y: onp.ToFloat,",
                "        z: onp.ToFloat,",
                "        /,",
            ),
            False,
        ),
        (
            ("        point: onp.Array1D[np.inexact] | Sequence[float],", "        /,"),
            False,
        ),
        (("        points: onp.Array2D[np.inexact],", "        /,"), True),
    )
    defaults = (True, False, True)
    for arguments, batch in inputs:
        for separate in (False, True):
            for count in range(1, len(MOMENT_RESULTS) + 1):
                for selected in itertools.combinations(MOMENT_RESULTS, count):
                    selected_flags = {item.flag for item in selected}
                    values = tuple(
                        item.flag in selected_flags for item in MOMENT_RESULTS
                    )
                    if separate:
                        types = tuple(item.batch for item in selected)
                        if batch:
                            types = tuple(
                                "onp.Array2D[np.float64]"
                                if item.flag == "dens"
                                else "onp.Array3D[np.float64]"
                                for item in selected
                            )
                    else:
                        types = tuple(
                            item.batch if batch else item.scalar for item in selected
                        )
                    result = (
                        types[0]
                        if len(types) == 1
                        else "tuple[" + ", ".join(types) + "]"
                    )
                    lines = [
                        "    @overload",
                        "    def moments(",
                        "        self,",
                        *arguments,
                        "        *,",
                    ]
                    for item, value, default in zip(
                        MOMENT_RESULTS, values, defaults, strict=True
                    ):
                        suffix = " = ..." if value == default else ""
                        lines.append(f"        {item.flag}: Literal[{value}]{suffix},")
                    suffix = " = ..." if not separate else ""
                    lines.append(f"        separate: Literal[{separate}]{suffix},")
                    lines.extend(
                        f"        {angle}: onp.ToFloat | onp.ToFloat1D = ...,"
                        for angle in ("alpha", "beta", "gamma")
                    )
                    _format_return(lines, result)
                    blocks.append("\n".join(lines))
    return "\n".join(blocks) + "\n"


def generate_total_mass() -> str:
    return """    @overload
    def totalMass(self, separate: Literal[False] = ...) -> float: ...
    @overload
    def totalMass(self, separate: Literal[True]) -> onp.Array1D[np.float64]: ...
    @overload
    def totalMass(self, separate: onp.ToBool) -> float | onp.Array1D[np.float64]: ...
"""


def generate_vdf() -> str:
    blocks: list[str] = []
    inputs = (
        (
            (
                "        x: onp.ToFloat,",
                "        y: onp.ToFloat,",
                "        z: onp.ToFloat,",
                "        /,",
            ),
            False,
        ),
        (("        x: onp.ToFloat,", "        y: onp.ToFloat,", "        /,"), False),
        (
            ("        point: onp.Array1D[np.float64] | Sequence[float],", "        /,"),
            False,
        ),
        (("        points: onp.Array2D[np.float64],", "        /,"), True),
    )
    for arguments, batch in inputs:
        for separate, dens in itertools.product((False, True), repeat=2):
            if not batch and not separate:
                value = "Spline"
                density = "float"
            else:
                rank = 2 if batch and separate else 1
                value = f"onp.Array{rank}D[np.object_]"
                density = f"onp.Array{rank}D[np.float64]"
            returns = [value, value, value]
            if dens:
                returns.append(density)
            result = "tuple[" + ", ".join(returns) + "]"
            lines = [
                "    @overload",
                "    def vdf(",
                "        self,",
                *arguments,
                "        *,",
            ]
            lines.extend(
                (
                    "        gridv: int | onp.ToFloat1D = ... ,".replace(
                        " ... ,", " ...,"
                    ),
                    f"        dens: Literal[{dens}]" + ("" if dens else " = ...") + ",",
                    f"        separate: Literal[{separate}]"
                    + ("" if separate else " = ...")
                    + ",",
                    "        alpha: onp.ToFloat | onp.ToFloat1D = ... ,".replace(
                        " ... ,", " ...,"
                    ),
                    "        beta: onp.ToFloat | onp.ToFloat1D = ... ,".replace(
                        " ... ,", " ...,"
                    ),
                    "        gamma: onp.ToFloat | onp.ToFloat1D = ... ,".replace(
                        " ... ,", " ...,"
                    ),
                )
            )
            _format_return(lines, result)
            blocks.append("\n".join(lines))
    return "\n".join(blocks) + "\n"


def generate_projected_df() -> str:
    blocks: list[str] = []
    inputs = (
        (("        points: onp.Array2D[np.float64],", "        /,"), True),
        (
            (
                "        X: onp.ToFloat,",
                "        Y: onp.ToFloat,",
                "        vX: onp.ToFloat,",
                "        vY: onp.ToFloat,",
                "        vZ: onp.ToFloat,",
                "        evX: onp.ToFloat,",
                "        evY: onp.ToFloat,",
                "        evZ: onp.ToFloat,",
                "        /,",
            ),
            False,
        ),
        (
            ("        point: onp.Array1D[np.float64] | Sequence[float],", "        /,"),
            False,
        ),
    )
    for arguments, batch in inputs:
        for separate in (False, True):
            rank = int(batch) + int(separate)
            result = "float" if rank == 0 else f"onp.Array{rank}D[np.float64]"
            lines = [
                "    @overload",
                "    def projectedDF(",
                "        self,",
                *arguments,
                "        *,",
            ]
            suffix = "" if separate else " = ..."
            lines.append(f"        separate: Literal[{separate}]{suffix},")
            lines.extend(
                f"        {angle}: onp.ToFloat | onp.ToFloat1D = ...,"
                for angle in ("alpha", "beta", "gamma")
            )
            lines.append(f"    ) -> {result}: ...")
            blocks.append("\n".join(lines))
    return "\n".join(blocks) + "\n"


def generate_orbit() -> str:
    blocks: list[str] = []
    for batch in (False, True):
        ic = (
            "onp.Array2D[np.inexact]"
            if batch
            else "onp.Array1D[np.inexact] | Sequence[float]"
        )
        time = "onp.ToFloat | onp.ToFloat1D" if batch else "onp.ToFloat"
        target_result = "_OrbitTargetBatch" if batch else "_OrbitTargetScalar"
        lyapunov_result = "_OrbitLyapunovBatch" if batch else "_OrbitLyapunovScalar"
        for object_dtype, der, lyapunov, target_mode in itertools.product(
            (False, True), (False, True), (False, True), ("none", "one", "many")
        ):
            trajectory = "_OrbitObjectBatch" if batch else "_OrbitObjectScalar"
            if batch and object_dtype:
                trajectory = "_OrbitObjectVector"
            if not batch and object_dtype:
                trajectory = "Orbit"
            derivative = "_OrbitObjectBatch" if batch else "_OrbitObjectScalar"
            outputs: list[str] = []
            if target_mode == "one":
                outputs.append(target_result)
            outputs.append(trajectory)
            if der:
                outputs.append(derivative)
            if lyapunov:
                outputs.append(lyapunov_result)
            if target_mode == "many":
                element = "_OrbitResultBatch" if batch else "_OrbitResultScalar"
                result = f"tuple[{element}, ...]"
            elif len(outputs) == 1:
                result = outputs[0]
            else:
                result = "tuple[" + ", ".join(outputs) + "]"
            lines = [
                "@overload",
                "def orbit(",
                "    *,",
                "    potential: _ToPotential,",
                f"    ic: {ic},",
                f"    time: {time},",
            ]
            if target_mode == "one":
                lines.append("    targets: Target,")
            elif target_mode == "many":
                lines.append("    targets: Sequence[Target],")
            if object_dtype:
                lines.append("    dtype: type[object],")
                trajsize = "onp.ToInt | onp.ToInt1D" if batch else "onp.ToInt"
                lines.append(f"    trajsize: {trajsize} = ...,")
            else:
                trajsize = "onp.ToInt | onp.ToInt1D" if batch else "onp.ToInt"
                lines.append(f"    trajsize: {trajsize},")
                lines.append("    dtype: str | type[np.generic] = ...,")
            lines.extend(
                (
                    f"    der: Literal[{der}]" + ("" if der else " = ...") + ",",
                    f"    lyapunov: Literal[{lyapunov}]"
                    + ("" if lyapunov else " = ...")
                    + ",",
                    "    Omega: onp.ToFloat = ... ,".replace(" ... ,", " ...,"),
                    f"    timestart: {time} = ... ,".replace(" ... ,", " ...,"),
                    "    accuracy: onp.ToFloat = ... ,".replace(" ... ,", " ...,"),
                    "    maxNumSteps: onp.ToInt = ... ,".replace(" ... ,", " ...,"),
                    '    method: Literal["dop853", "dprkn8", "hermite"] = ... ,'.replace(
                        " ... ,", " ...,"
                    ),
                    "    verbose: onp.ToBool = ... ,".replace(" ... ,", " ...,"),
                )
            )
            if len(result) > 82:
                inner = result.removeprefix("tuple[").removesuffix("]")
                lines.extend((") -> tuple[", f"    {inner}", "]: ..."))
            else:
                lines.append(f") -> {result}: ...")
            blocks.append("\n".join(lines))
    return "\n".join(blocks) + "\n"


def update_region(source: str, name: str, generated: str) -> str:
    start = f"    # BEGIN GENERATED {name} OVERLOADS\n"
    end = f"    # END GENERATED {name} OVERLOADS\n"
    if start not in source:
        start = start.removeprefix("    ")
        end = end.removeprefix("    ")
    before, separator, remainder = source.partition(start)
    if not separator:
        raise RuntimeError(f"missing start marker in {TARGET}")
    _, separator, after = remainder.partition(end)
    if not separator:
        raise RuntimeError(f"missing end marker in {TARGET}")
    return before + start + generated + end + after


def main() -> int:
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("--check", action="store_true")
    args = parser.parse_args(namespace=_Arguments())
    source = TARGET.read_text()
    eval_scalar = (
        (
            "        point: tuple[onp.ToFloat, onp.ToFloat, onp.ToFloat] | onp.Array1D[np.inexact],",
            "        /,",
        ),
        (
            "        x: onp.ToFloat,",
            "        y: onp.ToFloat,",
            "        z: onp.ToFloat,",
            "        /,",
        ),
    )
    projected_scalar = (
        (
            "        point: tuple[onp.ToFloat, onp.ToFloat] | onp.Array1D[np.inexact],",
            "        /,",
        ),
        ("        x: onp.ToFloat,", "        y: onp.ToFloat,", "        /,"),
    )
    updated = update_region(
        source,
        "POTENTIAL EVAL",
        generate(
            "eval",
            POTENTIAL_EVAL_RESULTS,
            eval_scalar,
            ("        points: onp.ToFloat2D,", "        /,"),
        ),
    )
    projected_extras = (
        "        alpha: onp.ToFloat | onp.ToFloat1D = ...,",
        "        beta: onp.ToFloat | onp.ToFloat1D = ...,",
        "        gamma: onp.ToFloat | onp.ToFloat1D = ...,",
    )
    updated = update_region(
        updated,
        "POTENTIAL PROJECTED EVAL",
        generate(
            "projectedEval",
            POTENTIAL_PROJECTED_EVAL_RESULTS,
            projected_scalar,
            ("        points: onp.ToFloat2D,", "        /,"),
            extras=projected_extras,
        ),
    )
    updates = {TARGET: (source, updated)}
    for path, regions in (
        (
            ACTION_TARGET,
            (
                ("ACTION FINDER CALL", generate_actions()),
                ("ACTION MAPPER CALL", generate_action_mapper()),
            ),
        ),
        (FUNCTIONS_TARGET, (("ORBIT", generate_orbit() + "\n"),)),
        (
            GALAXY_TARGET,
            (
                ("DISTRIBUTION FUNCTION CALL", generate_df_call()),
                ("GALAXY MODEL TOTAL MASS", generate_total_mass()),
                ("GALAXY MODEL MOMENTS", generate_moments()),
                ("GALAXY MODEL VDF", generate_vdf()),
                ("GALAXY MODEL PROJECTED DF", generate_projected_df()),
            ),
        ),
    ):
        original = path.read_text()
        changed = original
        for name, generated in regions:
            changed = update_region(changed, name, generated)
        updates[path] = (original, changed)
    stale = [
        path for path, (original, changed) in updates.items() if original != changed
    ]
    if args.check and stale:
        parser.error(
            "stale generated result overloads: "
            + ", ".join(str(path.relative_to(ROOT)) for path in stale)
        )
    if not args.check:
        for path, (_, changed) in updates.items():
            _ = path.write_text(changed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
