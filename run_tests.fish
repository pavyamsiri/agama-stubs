#!/usr/bin/env fish

# Build the package
uv build

# Find the latest built wheel
set wheel (ls -t dist/*.whl | head -n1)

if test -z "$wheel"
    echo "Error: No wheel found in dist/"
    exit 1
end

echo "Running type tests using wheel: $wheel"

# Run basedpyright
# We use --with to include the built wheel and its dependencies in a temporary environment
uv run --with basedpyright --with numpy --with optype --with "$wheel" basedpyright tests/test_density.pyi
uv run --with basedpyright --with numpy --with optype --with "$wheel" basedpyright tests/test_actionfinder.pyi
