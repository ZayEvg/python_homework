"""
Користувач уводить ціни 1 кг цукерок і 1 кг печива. Знайти вартість:
а) однієї покупки з 300 г цукерок і 400 г печива;
б) трьох покупок, кожна з 2 кг печива і 1 кг 800 г цукерок.
"""
import re

re_float = re.compile("^[-+]{0,1}\d+\.{0,1}\d*$")


def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text


def float_greater_zero_validator(prompt):
    number = float(validator(re_float, prompt))
    while number <= 0:
        number = float(validator(re_float, prompt))
    return number


sweets_1kg = float_greater_zero_validator('Enter price of kilogram of sweets: ')
cookies_1kg = float_greater_zero_validator('Enter price of kilogram of cookies: ')

print("The cost of 300 grams of sweets and 400 grams of cookies: " + str(0.3*sweets_1kg + 0.4*cookies_1kg))
print("The cost of 3 purchases of 1.8 kilograms of sweets and 2 kilograms of cookies: " + str(3*(1.8*sweets_1kg + 2*cookies_1kg)))