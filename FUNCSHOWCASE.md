# SciMatic functions

## Terminologies you may come across

### Asynchronous Programming
- A programming model that allows tasks to perform work without blocking other tasks while waiting for operations to finish.
- In Python, asynchronous programming commonly uses async, await, and asyncio.

### Database
- An organized system used to store, retrieve, and manage data.
SciMatic uses SQLite to store data locally.

### print_result
- A parameter used by many SciMatic functions to display their result directly in the terminal.
- When ```print_result=True```, there is no need to wrap the function call in ```print()```.

### Binary
- The binary number system, which uses only 0 and 1.
- Computers commonly use binary to represent and process data.

### Flick
- Refers to flipping Boolean or binary values.
- True becomes False, and False becomes True.
- 1 becomes 0, and 0 becomes 1.

### AsyncGenerator
- A generator created by an asynchronous function.
- Async generators can produce values over time and are consumed using ```async for```.

### Async Function
- A function declared using ```async def```.
- An async function returns a coroutine when called.
- A coroutine can be executed with ```asyncio.run()``` when it is not already inside an active event loop.

### sqlite3
- Python's standard-library interface for working with SQLite databases.
- SQLite is a lightweight, serverless database engine that is in the public domain.

### CSV
- CSV (Comma-Separated Values) is a plain-text format commonly used to store tabular data.
- Values are typically separated by commas, while rows are separated by newlines.
- SciMatic provides a custom `CSV` class for reading, writing, parsing, modifying, and duplicating CSV files.

### Matrix
- A matrix (plural: matrices) is a rectangular arrangement of values organized into rows and columns.
- In SciMatic, matrices are represented using nested Python lists.
- The length of the outer list (`len(matrix)`) represents the number of rows.
- The length of each child list represents the number of columns.

For example:

```python
matrix = [
	[1, 2, 3],
	[4, 5, 6]
]
```
- In this example, the matrix contains 2 rows and 3 columns.
---
## mathematic/

### - algebra.py
```quadratic_equation(a, b, c, x, print_result=False)```

```python
from scimatic.mathematic.algebra import quadratic_equation

quadratic_equation(1, 7, 3, 4, print_result=True)
# Output: 47
```

```quadratic_formula(a, b, c, print_result=False, vietas_formula=False)```

```python
from scimatic.mathematic.algebra import quadratic_formula

quadratic_formula(1, 7, 3, print_result=True, vietas_formula=True)
# Output: x1 = -0.459 x2 = -6.541, x1 + x2 = -7
```

```quadratic_inequality(a, b, c, symbol, print_result=False)```

```python
from scimatic.mathematic.algebra import quadratic_inequality

quadratic_inequality(1, 7, 3, '<', print_result=True)
# Output: '-6.541 < x < -0.459'
```

```pythagorean_theorem(a, b, c=None, print_result=False)```

```python
from scimatic.mathematic.algebra import pythagorean_theorem

pythagorean_theorem(1, 7, 3, print_result=True)
pythagorean_theorem(1, 7, print_result=True)
# Output: 3^2 = 1^2 + 7^2
#                                                                        False
# Output: sqrt(1^2 + 7^2) = 5sqrt(2) or 7.071
```

### - statistics.py
```quartile(raw_data, k, print_result=False)```
```python
from scimatic.mathematic.statistics import quartile

quartile([1, 2, 3, 4, 5], 2, print_result=True)
# Output: 3.0
```

```decile(raw_data, k, print_result=False)```
```python
from scimatic.mathematic.statistics import decile

decile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 5, print_result=True)
# Output: 6.0
```

```percentile(raw_data, k, print_result=False)```
```python
from scimatic.mathematic.statistics import percentile

percentile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 50, print_result=True)
# Output: 6.0
```

```median(raw_data, print_result=False)```
```python
from scimatic.mathematic.statistics import median

median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], print_result=True)
# Output: 6.0
```

```mean(raw_data, print_result=False)```
```python
from scimatic.mathematic.statistics import mean

mean([1, 1, 2, 2, 3], print_result=True)

# Output: 2.2
```

