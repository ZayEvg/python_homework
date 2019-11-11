"""
Обисилити F(x) = -3x+9 при х<=7, або F(x) = 1/(x-7) при х>7
"""
import re

re_float = re.compile("^[-+]{0,1}\d+\.{0,1}\d*$")


def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text


def variable_x(prompt):
    number = float(validator(re_float, prompt))
    return number


def function_count(count_x):
    if count_x <= 7:
        result = "F(X) = -3X + 9 = " + str(-3*count_x + 9)
        return result
    else:
        result = "F(X) = 1/(X - 7) = " + str(1/(count_x - 7))
        return result

print("F(x) = -3x+9, х<=7; F(x) = 1/(x-7), х>7")
x = variable_x('Enter count X: ')

print(function_count(x))