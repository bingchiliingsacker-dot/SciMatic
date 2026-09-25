import math
from .errors import CaseError, TrigonometryError
from ..utils.convenient_utils import pi
from decimal import Decimal

# Circle/spherical logic
def area_circle(
	r: Decimal,
	print_result: bool = False
) -> Decimal:
	
	output = pi() * r**2
	
	if print_result:
		print(output)
	return output

def circumference_circle(
	r: Decimal,
	print_result: bool = False
) -> Decimal:
	
	output = 2 * pi() * r
	
	if print_result:
		print(output)
	return output
	
def volume_circular(
	shape: str,  # Supports a cylinder, cone, sphere, and hemisphere
	*args: Decimal,
	print_result: bool = False
) -> Decimal:
	
	shapes = ['cylinder', 'cone', 'sphere', 'hemisphere']
    
	shape = shape.lower()
	
	if shape not in shapes:
		raise ValueError(f"Shapes must be {','.join(shapes)}.")
	
	else:
		if shape == shapes[0]:
			if len(args) != 2:
				raise ValueError(f'Cylinder needs 2 arguments, {len(args)} were given.')
			
			output = pi() * args[0]**2 * args[1]
			
		elif shape == shapes[1]:
			if len(args) != 2:
				raise ValueError(f'Cone needs 2 arguments, {len(args)} were given.')
			
			output = Decimal('1') / Decimal('3') * pi() * args[0]**2 * args[1]

		elif shape == shapes[2]:
			if len(args) != 1:
				raise ValueError(f'Sphere needs 1 argument, {len(args)} were given.')
			
			output = Decimal('4') / Decimal('3') * pi() * args[0]**3
		
		else:
			if len(args) != 1:
				raise ValueError(f'Hemisphere needs 1 argument, {len(args)} were given.')
			
			output = Decimal('2') / Decimal('3') * pi() * args[0]**3
	
	if print_result:
		print(output)
	return output				

# Triangle/Triangular logic
def perimeter_triangle(
	a: Decimal,
	b: Decimal,
	c: Decimal,
	print_result: bool = False
) -> Decimal:
	
	output = a + b + c
	
	if print_result:
		print(output)
	return output

def area_triangle(
	b: Decimal,
	h: Decimal,
	print_result: bool = False
) -> Decimal:
	
	output = Decimal('0.5') * b * h
	
	if print_result:
		print(output)
	return output
	
# Parallelogram logic
def perimeter_parallelogram(a: Decimal, b: Decimal, print_result: bool = False) -> Decimal:
	output = Decimal('2') * (a + b)
	
	if print_result:
		print(output)
	return output

def area_parallelogram(b: Decimal, h: Decimal, print_result: bool = False) -> Decimal:
	output = b * h
	
	if print_result:
		print(output)
	return output

# Trapezoin logic

def perimeter_trapezoid(a: Decimal, b: Decimal, c: Decimal, d: Decimal, print_result: bool = False) -> Decimal:
	output = a + b + c + d
	
	if print_result:
		print(output)
	return output

def area_trapezoid(a: Decimal, b: Decimal, h: Decimal, print_result: bool = False) -> Decimal:
	output = Decimal('1') / Decimal('2') * (a + b) * h
	
	if print_result:
		print(output)
	return output

# Square/quadrilateral logic

def perimeter_square(s: Decimal, print_result: bool = False) -> Decimal:
	output = Decimal('4') * s
	
	if print_result:
		print(output)
	return output

def area_square(s: Decimal, print_result: bool = False) -> Decimal:
	output = s**Decimal('2')
	
	if print_result:
		print(output)
	return output

# Rectangle logic

def perimeter_rect(l: Decimal, w: Decimal, print_result: bool = False) -> Decimal:
	output = Decimal('2') * (l + w)
	
	if print_result:
		print(output)
	return output

def area_rect(l: Decimal, w: Decimal, print_result: bool = False) -> Decimal:
	output = l * w
	
	if print_result:
		print(output)
	return output

# Polygon logic

def perimeter_polygon(n: Decimal, s: Decimal, print_result: bool = False) -> Decimal:
	output = n * s
	
	if print_result:
		print(output)
	return output

def area_polygon(P: Decimal, a: Decimal, print_result: bool = False) -> Decimal:
	output = Decimal('1') / Decimal('2') * P * a
	
	if print_result:
		print(output)
	return output

# Volume logic
def volume_cube(a: Decimal, print_result: bool = False) -> Decimal:
	output = a**Decimal('3')
	
	if print_result:
		print(output)
	return output

def volume_cuboid(l: Decimal, w: Decimal, h: Decimal, print_result: bool = False) -> Decimal:
	output = l * w * h
	
	if print_result:
		print(output)
	return output

def volume_prism(A: Decimal, h: Decimal, print_result: bool = False) -> Decimal:
	output = A * h
	
	if print_result:
		print(output)
	return output

