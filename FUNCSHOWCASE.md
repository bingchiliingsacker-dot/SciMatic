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

---

## mathematic/

### - algebra.py
```quadratic_equation(a, b, c, x, print_result=False)```

```python
import scimatic.mathematic.algebra.quadratic_equation as quadratic_equation

quadratic_equation(1, 7, 3, 4, print_result=True)
# Output: 47
```

```quadratic_formula(a, b, c, print_result=False, vietas_formula=False)```

```python
import scimatic.mathematic.algebra.quadratic_formula as quadratic_formula

quadratic_formula(1, 7, 3, print_result=True, vietas_formula=True)
# Output: x1 = -0.459 x2 = -6.541, x1 + x2 = -7
```

```quadratic_inequality(a, b, c, symbol, print_result=False)```

```python
import scimatic.mathematic.algebra.quadratic_inequality as quadratic_inequality

quadratic_inequality(1, 7, 3, '<', print_result=True)
# Output: '-6.541 < x < -0.459'
```

```pythagorean_theorem(a, b, c=None, print_result=False)```

```python
import scimatic.mathematic.algebra.pythagorean_theorem as pythagorean_theorem

pythagorean_theorem(1, 7, 3, print_result=True)
pythagorean_theorem(1, 7, print_result=True)
# Output: 3^2 = 1^2 + 7^2
#									False
# Output: sqrt(1^2 + 7^2) = 5sqrt(2) or 7.071
```

### - statistics.py
```quartile(raw_data, k, print_result=False)```
```python
import scimatic.mathematic.statistics.quartile as quartile

quartile([1, 2, 3, 4, 5], 2, print_result=True)
# Output: 3.0
```

```decile(raw_data, k, print_result=False)```
```python
import scimatic.mathematic.statistics.decile as decile

decile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 5, print_result=True)
# Output: 6.0
```

```percentile(raw_data, k, print_result=False)```
```python
import scimatic.mathematic.statistics.percentile as percentile

percentile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 50, print_result=True)
# Output: 6.0
```

```median(raw_data, print_result=False)```
```python
import scimatic.mathematic.statistics.median as median

median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], print_result=True)
# Output: 6.0
```
• Note: Statistical Functions can have an unsorted input and the same result applies

### - geometry.py
```sin_law(case, a, b, c, print_result=False)```
```python
import scimatic.mathematic.geometry.sin_law as sin_law

sin_law('SAA', 3, 40, 120, print_result=True)
sin_law('ASA', 50, 2, 127, print_result=True)
sin_law('SSA', 3, 4, 120, print_result=True)
sin_law('SSA', 5, 8, 30, print_result=True)
sin_law('SSA', 8, 10, 30, print_result=True)

# Output: Angle B = 20, Side b = 4.038, Side c = 1.603
# Output: Angle A = 3, Side b = 29.29, Side c = 31.47
# Output: No valid triangle is formed...
# Output: [{'angle B': 53.130, 'angle C': 96.870, 'side b': 9.928}]
# Output: [{'angle B': 38.682, 'angle C': 111.318, 'side b': 14.905}, {'angle B': 141.318, 'angle C': 8.682, 'side b': 2.415}]
```
• Note: AAS cases will get reverted to SAA cases so if you flip the first examples a and c parameter and switched SAA key to AAS, it will output the same stuff.

```cos_law(case, a, b, c, print_result=False)```

```python
import scimatic.mathematic.geometry.cos_law as cos_law

cos_law('SSS', 2, 3, 4, print_result=True)
cos_law('SAS', 2, 50, 4, print_result=True)

# Output: Angle A: 28.955, Angle B: 46.567, Angle C: 104.478
# Output: side c: 3.013, Angle A: 30.10, Angle B: 99.90
```

### - niche.py
```fibonacci(iterations)```

```python
import scimatic.mathematic.niche.fibonacci as fibonacci

fib = fibonacci(10)

for value in fib:
		print(value)
		
# Output: 
#		0
#		1
#		1
#		2
#		3
#		5
#		8
#		13
#		21
#		34
#		55
```

```collatz(n, print_result=False)```

```python
import scimatic.mathematic.niche.collatz as collatz

collatz(10, print_result=True)

# Output: [10, 5, 16, 8, 4, 2, 1]
```

```ackermann(array, m, n)```

```python
import scimatic.mathematic.niche.ackermann as ackermann

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
import scimatic.scientific.mechanics.momentum as momentum

momentum(25, 60, print_result=True)

# Output: Momentum: 670.56 kg•m/s
```

```impulse(force, initial_time, final_time, print_result=False, return_deltat=False)```

```python
import scimatic.scientific.mechanics.impulse as impulse

impulse(67, 10, 60, print_result=True, return_deltat=True)

# Output: Impulse: 3350N•s, Δt = 50s
```

## c_engineering/

### logic_gates.py

```AND(bool1, bool2, binary=False)```

```python
import scimatic.c_engineering.logic_gates.AND as AND

print(AND(True, True))
print(AND(1, 1, binary=True))
print(AND(True, True, binary=True))
print(AND(1, 1))

print(AND(True, False))
print(AND(1, 0, binary=True))
print(AND(True, False, binary=True))
print(AND(1, 0))

# Output(True, True):
#		True
#		1
#		1
#		True

# Output(True, False):
#		False
#		0
#		0
#		False
```

```not_gate(value, binary=False)```

