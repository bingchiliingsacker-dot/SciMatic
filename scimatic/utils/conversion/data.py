BITS = {
	'b': 1,
    'kb': 10**3,
	'Mb': 10**6,
	'Gb': 10**9,
	'Tb': 10**12,
	'Pb': 10**15,
	'Eb': 10**18,
	'Zb': 10**21,
	'Yb': 10**24,
	'Rb': 10**27,
	'Qb': 10**30
}

BYTES = {
	'B': 8,
    'kB': 8 * 10**3,
	'MB': 8 * 10**6,
	'GB': 8 * 10**9,
	'TB': 8 * 10**12,
	'PB': 8 * 10**15,
	'EB': 8 * 10**18,
	'ZB': 8 * 10**21,
	'YB': 8 * 10**24,
	'RB': 8 * 10**27,
	'QB': 8 * 10**30
}

BINARY_BYTES = {
	'B': 8,
    'kiB': 8 * 2**10,
	'MiB': 8 * 2**20,
	'GiB': 8 * 2**30,
	'TiB': 8 * 2**40,
	'PiB': 8 * 2**50,
	'EiB': 8 * 2**60,
	'ZiB': 8 * 2**70,
	'YiB': 8 * 2**80,
	'RiB': 8 * 2**90,
	'QiB': 8 * 2**100
}

COMPUTER_BITS = {
	**BITS,
	**BYTES,
	**BINARY_BYTES
}

def convert_bits(
	b: int,
	b_sym1,
	b_sym2,
	print_result=False
	) -> float:
	
	if b_sym1 not in COMPUTER_BITS:
		raise KeyError('Parameter b_sym1 is not a valid data symbol.')
	elif b_sym2 not in COMPUTER_BITS:
		raise KeyError('Parameter b_sym2 is not a valid data symbol.')
	
	output = b * COMPUTER_BITS[b_sym1] / COMPUTER_BITS[b_sym2]
	
	if print_result:
		print(f'{b}{b_sym1} -> {output}{b_sym2}')
	return output