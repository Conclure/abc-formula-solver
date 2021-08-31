from math import sqrt
from typing import Union

def parse_number(
        n: Union[str, float, int]
):
    if isinstance(n, str):
        return float(n)
    if not (isinstance(n, int) or isinstance(n, float)):
        raise TypeError()
    return n

def parse_numbers(
        *n: Union[str, float, int]
):
    result = list()
    for i in n:
        result.append(parse_number(i))

    return result


def abc_formula(
        a: Union[str, float, int],
        b: Union[str, float, int],
        c: Union[str, float, int]
):
    a, b, c = parse_numbers(a, b, c)

    if a == 0:
        raise ArithmeticError()

    discriminant = (b ** 2) - (4 * a * c)

    if discriminant < 0:
        raise ArithmeticError()
    elif discriminant == 0:
        return (-b) / 2 * a
    else:
        solution1 = ((-b) - sqrt(discriminant)) / (2 * a)
        solution2 = ((-b) + sqrt(discriminant)) / (2 * a)

        return solution1, solution2


print(abc_formula(6.0, "-17", 12))  # x = 6x^2 - 17x + 12