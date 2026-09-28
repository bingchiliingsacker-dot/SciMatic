from math import isclose

def boyles_law(
    initial_pressure: int | float,
    initial_volume: int | float,
    final_pressure: int | float | None = None,
    final_volume: int | float | None = None,
    print_result: bool = False
) -> int | float:

    if final_pressure is None and final_volume is None:
        print('💥 SciMatic failed.')
        print('')
        print('☝ Reason: Boyles law requires a final pressure or a final volume given.')
        print('💡 Tip: Give a final pressure or a final volume to the formula.')
        raise ValueError('Neither a final pressure nor a final volume were given. Refer to the text above for more information.')

    if final_pressure is None:
        final_pressure = initial_pressure * initial_volume / final_volume
        if print_result:
            print(final_pressure)
        return final_pressure
    elif final_volume is None:
        final_volume = initial_pressure * initial_volume / final_pressure
        if print_result:
            print(final_volume)
        return final_volume
    else:
        if print_result:
            print(f'P₁V₁ = P₂V₂ is {isclose(initial_pressure * initial_volume, final_pressure * final_volume)}!')
        return isclose(initial_pressure * initial_volume, final_pressure * final_volume)

def ideal_gas_law(
    P: int | float | None = None,
    V: int | float | None = None,
    n: int | float | None = None,
    T: int | float | None = None,
    R: int | float | None = 8.31446261815324,
    print_result: bool = False
) -> int | float:
    nones = [P, V, T, R, n]

    iterations = 0
    for n in nones:
        if n is None:
            iterations += 1
            continue

    if iterations == 0:
        if print_result:
            print(f'PV = nTR is {isclose(P * V, n * R * T)}!')
        return isclose(P * V, n * R * T)
    elif iterations > 1:
        print('💥 SciMatic failed.')
        print('')
        print('☝ Reason: Ideal Gas law requires all values except 1 having an integer or float, you got multiple unknown values.')
        print('💡 Tip: Give only 1 unknown value.')
        raise ValueError('Multiple unknown values were given. Refer to the text above for more information.')

    if P is None:
        P = n * R * T / V
        if print_result:
            print(f'{P}Pa')
        return P
    elif V is None:
        V = n * R * T / P
        if print_result:
            print(f'{V}m^3')
        return V
    elif n is None:
        n = P * V / (R * T)
        if print_result:
            print(f'{n}g/mol')
        return n
    elif T is None:
        T = P * V / (n * R)
        if print_result:
            print(f'{T}K')
        return T
    elif R is None:
        R = P * V / (n * T)
        if print_result:
            print(f'{R}J/(mol*K)')
        return R