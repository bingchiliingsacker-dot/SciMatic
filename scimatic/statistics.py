import math
from typing import List, Union

from .errors import ConstantError, DataError

Number = Union[int, float]


def _interpolate(sorted_data: List[Number], position: float) -> float:
    """
    Interpolate (or pick) the value at the given 1-based position in sorted_data.
    Position may be non-integer; we interpolate between floor(position) and ceil(position).
    If position <= 1 returns the first element; if position >= n returns the last element.
    """
    n = len(sorted_data)
    if n == 0:
        raise DataError("Raw data is empty.")

    # If position is at or below the first element, return first
    if position <= 1:
        return float(sorted_data[0])

    # If position is at or beyond the last element, return last
    if position >= n:
        return float(sorted_data[-1])

    if float(position).is_integer():
        return float(sorted_data[int(position) - 1])

    lower_idx = int(math.floor(position))      # 1-based index
    upper_idx = lower_idx + 1
    fraction = position - lower_idx

    lower_value = sorted_data[lower_idx - 1]
    upper_value = sorted_data[upper_idx - 1]
    return float(lower_value + fraction * (upper_value - lower_value))


def quartile(raw_data: List[Number], k: int, print_result: bool = False) -> float:
    if k not in (1, 2, 3):
        raise ConstantError

    if len(raw_data) == 0:
        raise DataError("Raw data is empty.")

    processed_data = sorted(raw_data)
    n = len(processed_data)
    position = k * (n + 1) / 4
    if print_result:
        print(position)
        print(f'Q{k} = {k}({n} + 1) / 4')

    return _interpolate(processed_data, position)


def decile(raw_data: List[Number], k: int, print_result: bool = False) -> float:
    if k not in range(1, 10):
        raise ConstantError

    if len(raw_data) == 0:
        raise DataError("Raw data is empty.")

    processed_data = sorted(raw_data)
    n = len(processed_data)
    position = k * (n + 1) / 10
    if print_result:
        print(position)
        print(f'D{k} = {k}({n} + 1) / 10')

    return _interpolate(processed_data, position)


def percentile(raw_data: List[Number], k: int, print_result: bool = False) -> float:
    if not (1 <= k <= 99):
        raise ConstantError

    if len(raw_data) == 0:
        raise DataError("Raw data is empty.")

    processed_data = sorted(raw_data)
    n = len(processed_data)
    position = k * (n + 1) / 100
    if print_result:
        print(position)
        print(f'P{k} = {k}({n} + 1) / 100')

    return _interpolate(processed_data, position)


def median(raw_data: List[Number], print_result: bool = False) -> float:
    if len(raw_data) == 0:
        raise DataError("Raw data is empty.")

    processed_data = sorted(raw_data)
    n = len(processed_data)
    position = (n + 1) / 2
    if print_result:
        print(processed_data)
        print('Position:', position)

    return _interpolate(processed_data, position)
