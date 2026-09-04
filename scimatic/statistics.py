import math
from .errors import NegativeDiscriminantError, VariableError, ConstantError, ComparisonError, DataError
	
def quartile(
	raw_data: list[int],
	k: int,
	print_result: bool = False
) -> int:
	
	constant_check = [1, 2, 3]
	
	if k not in constant_check:
		raise ConstantError
	
	if len(raw_data) <= 1:
		raise DataError('Raw data is too short.')
		
	processed_data = sorted(raw_data)
	n = len(processed_data)
	
	position = k * (n + 1) / 4
	
	if print_result:
		print(position)
	
	if position.isinteger():
		formula = processed_data[int(position) - 1]
	else:
		position1 = int(position)
		position2 = position1 + 1
		fraction = position - position1

		lower_value = processed_data[position1 - 1]
		higher_value = processed_data[position2 - 1]

		formula = lower_value + fraction * (higher_value - lower_value)
	
	if print_result:
		print(f'Q{k} = {k}({n} + 1) / 4')
		print(formula)
	return formula
	
def decile(
	raw_data: list[int],
	k: int,
	print_result: bool = False
) -> int | None:
	
	constant_check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	
	if k not in constant_check:
		raise ConstantError

	if len(raw_data) < 10:
		raise DataError('Raw data is too short.')
		
	
	processed_data = sorted(raw_data)
	
	n = len(processed_data)
	
	position = k * (n + 1) / 10
	
	if print_result:
		print(position)
	
	if position.isinteger():
		formula = processed_data[int(position) - 1]
	else:
		position1 = int(position)
		position2 = position1 + 1
		fraction = position - position1

		lower_value = processed_data[position1 - 1]
		higher_value = processed_data[position2 - 1]

		formula = lower_value + fraction * (higher_value - lower_value)
	
	if print_result:
		print(f'D{k} = {k}({n} + 1) / 10')
		print(formula)
	return formula
	
def percentile(
	raw_data: list[int],
	k: int,
	print_result: bool = False
) -> int | None:
	
	constant_check = []
	
	for i in range(100):
		if i == 0:
			continue
		
		constant_check.append(i)
	

	
	if k not in constant_check:
		raise ConstantError

	if len(raw_data) < 10:
		raise DataError('Raw data is too short.')
	
	processed_data = sorted(raw_data)
	
	if print_result:
		print(processed_data)
		
	n = len(processed_data)

	position = k * (n + 1) / 100
	
	if print_result:
		print(position)
	
	if position.isinteger():
		formula = processed_data[int(position) - 1]
	else:
		position1 = int(position)
		position2 = position1 + 1
		fraction = position - position1

		lower_value = processed_data[position1 - 1]
		higher_value = processed_data[position2 - 1]

		formula = lower_value + fraction * (higher_value - lower_value)
		
	if print_result:
		print(f'P{k} = {k}({n} + 1) / 100')
		print(formula)
	return formula
	
def median(
	raw_data: list[int],
	print_result: bool = False
) -> int | None:
	
	processed_data = sorted(raw_data)
	
	if len(raw_data) <= 1:
		raise DataError('Raw data is too short.')
	
	n = len(processed_data)
	
	position = (n + 1) / 2
	
	syntax_list = []
	
	num = ''
	
	position = str(position)
	
	is_float = False
	
	for p in position:
		if p == '.':
			is_float = True
			syntax_list.append(num)
			continue
		
		num += p
	
	syntax_list.append(num)

	position = float(position)

	if position.is_integer():
		formula = processed_data[int(position) - 1]
	
	else:
		position1 = int(position)
		position2 = position1 + 1
	
		lower_value = processed_data[position1 - 1]
		higher_value = processed_data[position2 - 1]
	
		fraction = position - position1
	
		formula = lower_value + fraction * (higher_value - lower_value)
	
	if print_result:
		print(processed_data)
		print('Position:', position)
		print('Median', formula)
	return position, formula
