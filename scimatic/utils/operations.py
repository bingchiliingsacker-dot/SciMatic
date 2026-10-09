def diff(*args, print_result: bool = False):
    output = 0

    for i, a in enumerate(args):
        if i == 0:
            output = a
            continue
        output -= a

    if print_result:
        print(output)
    return output

def prod(*args, print_result: bool = False):
    output = 0

    for i, a in enumerate(args):
        if i == 0:
            output = a
            continue
        output *= a

    if print_result:
        print(output)
    return output

def truediv(*args, print_result: bool = False):
    output = 0
    for i, a in enumerate(args):
        if i == 0:
            output = a
            continue
        output /= a

    if print_result:
        print(output)
    return output

def floordiv(*args, print_result: bool = False):
    output = 0
    for i, a in enumerate(args):
        if i == 0:
            output = a
            continue
        output /= a

    if print_result:
        print(output)
    return output

def modulo(*args, print_result: bool = False):
    output = 0
    for i, a in enumerate(args):
        if i == 0:
            output = a
            continue
        output %= a

    if print_result:
        print(output)
    return output

