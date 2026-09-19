from scimatic.c_engineering.logic_gates import XOR, AND, OR

def half_adder(
	a: bool | int,
	b: bool | int,
	binary: bool = False,
	print_result: bool = False
) -> tuple[bool | int, bool | int]:
	SUM = XOR(a, b, binary=binary)
	COUT = AND(a, b, binary=binary)
	
	if print_result:
		print(f'SUM: {SUM}')
		print(f'COUT: {COUT}')
	return SUM, COUT

def full_adder(
	x: bool | int,
	y: bool | int,
	z: bool | int,
	binary: bool = False,
	print_result: bool = False
) -> tuple[bool | int, bool | int]:
	
	#First step produces 4 variables a, b, c, d
	a = XOR(y, z, binary=binary)
	b = AND(y, z, binary=binary)
	c = AND(y, x, binary=binary)
	d = AND(z, x, binary=binary)
	
	#Second step produces SUM and e
	SUM = XOR(a, x, binary = binary)
	e = OR(b, c, binary=binary)
	
	#Third step produces the carry-out(COUT)
	COUT = OR(d, e, binary=binary)
	
	if print_result:
		print(f'SUM: {SUM}')
		print(f'COUT: {COUT}')
	return SUM, COUT