# SciMatic

A Python library for mathematics, statistics, science, and scientific computing.

SciMatic is a lightweight, student-friendly Python library designed to make mathematical and scientific calculations easier to perform programmatically.

«From basic mathematics to advanced scientific concepts — all in Python.»

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

- Median
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

It can also convert recognized tokens into numerical values such as integers and floats.

# Scientific Computing

SciMatic is designed to eventually expand beyond pure mathematics into scientific computing, including modules for:

- Physics
- Thermodynamics
- Calculus
- Engineering mathematics
- Advanced scientific calculations

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

print(scimatic.factorial(5))
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
│
├── general.py
├── error.py
├── quadratics.py
├── statistics.py
├── trigonometry.py
│
└── scientific/
    ├── physics.py
    └── rocket_science.py(my proposed idea)
```

This allows different areas of mathematics and science to remain separated while still being part of the same library.

---

£ Error Handling

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

- [ ] Mean
- [x] Median
- [ ] Mode
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
- [ ] Logic Gates
- [ ] Binary translation
- [ ] 7-display

## Future

- [ ] Improved documentation
- [ ] More comprehensive testing
- [ ] Performance optimization
- [ ] Expanded API
- [ ] Educational examples
- [ ] Possible integration of a ```ans``` history system with sqlite3

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
