# SciMatic

A Python library for mathematics, statistics, science, and scientific computing.

SciMatic is a lightweight, student-friendly Python library designed to make mathematical and scientific calculations easier to perform programmatically.

«From basic mathematics to advanced scientific concepts — all in Python(Include rust extension).»

---

# Features

SciMatic is built around modular mathematical tools.

# Mathematics

- Quadratic equations
- Quadratic inequalities
- Factorials
- Mathematical operators
- PEMDAS/BODMAS expression evaluation
- Custom mathematical functions

 # Statistics

- Mean
- Median
- Mode
- Quartiles
- Deciles
- Percentiles
- Interpolation

# Trigonometry

- Law of Sines
- Law of Cosines
- Trigonometric calculations
- Triangle-related mathematics

# Parser

SciMatic includes a general-purpose parser for processing mathematical expressions and tokens.

The parser can split input into:

- Characters
- Words
- Tokens
- Keyword Arguments

It can also convert recognized tokens into numerical values such as integers and floats.

# Scientific Computing

SciMatic is designed to eventually expand beyond pure mathematics into scientific computing, including modules for:

- Physics
- Thermodynamics
- Calculus
- Engineering mathematics
- Advanced scientific calculations

# Computer Engineering

SciMatic also offers functions that are in the computer engineering field.
- Logic Gates
- 7-Segment Display system
- Half/Full Adders
- High-Performance signal flickers

# Databasing
SciMatic also offers a database to store all the returned values with just a decorator.
- Storing returned values, no matter the type
- displaying the values stored
- deleting certain functions

# Conversion
SciMatic has functions that can convert certain measures from time, measurements, etc.
- Imperial-to-metric conversion(v.v.)(from quetto to quetta)
- Currency conversion(uses another database for offline mode)
- temperature conversion(supports °C, °F, k, °R, °Ré)
- Time conversion

# CSV 
SciMatic has functions that enable it to modify, duplicate, and read/write .csv files.
- Serialization/Deserialization of CSV values
- Read/Write .csv files
- Special Bracket convention to distinguish SciMatic-Made duplicates from other common convention(example[1].csv)

---

# Installation

Install SciMatic using pip:
```
pip install scimatic
```
Then import it in Python:
```
import scimatic
```
---

# Quick Start

Basic calculations
```
import scimatic

print(scimatic.utils.convenient_utils.factorial(5))
```
Output:
```
120
```
---

# Expression Parsing

SciMatic can be used to process mathematical expressions while respecting operator precedence.

For example:
```
equation = '2 + 3 * 4'
```
SciMatic evaluates multiplication before addition:
```
2 + (3 * 4)
```
Result:
```
14
```
SciMatic's expression system supports operators such as:
```
+
-
*
/
//
%
**
```
and parentheses.

---

# Quadratics

SciMatic provides tools for solving quadratic equations.

For an equation such as:
```
x² + 5x + 6 = 0
```
SciMatic can determine its roots:
```
x = -2
x = -3
```
The quadratic module is designed to provide a convenient programmatic interface for algebraic calculations.

---

# Statistics

SciMatic provides common statistical operations.

Example:
```
data = [10, 20, 20, 30, 40]
```
You can calculate values such as:
```
Mean
Median
Mode
Quartiles
Percentiles
```
SciMatic also supports interpolation-based statistical calculations.

---

# Modular Architecture

SciMatic is designed as a modular library.

A simplified structure looks like:
```
SciMatic/
├── .github/workflows
|
├── .gitigore
|
├── Cargo.toml
|
├── pyproject.toml
|
├── README.md <- you are here
|
├── RULES.md
|
├──LICENSE
|
├── src/
|   ├── lib.rs
|   ├── flicker.rs
|   └── conversion.rs
|
└── scimatic/
    |
    ├── _pycache_/
    |
    ├── __init__.py
    |
    ├── utils/
    |    ├── __init__.py
    |    ├── databasing.py
    |    ├── convenient_utils.py
    |    ├── csv.py
    |    └── conversion/
    |        ├── __init__.py
    |        ├── currency.py
    |        ├── data.py
    |        ├── measurements.py
    |        ├── time.py
    |        ├── temperature.py
    |        └── weight.py
    |
    ├── c_engineering/
    |   ├── __init__.py
    |   ├── circuits.py
    |   ├── logic_gates.py
    |   ├── seg_7display.py
    |   └── signals.py
    |
    ├── mathematic/
    |   ├── __init__.py
    |   ├── algebra.py
    |   ├── errors.py
    |   ├── geometry.py
    |   ├── niche.py
    |   └── statistics.py
    │
    └── scientific/
        └── mechanics.py
```

This allows different areas of mathematics and science to remain separated while still being part of the same library.

---

# Error Handling

SciMatic provides specialized exceptions for mathematical errors.

Examples include:
```
DataError
NegativeDiscriminantError
VariableError
```
These errors are intended to make invalid mathematical input easier to identify and handle.

---

# Philosophy

SciMatic is designed around three principles:

Simple

Mathematical operations should be easy to understand and use.

Modular

Different mathematical disciplines should be separated into dedicated modules.

Extensible

SciMatic should be able to grow from a mathematics library into a broader scientific-computing ecosystem.

---

# Development

SciMatic is currently under active development.

The project is intended to expand into areas such as:

- Advanced calculus
- Thermodynamics
- Physics
- Scientific simulations
- More advanced statistics
- Probability
- Engineering mathematics
- Scientific computing

---

# Roadmap

## Mathematics

- [x] Basic mathematical utilities
- [x] Expression parser
- [x] Operator handling
- [x] Quadratic calculations
- [x] Statistical utilities
- [x] Trigonometric utilities
- [ ] More advanced calculus
- [ ] More advanced algebra

## Statistics

- [x] Mean
- [x] Median
- [x] Mode
- [x] Quartiles
- [x] Percentiles
- [x] Interpolation
- [ ] Advanced statistical analysis

## Science

- [ ] Physics module
- [ ] Thermodynamics
- [ ] Scientific constants
- [ ] Engineering calculations
- [ ] Advanced scientific simulations

## Computer Engineering
- [x] Logic Gates
- [x] Binary translation
- [x] 7-display
- [x] Circuitry

## Future

- [ ] Improved documentation
- [ ] More comprehensive testing
- [ ] Performance optimization
- [ ] Expanded API
- [ ] Educational examples

---

# Contributing

Contributions, suggestions, and bug reports are welcome.

If you find a bug or have an idea for SciMatic, feel free to open an issue or submit a pull request.

When contributing, please try to keep new functionality modular and well documented.

---

# License

SciMatic is distributed under its project license.

See the "LICENSE" file for the full license terms.

---

# Author

SciMatic is an independently developed Python project focused on making mathematics and scientific computing accessible through code.

---

# Support the Project

If you find SciMatic useful, consider giving the project a ⭐ on GitHub.

Every improvement, experiment, and contribution helps SciMatic grow.

SciMatic — Mathematics, engineered for Python.
