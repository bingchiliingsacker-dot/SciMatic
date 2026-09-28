from ..utils.conversion.temperature import convert_temp
from math import log


def wind_chill(
    t: float,
    v: float,
    temp: str = 'f',
    print_result: bool = False
) -> float:
    formula = 35.74 + (0.6215 * t) - (35.75 * v ** 0.16) + (0.4275 * t * v ** 0.16)

    if temp not in ['c', 'f', 'k', 'r', 're']:
        print('💥 SciMatic failed.')
        print('')
        print('☝️ Reason: Temperature unit does not exist or is not supported.')
        print('💡 Tip: The supported temperatures are as follow:')
        print('Celsius(c) Fahrenheit(f) Kelvin(k)')
        print('Rankine(r) Reamur(re)')
        raise ValueError('SI unit for temperature not found. Refer to the text above for more infirmation.')
    output = convert_temp(formula, 'f', temp)

    if print_result:
        print(f'{output}{temp}')
    return output


def dew_point(
    t: float,
    rh: float,
    temp: str = 'c',
    print_result: bool = False
) -> float:
    if rh <= 0:
        print('💥 SciMatic failed.')
        print('')
        print('☝️ Reason: Relative Humidity(rh) cannot be 0 or below.')
        print('💡 Tip: You must give a non-zero argument to parameter rh.')
        raise ValueError('Relative Humidity cannot be 0. Refer to the text above for more information.')
    y = log(rh / 100) + (17.62 * t) / (243.12 + t)

    td = (243.12 * y) / (17.62 - y)

    if temp not in ['c', 'f', 'k', 'r', 're']:
        print('💥 SciMatic failed.')
        print('')
        print('☝️ Reason: Temperature unit does not exist or is not supported.')
        print('💡 Tip: The supported temperatures are as follow:')
        print('Celsius(c) Fahrenheit(f) Kelvin(k)')
        print('Rankine(r) Reamur(re)')
        raise ValueError('SI unit for temperature not found. Refer to the text above for more infirmation.')
    output = convert_temp(td, 'c', temp)

    if print_result:
        print(f'{output}{temp}')
    return output