```python
from scimatic.c_engineering.logic_gates import not_gate

print(not_gate(1))
print(not_gate(0))

# Output: False
# Output: True
```

```or_gate(a, b, binary=False)```

```python
from scimatic.c_engineering.logic_gates import or_gate

print(or_gate(0, 0))
print(or_gate(0, 1))
print(or_gate(1, 0))
print(or_gate(1, 1))

# Output: False
# Output: True
# Output: True
# Output: True
```

```nand_gate(a, b, binary=False)```

```python
from scimatic.c_engineering.logic_gates import nand_gate

print(nand_gate(0, 0))
print(nand_gate(0, 1))
print(nand_gate(1, 0))
print(nand_gate(1, 1))

# Output: True
# Output: True
# Output: True
# Output: False
```

```nor_gate(a, b, binary=False)```
```python
from scimatic.c_engineering.logic_gates import nor_gate

print(nor_gate(0, 0))
print(nor_gate(0, 1))
print(nor_gate(1, 0))
print(nor_gate(1, 1))

# Output: True
# Output: False
# Output: False
# Output: False
```


```xor_gate(a, b, binary=False)```
```python
from scimatic.c_engineering.logic_gates import xor_gate

print(xor_gate(0, 0))
print(xor_gate(0, 1))
print(xor_gate(1, 0))
print(xor_gate(1, 1))

# Output: False
# Output: True
# Output: True
# Output: False
```

```xnor_gate(a, b, binary=False)```
```python
from scimatic.c_engineering.logic_gates import xnor_gate

print(xnor_gate(0, 0))
print(xnor_gate(0, 1))
print(xnor_gate(1, 0))
print(xnor_gate(1, 1))

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

# Output: 1111111
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

• Note: As of 1.40.0, the 3 functions below strictly need a list of booleans, I am working on a fix to this issue as soon as possible.

```flick(digits, binary=False)```
```python
from scimatic.c_engineering.signals import flick

print(flick([1, 0, 1, 1]))

# Output: [False, True, False, False]
```
• Note: The function processes the supplied signal and produces a flickering signal.

```delay(digits, duration, binary=False)```
```python
from scimatic.c_engineering.signals import delay
import asyncio

print(asyncio.run(delay([1, 0, 1], 1)))

# Output: -1s-> [False, True, True]
```
• Note: The signal is delayed by the specified duration.

```pulse(digits, iterations, interval, binary=False)```
```python
from scimatic.c_engineering.signals import pulse
import asyncio

async def main():
		async for p in pulse([1, 0, 1], 3, 0.5):
				print(p)
asyncio.run(main)

# Output: [False, True, False] -0.5s-> [True, False, True] -0.5-> [False, True, False]
```
• Note: The signal is repeated for the specified number of iterations, with the given interval between pulses.

• Note: ```pulse()``` and ```delay()``` are async functions so you would need ```asyncio``` to run these functions.a

### Binary Mode

- Many of SciMatic's computer-engineering functions support:

```binary=True```

- This allows inputs and outputs to be handled as binary representations rather than ordinary Boolean values.

For example:
```python
from scimatic.c_engineering.logic_gates import xor_gate

print(xor_gate(1, 0, binary=True))

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

print(syntax.parse_letter()) # parses per letter
print(syntax.parse_word()) # parses per word(word determined by whitespace, so 'NorthwoodStreet' outputs ['NorthwoodStreet']
print(syntax.parse_token()) # parses per word and converts numbers into integers or floats

# Output: ['1', '2', '3', 'N', 'o', 'r', 't', 'h', 'w', 'o', 'o', 'd', 'S', 't', 'r', 'e', 'e', 't']
# Output: ['123', 'Northwood', 'Street']
# Output: [123, 'Northwood', 'Street']
```

```Operator```
- A type annotation for operators such as +, -, etc.

```python
from scimatic.utils.convenient_utils import Operator

def addition_op() -> Operator:
		return '+'
print(addition_op)

# Output: +
```

```calculate(text, print_result=False)```

```python
from scimatic.utils.convenient_utils import calculate

calculate('1 + 1', print_result=True) # calculate uses CreateParsable's .parse_token()

# Output: 2
```
- Basically a safer version of ```eval()```

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

print(int64_limit()) # if negative_value is True, -9,223,372,036,854,775,807
print(int64_limit(unsigned=True) # if negative_value is True, 0

# Output: 9,223,372,036,854,775,807
# Output: 18,446,744,073,709,551,615
```

```pi(decimal=None)```

```python
from scimatic.utils.convenient_utils import pi

print(pi())
print(pi(2))

# Output: 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
# Output: 3.14
```

### databasing.py(new addition)
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

# Output: ID: 2				Date stored: mm/dd/yyyy				Function: mul				Return Value: 4				Version: 1.4.0
# Output: ID: 1				Date stored: mm/dd/yyyy				Function: add				Return Value: 13				Version: 1.4.0
```
- If the id parameter is None it gets the most recently added value

```db.get_all(print_result=False)```
```python
from scimatic.utils.databasing import Database

db = Database()

db.get_all(print_result=True)

# Output: ID: 1				Date stored: mm/dd/yyyy				Function: add 			Return Value: 13				Version: 1.4.0
# 							 ID: 2				Date stored: mm/dd/yyyy				Function: mul				Return Value: 4				Version: 1.4.0
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
