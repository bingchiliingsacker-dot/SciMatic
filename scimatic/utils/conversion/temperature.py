def convert_temp(
	t: float, te_sym1: str,
	te_sym2: str,
	print_result: bool = False
	) -> float:
	
	te_sym1 = te_sym1.lower()
	te_sym2 = te_sym2.lower()
	
	if te_sym1 not in ['c', 'f', 'k', 'r', 're']:
		raise KeyError('Parameter te_sym1 is not a valid temperature symbol.')
	elif te_sym2 not in ['c', 'f', 'k', 'r', 're']:
		raise KeyError('Parameter te_sym2 is not a valid temperature symbol.')
		
	if te_sym1 == 'c':
		if te_sym2 == 'c':
			result = t
		elif te_sym2 == 'f':
			result = t * 9/5 + 32
		elif te_sym2 == 'k':
			result = t + 273.15
		elif te_sym2 == 'r':
			result = t * 9/5 + 491.67
		else:
			result = t * 4/5
	elif te_sym1 == 'f':
		if te_sym2 == 'f':
			result = t
		elif te_sym2 == 'c':
			result = (t - 32) * 5/9
		elif te_sym2 == 'k':
			result = (t - 32) * 5/9 + 273.15
		elif te_sym2 == 'r':
			result = t + 459.67
		else:
			result = (t - 32) * 4/9
	elif te_sym1 == 'k':
		if te_sym2 == 'k':
			result = t
		elif te_sym2 == 'c':
			result = t - 273.15
		elif te_sym2 == 'f':
			result = (t - 273.15) * 9/5 + 32
		elif te_sym2 == 'r':
			result = t * 9/5
		else:
			result = (t - 273.15) * 4/5
	elif te_sym1 == 'r':
		if te_sym2 == 'r':
			result = t
		elif te_sym2 == 'c':
			result = (t - 491.67) * 5/9
		elif te_sym2 == 'f':
			result = t - 459.67
		elif te_sym2 == 'k':
			result = t * 5/9
		else:
			result = (t - 491.67) * 4/9
	else:
		if te_sym2 == 're':
			result = t
		elif te_sym2 == 'c':
			result = t * 5/4
		elif te_sym2 == 'f':
			result = t * 9/4 + 32
		elif te_sym2 == 'k':
			result = t * 5/4 + 273.15
		else:
			result = t * 9/4 + 491.67
	
	if print_result:
		print(f'{t}{te_sym1} -> {result}{te_sym2}')
	return result