```mode(raw_data, k=1, print_result=False)```
```python
from scimatic.mathematic.statistics import mode

mode([2, 3, 3, 3, 4, 4, 5], k=2, print_result=True)

# Output: [3, 4]
```
• Note: Statistical Functions can have an unsorted input and the same result applies

### - geometry.py
```sin_law(case, a, b, c, print_result=False)```
```python
from scimatic.mathematic.geometry import sin_law

sin_law('SAA', 3, 40, 120, print_result=True)
sin_law('ASA', 50, 2, 127, print_result=True)
sin_law('SSA', 3, 4, 120, print_result=True)
sin_law('SSA', 5, 8, 30, print_result=True)
sin_law('SSA', 8, 10, 30, print_result=True)

# Output: Angle B = 20, Side b = 2.227, Side c = 1.185
# Output: Angle A = 3, Side b = 29.274, Side c = 30.520
# Output: No valid triangle is formed...
# Output: [{'angle B': 53.130, 'angle C': 96.870, 'side b': 9.928}]
# Output: [{'angle B': 38.682, 'angle C': 111.318, 'side b': 14.905}, {'angle B': 141.318, 'angle C': 8.682, 'side b': 2.415}]
```
• Note: AAS cases will get reverted to SAA cases so if you flip the first examples a and c parameter and switched SAA key to AAS, it will output the same stuff.

```cos_law(case, a, b, c, print_result=False)```

```python
from scimatic.mathematic.geometry import cos_law

cos_law('SSS', 2, 3, 4, print_result=True)
cos_law('SAS', 2, 50, 4, print_result=True)

# Output: Angle A: 28.955, Angle B: 46.567, Angle C: 104.478
# Output: side c: 3.117, Angle A: 29.441, Angle B: 100.559
```
```
area_circle()
circumference_circle()
volume_circular()

perimeter_triangle()
area_triangle()

perimeter_parallelogram()
area_parallelogram()

perimeter_trapezoid()
area_trapezoid()

perimeter_square()
area_square()

perimeter_rect()
area_rect()

perimeter_polygon()
area_polygon()

volume_cube()
volume_cuboid()
volume_prism()
volume_pyramid()
```
- These functions calculate the perimeter, area, or volume of their respective geometric shapes.
- If you know any basic math, I am sure you can intuitively guess each ones parameters as it follows their respective formulas.
```python
from scimatic.mathematic.geometry import area_circle

area_circle(40, print_result=True)

# Output: 5026.54...
```
### - niche.py
```fibonacci(iterations)```

```python
from scimatic.mathematic.niche import fibonacci

fib = fibonacci(10)

for value in fib:
                print(value)

# Output: 
#                0
#                1
#                1
#                2
#                3
#                5
#                8
#                13
#                21
#                34
#                55
```

```collatz(n, print_result=False)```

```python
from scimatic.mathematic.niche import collatz

collatz(10, print_result=True)

# Output: [10, 5, 16, 8, 4, 2, 1]
```

```ackermann(array, m, n)```

```python
from scimatic.mathematic.niche import ackermann

initiator = []

result = ackermann(initiator, 3, 2)

print(result)

# Output: 29
```

### - errors.py

Tip: Install the errors file like any other file in this markdown, and use them like pythons built-in errors.

## scientific/

### mechanics.py
```momentum(mass, velocity, print_result=False)```

```python
from scimatic.scientific.mechanics import momentum

momentum(25, 60, print_result=True)

# Output: Momentum: 1500 kg•m/s
```

```impulse(force, initial_time, final_time, print_result=False, return_deltat=False)```

```python
from scimatic.scientific.mechanics import impulse

impulse(67, 10, 60, print_result=True, return_deltat=True)

# Output: Impulse: 3350N•s, Δt = 50s
```

## c_engineering/

### logic_gates.py

```AND(bool1, bool2, binary=False)```

