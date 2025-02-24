# mufem-examples

A collection of validation examples for [μfem](http://www.raiden-numerics.com/mufem) ([version](VERSION)).

Run with:
```bash
> pip install mufem==0.0.2
> cd Electromagnetics/Compumag-Team1b-Felix-Cylinder
> mpiexec python3 case.py
```
(skip mpiexec if you want to run in serial).

## Validation cases

### Electromagnetics

- [Compumag TEAM-1b: The Felix Cylinder](Electromagnetics/Compumag-Team1b-Felix-Cylinder/README.md)
- [Compumag TEAM 20: 3D Static Force Problem](Electromagnetics/Compumag-Team20-3D-Static-Force-Problem/README.md)
- [Compumag TEAM 24: Locked Rotor](Electromagnetics/Compumag-Team24-Locked-Rotor/README.md)

## Continuous Integration

[![Run Examples](https://github.com/Raiden-Numerics/mufem-examples/actions/workflows/run_cases.yml/badge.svg)](https://github.com/Raiden-Numerics/mufem-examples/actions/workflows/run_cases.yml)
[![Python Black](https://github.com/Raiden-Numerics/mufem-examples/actions/workflows/black-check.yaml/badge.svg)](https://github.com/Raiden-Numerics/mufem-examples/actions/workflows/black-check.yaml)
[![Python flake8](https://github.com/Raiden-Numerics/mufem-examples/actions/workflows/flake8.yaml/badge.svg)](https://github.com/Raiden-Numerics/mufem-examples/actions/workflows/flake8.yaml)
