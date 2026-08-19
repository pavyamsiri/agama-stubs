"""Generate dynamic constructors other than ``Potential``."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from scripts.constructor_spec import (
    DENSITIES,
    DFS,
    TARGETS,
    Argument,
    ConstructorVariant,
)

ROOT = Path(__file__).resolve().parents[1]


def branches(variant: ConstructorVariant) -> list[tuple[Argument, ...]]:
    result: list[tuple[Argument, ...]] = [variant.arguments]
    for choices in variant.exclusive_aliases:
        choice_names = {choice.name for choice in choices}
        result = [
            tuple(argument for argument in branch if argument.name not in choice_names)
            + (choice,)
            for branch in result
            for choice in choices
        ]
    return result


def render(variant: ConstructorVariant) -> str:
    literal = ", ".join(json.dumps(value) for value in variant.discriminator)
    blocks: list[str] = []
    for arguments in branches(variant):
        lines = [
            "    @overload",
            "    def __init__(",
            "        self,",
            "        *,",
            f"        type: Literal[{literal}],",
        ]
        for argument in arguments:
            default = "" if argument.required else " = ..."
            lines.append(f"        {argument.name}: {argument.annotation}{default},")
        lines.append("    ) -> None: ...")
        blocks.append("\n".join(lines))
    return "\n".join(blocks)


def density() -> str:
    prefix = """    @overload
    def __init__(self, cumulmass: onp.ToJustFloat64_2D) -> None: ...
    @overload
    def __init__(self, filename: str) -> None: ...
    @overload
    def __init__(self, component: Density, /, *components: Density) -> None: ...
    @overload
    def __init__(self, density: _AgamaCallable, /, *, symmetry: _Symmetry) -> None: ..."""
    return "\n".join((prefix, *(render(item) for item in DENSITIES))) + "\n"


def distribution_function() -> str:
    prefix = """    @overload
    def __init__(
        self,
        component: _ToDistributionFunction,
        /,
        *components: _ToDistributionFunction,
    ) -> None: ..."""
    return "\n".join((prefix, *(render(item) for item in DFS))) + "\n"


def target() -> str:
    return "\n".join(render(item) for item in TARGETS) + "\n"


def component() -> str:
    return """    @overload
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
"""


REGIONS = {
    ROOT / "agama-stubs" / "_potential.pyi": {"DENSITY": density()},
    ROOT / "agama-stubs" / "_galaxy.pyi": {
        "COMPONENT": component(),
        "DISTRIBUTION_FUNCTION": distribution_function(),
        "TARGET": target(),
    },
}


def update(source: str, name: str, generated: str) -> str:
    start = f"    # BEGIN GENERATED {name} INIT OVERLOADS\n"
    end = f"    # END GENERATED {name} INIT OVERLOADS\n"
    before, separator, remainder = source.partition(start)
    if not separator:
        raise RuntimeError(f"missing marker {start.strip()}")
    _, separator, after = remainder.partition(end)
    if not separator:
        raise RuntimeError(f"missing marker {end.strip()}")
    return before + start + generated + end + after


def main() -> int:
    class _Arguments(argparse.Namespace):
        check: bool = False

    parser = argparse.ArgumentParser()
    _ = parser.add_argument("--check", action="store_true")
    check = parser.parse_args(namespace=_Arguments()).check
    stale: list[Path] = []
    for path, regions in REGIONS.items():
        source = path.read_text()
        result = source
        for name, generated in regions.items():
            result = update(result, name, generated)
        if result != source:
            stale.append(path)
            if not check:
                _ = path.write_text(result)
    if check and stale:
        parser.error(
            "stale generated constructors: "
            + ", ".join(str(path.relative_to(ROOT)) for path in stale)
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
