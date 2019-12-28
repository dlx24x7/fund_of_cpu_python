"""
Practice Exercises for Expressions
Week1_practice.py
Dec 28 2019
"""

# Exercise 1: there are 5280 feet in a mile.   Write a python statement that calculates and prints the number of feet in 13 miles
feet_per_mile = 5280
feet_per_13miles = 13 * feet_per_mile
print("The number of feet in 13 miles is:", feet_per_13miles)

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
print("The number of sec in 7 hours, 21 min and 37 sec is:", sec_per_7_hours + sec_per21_min + 37)

# Exercise 3: The perimeter of a rectangle is 2w + 2h, where w and h are lengths of its sides.
# Write a python statement the calculates the perimeter of a rectangle with sides 4 and 7 inches
width = 4
height = 7
perimeter = 2 * width + 2 * height
print("The perimeter of a 4 by 7 inch rectangle is:", perimeter)
