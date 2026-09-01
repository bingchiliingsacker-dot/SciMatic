def fibonacci(
	value: int,
):
	a, b = 0, 1

	i = 0
	
	while i <= value:
		yield a
		a, b = b, a + b
		i += 1

def collatz(
	value: int,
	print_result: bool = False
) -> list[int]:
	
	sequence = [value]
	
	for var in sequence:
		if var % 2 == 0:
			new_value = var // 2
		else:
			new_value = (3 * var) + 1
		
		sequence.append(new_value)
		
		if new_value == 1:
			break
	
	if print_result:
		print(sequence)
	return sequence

def ackermann(
	array: list,
	m: int,
	n: int
):
	if m > 3:
		print('The value of m is too high for python. If you want to have a niche that does not grow that quickly, I will recommend TREE.')
		return
	array.append((m, n))

	if m == 0:
		return n + 1
	elif n == 0:
		return ackermann(array, m - 1, 1)
	else:
		return ackermann(array, m - 1, ackermann(array, m, n - 1))
