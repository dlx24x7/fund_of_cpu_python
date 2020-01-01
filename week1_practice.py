"""
Practice Exercises for Expressions
Week1_practice.py
Dec 28 2019
course: Python 3 scripting
course: Fundamentals of computing
"""

# Exercise 1: there are 5280 feet in a mile.   Write a python statement that calculates and prints the number of feet in 13 miles
feet_per_mile = 5280
feet_per_13miles = 13 * feet_per_mile
print("Ex 1: The number of feet in 13 miles is:", feet_per_13miles)

# Exercise 2: Write a statement that calculates and prints the number of seconds in 7 hours, 21 minutes and 37 seconds
seconds_per_min = 60
min_per_hour = 60
sec_per_hour = seconds_per_min * min_per_hour
print("The number of sec in an hour is:", sec_per_hour)

# number of second in 7 hours
sec_per_7_hours = 7 * sec_per_hour
print("The number of sec in 7 hours is:", sec_per_7_hours)

# number of sec in 21 min 
sec_per21_min = 21 * seconds_per_min
print("The number of sec in 21 min is:", sec_per21_min)

# the number of sec in 7 hours, 21 min and 37 sec
print("Ex 2: The number of sec in 7 hours, 21 min and 37 sec is:", sec_per_7_hours + sec_per21_min + 37)

# Exercise 3: The perimeter of a rectangle is 2w + 2h, where w and h are lengths of its sides.
# Write a python statement the calculates the perimeter of a rectangle with sides 4 and 7 inches
width = 4
height = 7
perimeter = 2 * width + 2 * height
print("Ex 3: perimeter of a 4 by 7 inch rectangle is:", perimeter)

# exercise 4: The area of a rectangle is width * height.  Write a pythone statement that calculates
# the area of a rectangle that with a width of 4 inches and a height of 7 inches
width = 4
height = 7
area = width * height
print("Ex 4: The area of a 4 by 7 inch rectangle is:", area)

# exercise 5: the circumference of a circle is 2 * PI * radius.  Assume PI is 3.14 and the radius is 8
# what is the circumference of the triangle? 
radius = 8
PI = 3.14
circumference = 2 * PI * radius
print("Ex 5: The circumference of a circle with an 8 inch radius is:", circumference)

# exercise 6: The area of a circle is PI * radius ** 2; what is the area of a circle
radius = 8
PI = 3.14
circle_area = PI * (radius ** 2)
print("Ex 6: The area of a cricle with an an inch radius is:", circle_area)

# exercise 7: Given p dollars, the future value of this money when compounded yearly at a rate of r percent fo y years
# is p(1 + 0.01*r)**y.  Write a statement that calculates the value of 1000 = principle 7 is the rate and 7 is the years
principle = 1000
rate = 7 
year = 10 
future_value = principle * (1 + (0.01 * rate)) ** year
print("Ex 7: With 1000 dollars and a 7 percent interest, in 10 years your money would be:", future_value)

# exercise 8: Write a python statement that combines three strings: My name is Joe and Warren
string1 = "My name is"
string2 = "Joe"
string3 = "Warren."
print("Ex 8:", string1 + ' ' + string2 + ' ' + string3)

# exercise 9: Write a python expression that creates a string Joe Warren is 56 years old
string1 = "Joe Warren is"
age = 56
string2 = str(age)
string3 = "years old."
print("Ex 9:", string1 + ' ' + string2 + ' ' + string3)
