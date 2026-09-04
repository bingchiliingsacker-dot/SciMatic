import math
from .errors import CaseError, TrigonometryError


def sin_law(
	case: str,
	a: int | float,
	b: int | float,
	c: int | float,
	print_result: bool = False
) -> int | float | list[dict[str, int | float]] | None:
	
	cases = ['SAA', 'AAS', 'ASA', 'SSA']
	
	if case not in cases:
		raise CaseError(f'Parameter \'case\' must be: {cases}.')
		
	known_items = [a, b, c]
	
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
			print(f'Angle B: {B}, Side C: {sidec}, Side B: {sideb}')
		return B, sidec, sideb
		
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
		
		if print_result:
			print(output1)
			print(output2)
		return output1, output2
		

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
