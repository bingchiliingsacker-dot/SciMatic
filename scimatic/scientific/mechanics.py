def momentum(
	mass: int | float,
	velocity: int | float,
	print_result: bool = False
) -> int | float | None:
	
	p = mass * velocity
	
	if print_result:
		print(f'Momentum: {p}kg•m/s')
	return p
	
def impulse(
	force: int | float,
	initial_time: int | float,
	final_time: int | float,
	print_result: bool = False,
	return_deltat: bool = False
) -> int | float | None:
	
	if initial_time >= final_time:
		raise ValueError
	
	delta_t = final_time - initial_time
	
	J = force * delta_t
	
	delta = '\u0394'
	
	if print_result:
		if not return_deltat:
			print(f'Impulse: {J}N•s')
		else:
			print(f'Impulse: {J}N•s, {delta}t: {delta_t}s')
			
	if return_deltat:
		return J, delta_t
	else:
		return J
