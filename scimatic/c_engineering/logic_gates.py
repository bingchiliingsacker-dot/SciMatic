def AND(
        bool1: bool | int,
        bool2: bool | int,
        binary: bool = False,
        print_result: bool = False
) -> bool | int:

    result = bool(bool1) and bool(bool2)

    output = int(result) if binary else result

    if print_result:
        print(output)

    return output


def NOT(
        bool1: bool | int,
        binary: bool = False,
        print_result: bool = False
) -> bool | int:

    result = not bool(bool1)

    output = int(result) if binary else result

    if print_result:
        print(output)

    return output


def NAND(
        bool1: bool | int,
        bool2: bool | int,
        binary: bool = False,
        print_result: bool = False
) -> bool | int:

    result = NOT(AND(bool1, bool2))

    output = int(result) if binary else result

    if print_result:
        print(output)

    return output


def OR(
        bool1: bool | int,
        bool2: bool | int,
        binary: bool = False,
        print_result: bool = False
) -> bool | int:

    result = bool(bool1) or bool(bool2)

    output = int(result) if binary else result

    if print_result:
        print(output)

    return output


def XOR(
        bool1: bool | int,
        bool2: bool | int,
        binary: bool = False,
        print_result: bool = False
) -> bool | int:

    result = bool(bool1) != bool(bool2)

    output = int(result) if binary else result

    if print_result:
        print(output)

    return output


def NOR(
        bool1: bool | int,
        bool2: bool | int,
        binary: bool = False,
        print_result: bool = False
) -> bool | int:

    result = NOT(OR(bool1, bool2))

    output = int(result) if binary else result

    if print_result:
        print(output)

    return output


def XNOR(
        bool1: bool | int,
        bool2: bool | int,
        binary: bool = False,
        print_result: bool = False
) -> bool | int:

    result = bool(bool1) == bool(bool2)

    output = int(result) if binary else result

    if print_result:
        print(output)

    return output