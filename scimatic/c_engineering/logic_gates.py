def AND(
	bool1: bool | int,
	bool2: bool | int,
	binary: bool = False
) -> bool | int:
	
	result = bool(bool1) and bool(bool2)
	
	return int(result) if binary else result

def NOT(
	bool1: bool | int,
	binary: bool = False
) -> bool | int:
	
	result = not bool(bool1)
	
	return int(result) if binary else result

def NAND(
	bool1: bool | int,
	bool2: bool | int,
	binary: bool = False
) -> bool | int:
	
	result = NOT(AND(bool1, bool2))
	
	return int(result) if binary else result

def OR(
	bool1: bool | int,
	bool2: bool | int,
	binary: bool = False
) -> bool | int:
	
	result = bool(bool1) or bool(bool2)
	
	return int(result) if binary else result

def XOR(
	bool1: bool | int,
	bool2: bool | int,
	binary: bool = False
) -> bool | int:
	
	result = bool(bool1) != bool(bool2)
	
	return int(result) if binary else result
	
def NOR(
	bool1: bool | int,
	bool2: bool | int,
	binary: bool = False
) -> bool | int:
	
	result = NOT(OR(bool1, bool2))
	
	return int(result) if binary else result

def XNOR(
	bool1: bool | int,
	bool2: bool | int,
	binary: bool = False
) -> bool | int:
	
	result = bool(bool1) == bool(bool2)

	return int(result) if binary else result