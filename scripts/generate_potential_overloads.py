#!/usr/bin/env python3
"""Generate the overloads for ``Potential.__init__`` from ``potential_spec``."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

from scripts.potential_spec import MODIFIERS, PARAMETERS, POTENTIALS, PotentialKind

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "agama-stubs" / "_potential.pyi"
START = "    # BEGIN GENERATED POTENTIAL INIT OVERLOADS\n"
END = "    # END GENERATED POTENTIAL INIT OVERLOADS\n"

SOURCE_PARAMETERS = {
    "density": "_ToDensity",
    "potential": "_ToPotential",
    "file": "str",
    "particles": "tuple[onp.ToJustFloat64_2D, onp.ToJustFloat64_1D]",
}


class _Arguments(argparse.Namespace):
    check: bool = False


def _parameter_branches(kind: PotentialKind) -> list[tuple[str, ...]]:
    branches = [kind.parameters]
    for group in kind.exclusive:
        next_branches: list[tuple[str, ...]] = []
        for branch in branches:
            without_group = tuple(item for item in branch if item not in group)
            next_branches.extend(without_group + (choice,) for choice in group)
        branches = next_branches
    return branches


def _spellings(parameters: tuple[str, ...]) -> list[tuple[tuple[str, str], ...]]:
    choices = [
        tuple((name, PARAMETERS[key].annotation) for name in PARAMETERS[key].names)
        for key in parameters
    ]
    return list(itertools.product(*choices)) if choices else [()]


def _render_overload(
    kind: PotentialKind, source: str | None, parameters: tuple[tuple[str, str], ...]
) -> str:
    literal = ", ".join(json.dumps(name) for name in kind.names)
    arguments = [("type", f"Literal[{literal}]", False)]
    if source is not None:
        arguments.append((source, SOURCE_PARAMETERS[source], False))
    arguments.extend((name, annotation, True) for name, annotation in parameters)
    arguments.extend((name, annotation, True) for name, annotation in MODIFIERS.items())

    lines = ["    @overload", "    def __init__(", "        self,", "        *,"]
    for name, annotation, optional in arguments:
        default = " = ..." if optional else ""
        lines.append(f"        {name}: {annotation}{default},")
    lines.append("    ) -> None: ...")
    return "\n".join(lines)


def generate() -> str:
    modifier_arguments = "\n".join(
        f"        {name}: {annotation} = ...," for name, annotation in MODIFIERS.items()
    )
    blocks = [
        "    @overload\n    def __init__(self, filename: str, /) -> None: ...",
        "    @overload\n    def __init__(\n        self,\n        component: _ToPotential | _PotentialParams,\n        /,\n        *components: _ToPotential | _PotentialParams,\n    ) -> None: ...",
        "    @overload\n    def __init__(\n        self, potential: _AgamaCallable, /, *, symmetry: _Symmetry\n    ) -> None: ...",
        f"    @overload\n    def __init__(\n        self,\n        *,\n        file: str,\n{modifier_arguments}\n    ) -> None: ...",
        f"    @overload\n    def __init__(\n        self,\n        *,\n        potential: _ToPotential,\n{modifier_arguments}\n    ) -> None: ...",
    ]
    for kind in POTENTIALS:
        sources: tuple[str | None, ...] = kind.sources or (None,)
        for source in sources:
            for branch in _parameter_branches(kind):
                blocks.extend(
                    _render_overload(kind, source, spelling)
                    for spelling in _spellings(branch)
                )
    return "\n".join(blocks) + "\n"


def updated_source(source: str) -> str:
    before, separator, remainder = source.partition(START)
    if not separator:
        raise RuntimeError(f"missing start marker in {TARGET}")
    _, separator, after = remainder.partition(END)
    if not separator:
        raise RuntimeError(f"missing end marker in {TARGET}")
    return before + START + generate() + END + after


def main() -> int:
    parser = argparse.ArgumentParser()
    _ = parser.add_argument(
        "--check", action="store_true", help="fail if the generated section is stale"
    )
    args = parser.parse_args(namespace=_Arguments())
    source = TARGET.read_text()
    updated = updated_source(source)
    if args.check:
        if source != updated:
            parser.error(
                f"{TARGET.relative_to(ROOT)} is stale; run {Path(__file__).name}"
            )
        return 0
    _ = TARGET.write_text(updated)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