def volume_pyramid(A: Decimal, h: Decimal, print_result: bool = False) -> Decimal:
	output = Decimal('1') / Decimal('3') * 	  A * h
	
	if print_result:
		print(output)
	return output



def sin_law(
	case: str,
	a: int | float,
	b: int | float,
	c: int | float,
	print_result: bool = False
) -> tuple[float, float, float] | list[dict[str, float]] | None:
	
	cases = ['SAA', 'AAS', 'ASA', 'SSA']
	
	if case not in cases:
		raise CaseError(f'Parameter \'case\' must be: {cases}.')
		
	known_items = [a, b, c]
	
	if any(var <= 0 for var in known_items):
		raise ValueError('Triangle values must be positive.')
	
	for var in known_items:
		if not isinstance(var, (int, float)):
			raise ValueError('Invalid variables.')
	
	if case == cases[1]:
		a, c = c, a
		case = cases[0]
	
	if case == cases[0]:
		B = 180 - (b + c)
		
		A = c
		C = b
		
		sidec = (a * math.sin(math.radians(C))) / (math.sin(math.radians(A)))
		
		sideb = (a * math.sin(math.radians(B))) / (math.sin(math.radians(A)))
		
		if print_result:
			print(f'Angle B: {B}, Side C: {sidec}, Side B: {sideb}')
		return B, sidec, sideb
	
	elif case == cases[2]:
		A = 180 - (a + c)
		
		B = c
		C = a
		
		sidec = (b * math.sin(math.radians(C))) / (math.sin(math.radians(A)))
		
		sideb = (b * math.sin(math.radians(B))) / (math.sin(math.radians(A)))
		
		if print_result:
			print(f'Angle A: {A}, Side C: {sidec}, Side B: {sideb}')
		return A, sidec, sideb
		
	else:
		A = c
		
		try:
			B1 = math.degrees(math.asin((b * math.sin(math.radians(A))) / a))
		except ValueError:
			if print_result:
				print('No real triangle is formed...')
			else:
				raise TrigonometryError
			return
		
		B2 = 180 - B1
		
		valid_case = [False, False]
		
		if A + B1 < 180:
			valid_case[0] = True
		
		if A + B2 < 180:
			valid_case[1] = True
			
		output1 = []
		output2 = []
		
		for i, triangle in enumerate(valid_case):
			if not triangle:
				continue
			
			B = B1 if i == 0 else B2
			
			C = 180 - (A + B)
			
			sideb = (a * math.sin(math.radians(B))) / (math.sin(math.radians(A)))
			
			if i == 0:
				output1.append({
				'angle B': B1, 
				'angle C': C, 
				'side b': sideb
				})
			else:
				output2.append({
				'angle B': B2, 
				'angle C': C, 
				'side b': sideb
				})
		
		outputs = []
		
		outputs.extend(output1)
		outputs.extend(output2)
		
		if print_result:
			print(outputs)
		return outputs
		

def cos_law(
	case: str,
	a: int | float,
	b: int | float,
	c: int | float,
	print_result: bool = False
) -> int | float | None:
	
	cases = ['SSS', 'SAS']
	
	if case not in cases:
		raise CaseError(f'Parameter \'case\' must be: {cases}.')
		
	known_items = [a, b, c]
	
	if any(var <= 0 for var in known_items):
		raise ValueError('Triangle values must be positive.')
	
	for var in known_items:
		if not isinstance(var, (int, float)):
			raise ValueError('Invalid variables.')

	if case == cases[0]:
		if a + b <= c or a + c <= b or b + c <= a:
			if print_result:
				print('No such valid triangle...')
			else:
				raise TrigonometryError
			return
		A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
		B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
		
		C = 180 - (A + B)
		
		if print_result:
			print(f'Angle A: {A}, Angle B: {B}, Angle C: {C}')
		return A, B, C
	
	else:
		C = b
		sidec = math.sqrt(a**2 + c**2 - 2 * a * c * math.cos(math.radians(C)))
		
		acos_arg = (c**2 + sidec**2 - a**2) / (2 * c * sidec)
		acos_arg = max(-1.0, min(1.0, acos_arg))
		A = math.degrees(math.acos(acos_arg))
		
		B = 180 - (A + C)
		
		if print_result:
			print(f'Side c: {sidec}, Angle A: {A}, Angle B: {B}')
		return sidec, A, B
		
		acos_arg = (c**2 + sidec**2 - a**2) / (2 * c * sidec)
		acos_arg = max(-1.0, min(1.0, acos_arg))
		A = math.degrees(math.acos(acos_arg))
		
		B = 180 - (A + C)
		
		if print_result:
			print(f'Side c: {sidec}, Angle A: {A}, Angle B: {B}')
		return sidec, A, B
