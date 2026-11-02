
import math
import operator

from .errors import NegativeDiscriminantError, ComparisonError
from ..utils.convenient_utils import Operator


operators = {
    '>': operator.gt,
    '<': operator.lt,
    '>=': operator.ge,
    '<=': operator.le
}


def quadratic_equation(
    a: int | float,
    b: int | float,
    c: int | float,
    x: int | float,
    print_result: bool = False
) -> int | float:

    result = a * x**2 + b * x + c

    if print_result:
        print(result)

    return result


def quadratic_formula(
    a: int | float,
    b: int | float,
    c: int | float,
    print_result: bool = False,
    vietas_formula: bool = False
) -> tuple[float, float] | tuple[float, float, float, float]:

    if a == 0:
        print('💥 SciMatic failed [E0102].')
        print('☝️ Reason: Quadratic equations require a nonzero value for a. Otherwise, the equation is no longer quadratic.')
        print('💡 Tip: Make sure parameter a is not equal to 0.')
        print('🔗 Link: https://github.com/bingchiliingsacker-dot/SciMatic_Errors/blob/main/errors/Math-Errors%5BE0101-E0200%5D/%5BE0102%5D.md')

        raise ZeroDivisionError(
            'Attempted to divide by zero. Refer to the message above for more information.'
        )

    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        print('💥 SciMatic failed [E0101].')
        print(f'☝️ Reason: The discriminant is negative ({discriminant}), meaning the equation has no real-number solutions.')
        print('💡 Tip: Consider changing the values of a, b, and c so that the discriminant is greater than or equal to 0.')
        print('🔗 Link: https://github.com/bingchiliingsacker-dot/SciMatic_Errors/blob/main/errors/Math-Errors%5BE0101-E0200%5D/%5BE0101%5D.md')

        raise NegativeDiscriminantError(
            'The given coefficients do not produce real roots. Refer to the message above for more information.'
        )

    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)

    if print_result:
        print(f'x = {x1}, x = {x2}')

    if vietas_formula:
        root_sum = x1 + x2
        root_product = x1 * x2

        if print_result:
            print(f'x1 + x2 = {root_sum}')
            print(f'x1 * x2 = {root_product}')

        return x1, x2, root_sum, root_product

    return x1, x2


def quadratic_inequality(
    a: int | float,
    b: int | float,
    c: int | float,
    symbol: Operator,
    print_result: bool = False
) -> tuple[str, float | None, float | None]:

    symbol_list = ['>', '<', '>=', '<=']

    if symbol not in symbol_list:
        print('💥 SciMatic failed [E0602].')
        print('☝️ Reason: The symbol parameter contains an invalid comparison operator.')
        print(f'💡 Tip: Make sure the symbol is one of the following: {symbol_list}.')
        print('🔗 Link: https://github.com/bingchiliingsacker-dot/SciMatic_Errors/blob/main/errors/User-Errors%5BE0601-E0800%5D/%5BE0602%5D.md')

        raise ComparisonError(
            'The symbol parameter contains an invalid comparison operator. Refer to the message above for more information.'
        )

    if a == 0:
        print('💥 SciMatic failed [E0102].')
        print('☝️ Reason: Quadratic equations require a nonzero value for a. Otherwise, the equation is no longer quadratic.')
        print('💡 Tip: Make sure parameter a is not equal to 0.')
        print('🔗 Link: https://github.com/bingchiliingsacker-dot/SciMatic_Errors/blob/main/errors/Math-Errors%5BE0101-E0200%5D/%5BE0102%5D.md')

        raise ZeroDivisionError(
            'Attempted to divide by zero. Refer to the message above for more information.'
        )

    discriminant = b**2 - 4 * a * c

    # Handles negative discriminants
    if discriminant < 0:
        # The polynomial always has the same sign as a.
        if operators[symbol](a, 0):
            solutions = 'All real numbers are solutions...'
        else:
            solutions = 'No real solutions...'

        if print_result:
            print(solutions)

        return solutions, None, None

    # Handles repeated roots
    elif discriminant == 0:
        root = -b / (2 * a)

        if a > 0:
            if symbol == '>':
                solutions = f'x != {root}'
            elif symbol == '>=':
                solutions = 'All real numbers are solutions...'
            elif symbol == '<':
                solutions = 'No real solutions...'
            else:
                solutions = f'x = {root}'

        else:
            if symbol == '>':
                solutions = 'No real solutions...'
            elif symbol == '>=':
                solutions = f'x = {root}'
            elif symbol == '<':
                solutions = f'x != {root}'
            else:
                solutions = 'All real numbers are solutions...'

        if print_result:
            print(solutions)

        return solutions, root, root

    # Handles two distinct real roots
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)

        x1, x2 = sorted([x1, x2])

        testpoint1 = x1 - 1
        testpoint2 = (x1 + x2) / 2
        testpoint3 = x2 + 1

        test_points = [testpoint1, testpoint2, testpoint3]

        truth_table = [
            operators[symbol](a * point**2 + b * point + c, 0)
            for point in test_points
        ]

        false_count = truth_table.count(False)

        # Handles [True, False, True]
        if false_count == 1:
            if symbol in ['>', '<']:
                solutions = f'x < {x1} or x > {x2}'
            else:
                solutions = f'x <= {x1} or x >= {x2}'

        # Handles [False, True, False]
        elif false_count == 2:
            if symbol in ['>', '<']:
                solutions = f'{x1} < x < {x2}'
            else:
                solutions = f'{x1} <= x <= {x2}'

        # Handles [False, False, False]
        elif false_count == 3:
            solutions = 'No real solutions...'

        # Handles [True, True, True]
        else:
            solutions = 'All real numbers are solutions...'

        if print_result:
            print(solutions)

        return solutions, x1, x2


def pythagorean_theorem(
    a: int | float,
    b: int | float,
    c: int | float | None = None,
    print_result: bool = True
) -> tuple[bool, float] | float:

    c_squared = a**2 + b**2

    if c is not None:
        output = math.isclose(
            c**2,
            c_squared,
            rel_tol=1e-9,
            abs_tol=1e-9
        )

        if print_result:
            print(f'{c}^2 = {a}^2 + {b}^2')
            print(output)

        return output, c_squared

    hypotenuse = math.sqrt(c_squared)

    if print_result:
        print(f'sqrt({a}^2 + {b}^2) = {hypotenuse}')

    return hypotenuse