```python
from scimatic.c_engineering.logic_gates import AND

print(AND(True, True))
print(AND(1, 1, binary=True))
print(AND(True, True, binary=True))
print(AND(1, 1))

print(AND(True, False))
print(AND(1, 0, binary=True))
print(AND(True, False, binary=True))
print(AND(1, 0))

# Output(True, True):
#                True
#                1
#                1
#                True

# Output(True, False):
#                False
#                0
#                0
#                False
```

```NOT(value, binary=False)```

```python
from scimatic.c_engineering.logic_gates import NOT

print(NOT(1))
print(NOT(0))

# Output: False
# Output: True
```

```OR(a, b, binary=False)```

```python
from scimatic.c_engineering.logic_gates import OR

print(OR(0, 0))
print(OR(0, 1))
print(OR(1, 0))
print(OR(1, 1))

# Output: False
# Output: True
# Output: True
# Output: True
```

```NAND(a, b, binary=False)```

```python
from scimatic.c_engineering.logic_gates import NAND

print(NAND(0, 0))
print(NAND(0, 1))
print(NAND(1, 0))
print(NAND(1, 1))

# Output: True
# Output: True
# Output: True
# Output: False
```

```NOR(a, b, binary=False)```
```python
from scimatic.c_engineering.logic_gates import NOR

print(NOR(0, 0))
print(NOR(0, 1))
print(NOR(1, 0))
print(NOR(1, 1))

# Output: True
# Output: False
# Output: False
# Output: False
```


```XOR(a, b, binary=False)```
```python
from scimatic.c_engineering.logic_gates import XOR

print(XOR(0, 0))
print(XOR(0, 1))
print(XOR(1, 0))
print(XOR(1, 1))

# Output: False
# Output: True
# Output: True
# Output: False
```

```XNOR(a, b, binary=False)```
```python
from scimatic.c_engineering.logic_gates import XNOR

print(XNOR(0, 0))
print(XNOR(0, 1))
print(XNOR(1, 0))
print(XNOR(1, 1))

# Output: True
# Output: False
# Output: False
# Output: True
```

### - seg_7display.py 

```display_to_7seg(character, binary=False)```
```python
from scimatic.c_engineering.seg_7display import display_to_7seg

print(display_to_7seg("8"))

# Output: (1, 1, 1, 1, 1, 1, 1)
```
Note: The "8" character activates every segment of the display.

### circuits.py

```half_adder(a, b, binary=False)```
```python
from scimatic.c_engineering.circuits import half_adder

print(half_adder(0, 0))
print(half_adder(0, 1))
print(half_adder(1, 0))
print(half_adder(1, 1))

# Output: (False, False)
# Output: (True, False)
# Output: (True, False)
# Output: (False, True)
```

```full_adder(a, b, carry_in, binary=False)```
```python
from scimatic.c_engineering.circuits import full_adder

print(full_adder(0, 0, 0))
print(full_adder(0, 1, 0))
print(full_adder(1, 1, 0))
print(full_adder(1, 1, 1))

# Output: (False, False)
# Output: (True, False)
# Output: (False, True)
# Output: (True, True)
```

### Signals.py

• SciMatic's signal functions are backed by its high-performance Rust extension.

• They can be used to create flickering, delayed, and pulsed binary signals.

```flick(digits, binary=False, print_result=False)```
```python
from scimatic import flick

flick([True, False, True, True], print_result=True)

# Output: [False, True, False, False]
```
• Note: The function processes the supplied signal and produces a flickering signal.

```delay(digits, duration, binary=False, print_result=False)```
```python
from scimatic.c_engineering.signals import delay
import asyncio

asyncio.run(delay([True, False, True], 1, print_result=True))

# Output: -1s-> [False, True, False]
```
• Note: The signal is delayed by the specified duration.

```pulse(digits, iterations, interval, binary=False)```
```python
from scimatic.c_engineering.signals import pulse
import asyncio

async def main():
                async for p in pulse([True, False, True], 3, 0.5):
                                print(p)
asyncio.run(main())

# Output: [False, True, False] -0.5s-> [True, False, True] -0.5-> [False, True, False]
```
• Note: The signal is repeated for the specified number of iterations, with the given interval between pulses.

