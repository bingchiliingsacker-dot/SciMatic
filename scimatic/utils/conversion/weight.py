METRIC_WEIGHTS = {
	'qg': 1e-30,
	'rg': 1e-27,
	'yg': 1e-24,
	'zg': 1e-21,
	'ag': 1e-18,
	'fg': 1e-15,
	'pg': 1e-12,
	'ng': 1e-9,
	'µg': 1e-6,
	'ug': 1e-6,
	'mg': 1e-3,
	'cg': 1e-2,
	'dg': 1e-1,
	'g': 1,
	'dag': 1e1,
	'hg': 1e2,
	'kg': 1e3,
	'Mg': 1e6,
	'Gg': 1e9,
	'Tg': 1e12,
	'Pg': 1e15,
	'Eg': 1e18,
	'Zg': 1e21,
	'Yg': 1e24,
	'Rg': 1e27,
	'Qg': 1e30
}

IMPERIAL_WEIGHTS = {
	'gr': 0.06479891,
	'dr': 1.7718451953125,
	'oz': 28.349523125,
	'lb': 453.59237,
	'st': 6_350.29318,
	'qr': 12_700.58636,
	'cwt': 50_802.34544,
	'ton': 1_016_046.9088
}

WEIGHTS = {
	**METRIC_WEIGHTS,
	**IMPERIAL_WEIGHTS
}

def convert_weight(
	w: float,
	w_sym1: str,
	w_sym2: str,
	print_result: bool = False
	) -> float:
	
	if w_sym1 not in WEIGHTS:
		raise KeyError('Parameter w_sym1 is not a valid weight symbol.')
	elif w_sym2 not in WEIGHTS:
		raise KeyError('Parameter w_sym2 is not a valid weight symbol.')
	
	value = w * WEIGHTS[w_sym1]
	output = value / WEIGHTS[w_sym2]

	if print_result:
		print(f'{w}{w_sym1} -> {output}{w_sym2}')
	return output