import math
from .errors import NegativeDiscriminantError, ComparisonError, VariableError
from .convenient_utils import Operator

def quadratic_equation(
	a: int | float,
	b: int | float,
	c: int | float,
	x: int | float,
	print_result: bool = False
) -> int | float | None:
	
	result = a * x**2 + b * x + c
	
	if print_result:
		print(result)
	return result
		

def quadratic_formula(
	a: int | float,
	b: int | float,
	c: int | float,
	print_result: bool = False,
	vietas_formula: bool = False
) -> int | float | None:
	
	discriminant = b**2 - 4 * a * c
	
	if discriminant < 0:
		if print_result:
			print('No real solution...')
		else:
			raise NegativeDiscriminantError('The given integers does not produce a real solution.')
		return None
	
	x1 = (-b + math.sqrt(discriminant)) / (2 * a)
	x2 = (-b - math.sqrt(discriminant)) / (2 * a)
	
	if print_result:
		print(f'x = {x1}, x = {x2}')
		if vietas_formula:
			print(f'x1 + x2 = {x1 + x2}')
	if vietas_formula:
		return x1, x2, x1 + x2
	
	return x1, x2
	
def quadratic_inequality(
	a: int | float,
	b: int | float,
	c: int | float,
	symbol: Operator,
	print_result: bool = False
) -> int | float | None:
	symbol_list = ['>', '<', '>=', '<=']
	
	if symbol not in symbol_list:
		raise ComparisonError()
		
	if a == 0:
		raise VariableError()

	
	discriminant = b**2 - 4 * a * c
	
	if discriminant < 0:
		if print_result:
			print('No real solution...')
		else:
			raise NegativeDiscriminantError()
		return None
	
	elif discriminant == 0:
		x = (-b + math.sqrt(discriminant)) / (2 * a)
		
		if print_result:
			print('One real solution...')
			print(f'x = {x}')
		return x
		
	else:
		x1 = (-b + math.sqrt(discriminant)) / (2 * a)
		x2 = (-b - math.sqrt(discriminant)) / (2 * a)
		
		x1, x2 = sorted([x1, x2])
		
		parabola = a > 0
	
		def for_loop(x1, x2):
			testpoint1 = x1 - 1
			testpoint2 = (x1 + x2) / 2
			testpoint3 = x2 + 1
			test_points = [testpoint1, testpoint2, testpoint3]
		  
			torf = []

			for point in test_points:
				if symbol == '>':
					torf.append((a * point**2 + b * point + c) > 0)
				elif symbol == '<':
					torf.append((a * point**2 + b * point + c) < 0)
				elif symbol == '>=':
					torf.append((a * point**2 + b * point + c) >= 0)
				else:
					torf.append((a * point**2 + b * point + c) <= 0)
			
			return torf
		    
		if parabola:
			torf = for_loop(x1, x2)
			
			if symbol == '>':
				answer = f'x < {x1} or x > {x2}'
			elif symbol == '>=':
				answer = f'x <= {x1} or x >= {x2}'
			elif symbol == '<':
				answer = f'{x1} < x < {x2}'
			else:
				answer = f'{x1} <= x <= {x2}'
			
			if print_result:
				print(answer)
			return answer
			
		else:
			torf = for_loop(x1, x2)
			
			if symbol == '>':
				answer = f'{x1} < x < {x2}'
			elif symbol == '>=':
				answer = f'{x1} <= x <= {x2}'
			elif symbol == '<':
				answer = f'x < {x1} or x > {x2}'
			else:
				answer = f'x <= {x1} or x >= {x2}'
			
			if print_result:
				print(answer)
			return answer
			
def pythagorean_theorem(
	a: int | float,
	b: int | float,
	c: int | float | None = None,
	print_result: bool = True
) -> int | float | None:
	
	if c is not None:
		c_square = a**2 + b**2
		
		if c**2 == (a**2 + b**2):
			output = True
		else:
			output = False
		
		if print_result:
			print(f'{c}^2 = {a}^2 + {b}^2')
			print(output)
		return output, c_square
	
	else:
		c_square = math.sqrt(a**2 + b**2)
		if print_result:
			print(f'sqrt({a}^2 + {b}^2) = {c_square}')
		return c_square
