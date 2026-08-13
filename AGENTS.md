# Repository guide

## Purpose and layout

This repository publishes third-party type stubs for the runtime `agama` package.
It uses a flat layout, following scipy-stubs: the distributable stub package is
`agama-stubs/`, inference tests are in `tests/`, and project configuration lives
in `pyproject.toml`.

`agama-stubs/__init__.pyi` explicitly re-exports the public API. Declarations are
grouped by concern in `_potential.pyi`, `_actions.pyi`, `_galaxy.pyi`, and
`_functions.pyi`; the nominal runtime-only `Orbit` class lives in `_orbit.pyi`
to avoid circular imports. Keep `py.typed` in the package directory so built
wheels are recognized as stub-only packages.

## Development workflow

- Use Python 3.13 and `uv` for environments, dependencies, and builds.
- Run `just sync` after cloning or changing development dependencies.
- Run `just basedpyright`, `just basedmypy`, `just ty`, or `just pyrefly` to
  exercise one type checker. The shared fixture set currently covers Density,
  ActionFinder, and generated constructor calls; the other fixtures describe
  unfinished stub coverage and are not in the passing validation set.
- Run `just format` after editing Python or stub files. Run `just ready` to
  regenerate overloads, format the repository, and perform complete validation.
- Run `just check` before finishing a change. It is the single entry point for
  generator freshness, Ruff formatting and linting, all four type checkers, and
  package building.
- Run `just build` when only package artifacts are needed, and `just clean` to
  remove generated artifacts.
- Use `just --list` to discover the available recipes.
- Edit `scripts/potential_spec.py` for `Potential` and
  `scripts/constructor_spec.py` for `Density`, `DistributionFunction`, `Target`,
  and `Component`; do not edit their marked generated constructor sections
  directly. Methods and other declarations remain handwritten. Run
  `just generate` after changing a specification; `just check` verifies that
  generated declarations are current.
- Edit `scripts/result_dispatch_spec.py` and
  `scripts/generate_result_overloads.py` for generated literal-flag, input-rank,
  and dtype dispatch. This generator owns both Potential evaluation methods,
  action calls, DF calls, GalaxyModel result methods, and `orbit`. Do not edit
  their marked sections directly.

## Stub conventions

- Treat the installed `agama` runtime as authoritative. Inspect public objects
  and signatures, and use small safe probes when behavior is unclear.
- Preserve runtime parameter names, positional-only and keyword-only markers,
  defaults, descriptors, and public attributes.
- The project requires Python 3.13, so use modern typing syntax: PEP 695 type
  parameters and aliases, `X | Y`, and built-in collection types.
- Prefer precise protocols, overloads, and concrete domain types over `Any`.
  Use `Any` only for genuinely unrestricted runtime behavior.
- Import NumPy typing helpers as `from optype import numpy as onp`. Preserve
  array dimensionality and dtype behavior rather than broadening to an
  unshaped array.
- Keep `.pyi` files concise. Add realistic `assert_type` cases under `tests/`
  whenever a public contract is added or corrected.
- Do not weaken strict checker settings or add broad suppressions to make a
  change pass.

## Finishing changes

Review the built wheel to ensure all `agama-stubs/*.pyi` modules and `py.typed`
are present, run `just check`, and inspect the final diff for stale paths,
accidental private APIs, imprecise types, and unrelated edits.