• Note: ```pulse()``` and ```delay()``` are async functions so you would need ```asyncio``` to run these functions.

### Binary Mode

- Many of SciMatic's computer-engineering functions support:

```binary=True```

- This allows inputs and outputs to be handled as binary representations rather than ordinary Boolean values.

For example:
```python
from scimatic.c_engineering.logic_gates import XOR

print(XOR(1, 0, binary=True))

1
```
- This makes the functions useful for experimenting with digital logic and binary systems directly from Python.

## utils/

### convenient_utils.py
```CreateParsable(text)```
- This class takes the ```text``` parameter and makes it usable for parsing.
- CreateParsable has 3 attributes namely ```.parse_letter()```, ```.parse_word()```, and ```.parse_token()```
Eg.

```python
from scimatic.utils.convenient_utils import CreateParsable

test_subject = '123 Northwood Street' # Not my real address

syntax = CreateParsable(test_subject)
key = CreateParsable("name=Paul age=15 gender= mode='w' json=data.json")

print(syntax.parse_letter()) # parses per letter
print(syntax.parse_word()) # parses per word(word determined by whitespace, so 'NorthwoodStreet' outputs ['NorthwoodStreet']
print(syntax.parse_token()) # parses per word and converts numbers into integers or floats
print(key.parse_kwargs(save_json=True, print_result=True))

# Output: ['1', '2', '3', 'N', 'o', 'r', 't', 'h', 'w', 'o', 'o', 'd', 'S', 't', 'r', 'e', 'e', 't']
# Output: ['123', 'Northwood', 'Street']
# Output: [123, 'Northwood', 'Street']
# Output: {'name': 'Paul', 'age': 15, 'gender': None}
```
- Note: If save_json is enabled, parse_kwargs tries to find a key named json and a key named mode(determines if the method of input is w, r+, or w+)(Optional because it just defaults to w) with a value .json and saves the parsed output into the json values .json file.

```Operator```
- A type annotation for operators such as +, -, etc.

```python
from scimatic.utils.convenient_utils import Operator

def addition_op() -> Operator:
                return '+'
print(addition_op())

# Output: +
```

```calculate(text, print_result=False)```

```python
from scimatic.utils.convenient_utils import calculate

calculate('1 + 1', print_result=True) # calculate uses CreateParsable's .parse_token()

# Output: 2
```
- A restricted arithmetic expression evaluator that uses SciMatic's parsing system instead of directly executing arbitrary Python code.

```factorial(n, print_result=False)```

```python
from scimatic.utils.convenient_utils import factorial

factorial(3, print_result=True)

# Output: 6
```

```int64_limit(unsigned=False, negative_value=False)```
- This just gives the 64-integer limit of 922...07(long number, think the backrooms level true end)

```python
from scimatic.utils.convenient_utils import int64_limit

print(int64_limit())
print(int64_limit(unsigned=True))
print(int64_limit(negative_value=True))

# Output:
# 9,223,372,036,854,775,807
# 18,446,744,073,709,551,615
# -9,223,372,036,854,775,807
```
- Theres also an int32, int16, and int8 limit but their parameters are the same, only difference is the naming.

```pi(decimal=None, print_result=True)```

```python
from scimatic.utils.convenient_utils import pi

pi(print_result=True)
pi(2, print_result=True)

# Output: 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
# Output: 3.14
```

### databasing.py
```Database()```
- The class that contains all of ```databasing.py```'s functions
- This class uses an sqlite3 database file(redirected to users application data directory to prevent PermissionError)
- In the showcase of each function, let db = Database()

```@db.store```
- A decorator function used to store the output of each function it decorates.

```python
from scimatic.utils.databasing import Database

db = Database()

@db.store
def add(a, b):
                return a + b
@db.store
def mul(a, b):
                return a * b

add(6, 7)
mul(2, 2)

# Output: 13
# Output: 4
```

```db.get_one(id=None, print_result=False)```

