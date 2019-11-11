"""
Обчислити ∑(x+i)/x^2
"""
import re

re_float = re.compile("^[-+]{0,1}\d+\.{0,1}\d*$")
re_integer = re.compile("^[-+]{0,1}\d+$")


def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text


def float_x(prompt):
    number = float(validator(re_float, prompt))
    while number == 0:
        number = float(validator(re_float, prompt))
    return number


def int_n(prompt):
    number = int(validator(re_integer, prompt))
    while number == 0:
        number = int(validator(re_integer, prompt))
    return number


def alg_sum(variable_x, upper_bound_n):
    result = 0
    for count in range(int(upper_bound_n) + 1):
        result += variable_x + count
    result = result/variable_x**2
    return result


x = float_x('Enter variable X that !=0: ')
n = int_n('Enter N - upper bound of an algebraic sum, that > 0: ')

print("∑(x+i)/x^2 = " + str(alg_sum(x, n)))