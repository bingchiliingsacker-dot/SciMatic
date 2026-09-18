METRIC_MEASURE = {
	'qm': 1e-30,
	'rm': 1e-27,
	'ym': 1e-24,
	'zm': 1e-21,
	'am': 1e-18,
	'fm': 1e-15,
	'pm': 1e-12,
	'nm': 1e-9,
	'µm': 1e-6,
	'um': 1e-6,
	'mm': 1e-3,
	'cm': 1e-2,
	'dm': 1e-1,
	'm': 1,
	'dam': 1e1,
	'hm': 1e2,
	'km': 1e3,
	'Mm': 1e6,
	'Gm': 1e9,
	'Tm': 1e12,
	'Pm': 1e15,
	'Em': 1e18,
	'Zm': 1e21,
	'Ym': 1e24,
	'Rm': 1e27,
	'Qm': 1e30
}

IMPERIAL_MEASURE = {
	'in': 0.0254,
	'ft': 0.3048,
	'yd': 0.9144,
	'ch': 20.1168,
	'fur': 201.168,
	'mi': 1609.344,
	'lea': 4828.032
}

METRIC_AREA = {
	'qm2': 1e-60,
	'rm2': 1e-57,
	'ym2': 1e-54,
	'zm2': 1e-51,
	'am2': 1e-48,
	'fm2': 1e-30,
	'pm2': 1e-24,
	'nm2': 1e-18,
	'µm2': 1e-12,
	'um2': 1e-12,
	'mm2': 1e-6,
	'cm2': 1e-4,
	'dm2': 1e-2,
	'm2': 1,
	'dam2': 1e2,
	'hm2': 1e4,
	'km2': 1e6,
	'Mm2': 1e12,
	'Gm2': 1e15,
	'Tm2': 1e24,
	'Pm2': 1e30,
	'Em2': 1e36,
	'Zm2': 1e42,
	'Ym2': 1e48,
	'Rm2': 1e54,
	'Qm2': 1e60,

	'hectare': 10000
}

IMPERIAL_AREA = {
	'in2': 0.00064516,
	'ft2': 0.09290304,
	'yd2': 0.83612736,
	'rd2': 25.29285264,
	'ch2': 404.68564224,
	'fur2': 40468.564224,
	'mi2': 2589988.110336,

	'acre': 4046.8564224,
	'rood': 1011.7141056,
}

LENGTH_MEASURE = {
	**METRIC_MEASURE,
	**IMPERIAL_MEASURE
}

AREA_MEASURE = {
	**METRIC_AREA,
	**IMPERIAL_MEASURE
}

def convert_len(
	n: float,
	u_sym1: str,
	u_sym2: str,
	print_result: bool = False
	) -> float:
	
	if u_sym1 not in LENGTH_MEASURE:
		raise KeyError('Parameter u_sym1 is not a valid unit symbol.')
	elif u_sym2 not in LENGTH_MEASURE:
		raise KeyError('Parameter u_sym2 is not a valid unit symbol.')
		
	value = n * LENGTH_MEASURE[u_sym1]
	output = value / LENGTH_MEASURE[u_sym2]
		
	if print_result:
		print(f'{n}{u_sym1} -> {output}{u_sym2}')
	return output
	
def convert_area(
	n: float,
	u_sym1: str,
	u_sym2: str,
	print_result: bool = False
	) -> float:
	
	if u_sym1 not in AREA_MEASURE:
		raise KeyError('Parameter u_sym1 is not a valid unit symbol.')
	elif u_sym2 not in AREA_MEASURE:
		raise KeyError('Parameter u_sym2 is not a valid unit symbol.')
		
	value = n * AREA_MEASURE[u_sym1]
	output = value / AREA_MEASURE[u_sym2]
		
	if print_result:
		print(f'{n}{u_sym1} -> {output}{u_sym2}')
	return output