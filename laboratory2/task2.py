"""
Необхідно підсумувати всі непарні цілі числа в діапазоні, який введе користувач з клавіатури.
"""
import re

re_integer = re.compile("^[-+]{0,1}\d+$")


def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text


def limits(prompt):
    number = int(validator(re_integer, prompt))
    return number


def counting_unpaired_numbers(first_limit, second_limit):
    while first_limit == second_limit or first_limit > second_limit:
        if first_limit == second_limit:
            print("Limits can't be equal")
            first_limit = int(input("Enter the bottom of the range: "))
            second_limit = int(input("Enter the upper limit of the range: "))
        else:
            print("Bottom limit must be lower than upper limit")
            print("The bottom of the range is: " + str(first_limit))
            second_limit = int(input("Enter the upper limit of the range: "))
    if first_limit % 2 == 0:
        changed_first_limit = int(first_limit + 1)
        if second_limit % 2 == 0:
            changed_second_limit = int(second_limit - 1)
            result = changed_first_limit
            while changed_first_limit != changed_second_limit:
                changed_first_limit += 2
                result += changed_first_limit
            return result
        else:
            result = changed_first_limit
            while changed_first_limit != second_limit:
                changed_first_limit += 2
                result += changed_first_limit
            return result
    else:
        if second_limit % 2 == 0:
            changed_second_limit = int(second_limit - 1)
            result = first_limit
            while first_limit != changed_second_limit:
                first_limit += 2
                result += first_limit
            return result
        else:
            result = first_limit
            while first_limit != second_limit:
                first_limit += 2
                result += first_limit
            return result

limit_down = limits('Enter the bottom of the range: ')
limit_up = limits('Enter the upper limit of the range: ')

print(counting_unpaired_numbers(limit_down, limit_up))