TIME = {
	'us': 1e-6,
	'µs': 1e-6,
	'ms': 1e-3,
	's': 1,
	'min': 60,
	'h': 3_600,
	'd': 86_400,
	'w': 604_800,
	'mon': 2_629_800,
	'y': 31_557_600,
	'dec': 315_576_000,
	'cen': 3_155_760_000,
    'mil': 31_557_600_000
}

def convert_time(
	n: float,
	t_sym1: str,
	t_sym2: str,
	print_result: bool = False
	) -> float:
	
	if t_sym1 not in TIME:
		raise KeyError('Parameter t_sym1 is not a valid time symbol.')
	elif t_sym2 not in TIME:
		raise KeyError('Parameter t_sym2 is not a valid time symbol.')
		
	value = n * TIME[t_sym1]
	output = value / TIME[t_sym2]
		
	if print_result:
		print(f'{n}{t_sym1} -> {output}{t_sym2}')
	return output