```python
from scimatic.utils.databasing import Database

db = Database()

db.get_one(print_result=True)
db.get_one(1, print_result=True)

# Output: ID: 2                                Date stored: mm/dd/yyyy                                Function: mul                                Return Value: 4                                Version: 1.4.0
# Output: ID: 1                                Date stored: mm/dd/yyyy                                Function: add                                Return Value: 13                                Version: 1.4.0
```
- If the id parameter is None it gets the most recently added value

```db.get_all(print_result=False)```
```python
from scimatic.utils.databasing import Database

db = Database()

db.get_all(print_result=True)

# Output: ID: 1                                Date stored: mm/dd/yyyy                                Function: add                         Return Value: 13                                Version: 1.4.0
#                                                          ID: 2                                Date stored: mm/dd/yyyy                                Function: mul                                Return Value: 4                                Version: 1.4.0
```

```db.delete(id=None, print_result=False)```
```python
from scimatic.utils.databasing import Database

db = Database()

db.delete(1, print_result=True)

# Output: Deleted ID 1
```
- If id is None, delete() will delete the most recent value

```db.reset(print_result=False)```
```python
from scimatic.utils.databasing import Database

db = Database()

db.reset(print_result=True)

# Output: Database reset successfully.
```
- Warning: reset() deletes everything inside data.db

## conversion/

### - measurements.py
```convert_len(n, u_sym1, u_sym2, print_result=False)```
```python
from scimatic.utils.conversion.measurements import convert_len

convert_len(1, 'in', 'm', print_result=True)

# Output: 1in -> 0.0254m
```

```convert_area(n, u_sym1, u_sym2, print_result=False)```
```python
from scimatic.utils.conversion.measurements import convert_area

convert_area(1, 'in2', 'm2', print_result=True)

# Output: 1in2 -> 0.00064516m2
```

### - time.py
```convert_time(t, t_sym1, t_sym2, print_result=False)```
```python
from scimatic.utils.conversion.time import convert_time

convert_time(1, 's', 'ms', print_result=True)

# Output: 1s -> 1000ms
```

### - data.py
```convert_bits(b, b_sym1, b_sym2, print_result=False)```
```python
from scimatic.utils.conversion.data import convert_bits

convert_bits(1, 'b', 'B', print_result=True)

# Output: 1b -> 0.125B
```

### - weight.py
```convert_weight(w, w_sym1, w_sym2, print_result=False)```
```python
from scimatic.utils.conversion.weight import convert_weight

convert_weight(1, 'kg', 'g', print_result=True)

# Output: 1kg -> 1000g
```

