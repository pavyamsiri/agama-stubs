import agama

# Canonical names and the commonly used lowercase spellings are supported.
agama.Potential(type="Plummer", mass=1.0, scaleRadius=2.0)
agama.Potential(type="plummer", mass=1.0, rscale=2.0)
agama.Potential(type="Logarithmic", v0=220.0, p=0.9, axisRatioZ=0.8)
agama.Potential(type="MiyamotoNagai", mass=1.0, scaleRadius=2.0, scaleRadius2=0.2)

# Normalization aliases and mutually exclusive normalization families expand
# into distinct overloads.
agama.Potential(type="Disk", Sigma0=1.0, rscale=2.0, scaleHeight=0.2)
agama.Potential(type="Spheroid", rho0=1.0, scaleRadius=2.0, p=0.9, q=0.8)

# Expansion inputs are mutually exclusive source overloads.
density: agama.Density
potential: agama.Potential
agama.Potential(type="Multipole", density=density, lmax=4)
agama.Potential(type="Multipole", potential=potential, lmax=4)
agama.Potential(type="Multipole", file="coefficients.ini", lmax=4)

# Existing potentials and INI files can also be wrapped without a type.
agama.Potential(file="potential.ini", center=(1.0, 2.0, 3.0))
agama.Potential(potential=potential, rotation=0.5)
