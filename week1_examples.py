"""
This is my first program 
Its an example to teach you the fundamentals of python
Week1_examples.py
"""
# Arithmetic expressions - numbers, operators, expressions

print(3, -1, 3.141459, -2.8)

# numbers - two types, an integer or a decimal number
# two corresponding data types int() and float()

print(type(3), type(3.14159))
print(type(3.0))

# we can convert between data types using int() and float()
# note that int() takes the "whole" part of a decimal number
# float() applied to integers is boring

print(int(3.14159), int(-2.8))
print(float(3), float(-1))

# floating point number have around 15 decimals of accuracy
# pi is 3.1415926535897932384626433832795028841971...
# square root of two is 1.414213562373095048801688724209698

print(3.1415926535897932384626433832795028841971)
print(1.414213562373095048801688724209698)

# arithmetic operations
# + plus addition
# - minus subtraction
# * times multiplication
# / divided by divsion
# ** power exponetiation

print(1+2, 3 - 4, 5* 6, 2 ** 5)

# division in python 3
# if one operand is a decimal (float), the answer is decimal

print(1.0/3, 5.0/2.0, -7/3.0)

# what happens when both numbers are integers

print(1/3, 5/2, -7/3)

# expressions - number or a binary operator applited to two expressions

print(1+2*3, 4.0 - 5.0 / 6.0, 7*8 + 9 * 10)

# expressions are entered as sequence of numbers and operators

print(1 * 2 + 3 * 4)
print(2 + 12)

# always manually group using parantheses when in doubt

print(1 * (2+3) *4)
print(1 * 5 * 4) 