### - currency.py
- This one is the elephant in the room, it requires internet as it needs to use [frankfurter](https://frankfurter.dev/)
- This function uses the Frankfurter API to retrieve exchange-rate data.
- SciMatic also provides an offline mode that stores exchange-rate data locally using SQLite.

```fresh_convert_curr(money, curr1, curr2, id=None, save_offline=True, use_offline_db=False, reset_db=False, print_result=False)```
```python
from scimatic.utils.conversion.currency import fresh_convert_curr

fresh_convert_curr(1, 'USD', 'PHP', print_result=True) # The result will store in the database

# Output: 1USD -> <current exchange rate>PHP
```

```cached_convert_curr(money, curr1, curr2, print_result=False)```
```python
from scimatic.utils.conversion.currency import cache_convert_curr

for _ in range(3):
		cache_convert_curr(1, 'USD', 'PHP', print_result=True)

# Output: 1USD -> <current exchange rate>PHP
# Bottom line: This function sacrifices the offline features fresh_convert_curr has for speed via caching the result.
```

```convert_binary(b, print_result=False)```
```python
from scimatic import rs_converters

rs_converters.convert_binary([True, False], print_result=True)

# Output: [1, 0]
```

## csv/

### - CSV
- This class takes a .csv file as an argument and when the .csv file does not exist it creates one in the os' Downloads directory.

```serialize(matrix, write_to_file=False, print_result=False)```
```python
from scimatic.utils.csv import CSV

csv = CSV('example.csv')

csv.serialize(
		[
				[
						'1',
						'2',
						'3'
				], [
						'x',
						'y',
						'z'
				]
		],
		write_to_file=True,
		print_result=True
)

# Output: 1,2,3\nx,y,z\n
# Background Output: The serialized output is written on the file.
```

```deserialize(text, print_result=False)```
```python
from scimatic.utils.csv import CSV

csv = CSV('example.csv')

csv.deserialize('1,2,3\nx,y,z\n')

# Output: [['1', '2', '3'], ['x', 'y', 'z']]
```

```read(print_result=False)```
```python
from scimatic.utils.csv import CSV

csv = CSV('example.csv')

csv.read(print_result=True)

# Output: 
#		1,2,3
#		x,y,z
```

```write(text)```
```python
from scimatic.utils.csv import CSV

csv = CSV('example.csv')

csv.write('4,5,6\na,b,c')

# Background Output: Contents overwrite the current file
```

```rwrite(text, print_result=False)```
```python
from scimatic.utils.csv import CSV

csv = CSV('example.csv')

# Current contents:
# 4,5,6
# a,b,c

old = csv.rwrite('1,2,3\nx,y,z', print_result=True)

# Output:
# 4,5,6
# a,b,c

# The file now contains:
# 1,2,3
# x,y,z
# Background Output: The table gets rewritten.
# Bottom line: rwrite returns the old contents before rewriting meaning old will be the same as the output suggests.
```
- Note: This csv method first reads the old contents and then rewrites it.

```wread(text, print_result=False)```
```python
from scimatic.utils.csv import CSV

csv = CSV('example.csv')

new = csv.wread('4,5,6\na,b,c', print_result=True)

# Output:
#		4,5,6
#		a,b,c
# Background Output: The function wread first rewrites the old contents then returns the new contents.
```

```dup(name=None, ndups=1)```
```python
from scimatic.utils.csv import CSV

csv = CSV('example.csv')

csv.dup(name='dupli.csv')
csv.dup(ndups=4)

# Output: dupli.csv will have the same contents as example.csv
# Output: example[1].csv, example[2].csv, ...
```
- If `name` is provided, `ndups` is ignored and only the specified file is created.
- If `name` is not provided, SciMatic uses bracketed numbering such as `example[1].csv`, `example[2].csv`, and so on.

```add_row(new_row, mode='w', print_result=False)```
```python
from scimatic.utils.csv import CSV

csv = CSV('example.csv')

csv.add_row([['d', 'e', 'f']])

# Output: Row will be added to example.csv
# Bottom line: The add_row method needs a matrix.
```

```delete_row(row_num=None)```
```python
from scimatic.utils.csv import CSV

csv = CSV('example.csv')

csv.delete_row()

# Output: row index 0(4,5,6) will be deleted
```

```add_column(new_col, mode='w', print_result=False)```
```python
from scimatic.utils.csv import CSV

csv = CSV('example.csv')

csv.add_column([['1', '2', '3']])

# Output: Column 1 will be added at the last column.
#																2
#																3
# Bottom line: The given matrix must be a Matrix Transpose:
```

- `add_column()` expects its input in column-oriented form.
- Each child list represents one column.
- The values inside that child list are the values belonging to that column.

For example:

```python
[
	['a', 'b', 'c'],
	['1', '2', '3']
]
```
represents two columns:

```
a  1
b  2
c  3
```

```delete_column(index=None)```
```python
from scimatic.utils.csv import CSV

csv = CSV('example.csv')

csv.delete_column()

# Output: The column we just added will get deleted because no arguments were given at index
```
```replace_cell(coordinates, value)```
```python
from scimatic.utils.csv import CSV

csv = CSV('example.csv')

csv.replace_cell((0, 0), '0')

# Output: The cell(0, 0) value(a) will be replaced with 0
```

```delete_cell(coordinates)```
```python
from scimatic.utils.csv import CSV

csv = CSV('example.csv')

csv.delete_cell((0, 0))

# Output: The value at coordinate (0, 0) will get deleted.

'''
,b,c
d,e,f
'''
```