"""
На площині ХОY задана своїми координатами точка А (координати ввести з клавіатури). Вказати, де вона розташована (на якій осі або в якому координатном куті).
"""
import re

re_float = re.compile("^[-+]{0,1}\d+\.{0,1}\d*$")


def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text


def float_of_point_a(prompt):
    number = float(validator(re_float, prompt))
    return number


def point_location(coord_x, coord_y):
    if coord_x == 0 and coord_y == 0:
        result = "point A is on the axis OX and OY"
        return result
    elif coord_x == 0 and coord_y != 0:
        result = "point A is on the axis OY"
        return result
    elif coord_x != 0 and coord_y == 0:
        result = "point A is on the axis OX"
        return result
    elif coord_x > 0 and coord_y > 0:
        result = "point A is in the 1-st coordinate quarter"
        return result
    elif coord_x > 0 and coord_y < 0:
        result = "point A is in the 4-th coordinate quarter"
        return result
    elif coord_x < 0 and coord_y > 0:
        result = "point A is in the 2-nd coordinate quarter"
        return result
    elif coord_x < 0 and coord_y < 0:
        result = "point A is in the 3-rd coordinate quarter"
        return result


x_of_a = float_of_point_a('Enter X coordinate of point A: ')
y_of_a = float_of_point_a('Enter Y coordinate of point A: ')

print(point_location(x_of_a, y_of_a))
