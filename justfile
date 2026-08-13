set shell := ["bash", "-cu"]

stubs := "agama-stubs"
typing_tests := "tests/test_density.pyi tests/test_actionfinder.pyi tests/test_potential.pyi tests/test_constructors.pyi tests/test_results.pyi"
scripts := "scripts"
sources := stubs + " " + typing_tests + " " + scripts
python := ".venv/bin/python"

default: check

check: generate-check format-check lint basedpyright basedmypy ty pyrefly build

ready:
    just generate
    just format
    just check

# Regenerate dynamic constructor overloads from their specifications.
generate:
    {{python}} -m scripts.generate_potential_overloads
    {{python}} -m scripts.generate_constructor_overloads
    {{python}} -m scripts.generate_result_overloads

# Check that generated constructor overloads are current.
generate-check:
    {{python}} -m scripts.generate_potential_overloads --check
    {{python}} -m scripts.generate_constructor_overloads --check
    {{python}} -m scripts.generate_result_overloads --check

format:
    .venv/bin/ruff check --fix {{sources}}
    .venv/bin/ruff format {{sources}}

format-check:
    .venv/bin/ruff format --check {{sources}}

lint:
    .venv/bin/ruff check {{sources}}

basedpyright:
    .venv/bin/basedpyright {{sources}}

basedmypy:
    .venv/bin/mypy --no-incremental --no-strict --strict --disable-error-code=explicit-any --disable-error-code=misc --disable-error-code=explicit-override --disable-error-code=override --disable-error-code=type-arg --disable-error-code=import-untyped --disable-error-code=subclass-any --disable-error-code=no-any-unimported --disable-error-code=attr-defined --python-executable {{python}} --python-version 3.13 {{sources}}

basedmypy-audit:
    .venv/bin/mypy --no-incremental --no-strict --strict --disable-error-code=explicit-any --disable-error-code=misc --python-executable {{python}} --python-version 3.13 {{sources}}

ty:
    .venv/bin/ty check --python .venv --extra-search-path . {{sources}}

pyrefly:
    .venv/bin/pyrefly check --python-interpreter-path {{python}} --search-path . --summary=none --progress-bar no {{sources}}

# Install the project and development dependency group.
sync:
    uv sync --dev

# Build the source distribution and wheel.
build:
    uv build

# Remove generated package artifacts.
clean:
    #!/usr/bin/env bash
    shopt -s nullglob
    artifacts=(build/* dist/*.whl dist/*.tar.gz)
    if ((${#artifacts[@]})); then
        rm -r -- "${artifacts[@]}"
    fi
