"""
Week2_practice.py
This program is about week 2 programming
Author: ConradU 
Date: 01/04/2020
"""
import math
PI = math.pi

# Ex 1
def miles_to_feet(miles):
    """
    This function converts miles into feet
    """
    total_feet = 5280 * miles
    return total_feet

# Ex 2    
def total_seconds(hours, minutes, seconds): 
    """
    total_seconds takes three parameters, hours minutes and seconds
    it returns the total number of seconds for hours, minutes and seconds
    """
    seconds_per_min = minutes * 60 
    seconds_per_hour = hours * 60 * 60 
    total_seconds = seconds_per_hour + seconds_per_min + seconds
    return total_seconds
    
# Ex 3
def rectangle_perimeter(width, height): 
    """
    rectangle_perimeter takes two parameters width and height
    and returns the permite of the rectangle in inches
    """
    perimeter = 2 * width + 2 * height
    return perimeter
    
# Ex 4
def rectangle_area(width, height): 
    """
    returns the rectangle area for a given width and height
    """
    area = width * height
    return area
    
# Ex 5
def circle_circumference(radius): 
    """
    returns the circle_circumference for a given radius
    """
    circumference = 2 * PI * radius
    return circumference
    
# Ex 6
def circle_area(radius): 
    """
    returns the area of the circle for a given radius
    """
    circle_area = PI * (radius ** 2)
    return circle_area
    
# Ex 7
def future_value(present_value, annual_rate, years): 
    """
    returns compounded future_value based on a present_value, annual_rate and years
    """
    future_value = present_value * (1 + (0.01 * annual_rate)) ** years
    return future_value

# Ex 8
def name_tag(first_name, last_name): 
    """
    returns my name is when the strings are the firstname and lastname
    """
    name_tag = "My name is " + first_name + ' ' + last_name + "."
    return name_tag
    
# Ex 9
def name_and_age(name, age): 
    """
    returns a string in the form of % is % years old using name and age
    """
    name_and_age = name + " is " + str(age) + " years old. "
    return name_and_age

# Ex 10
def point_distance(x_0, y_0, x_1, y_1): 
    """
    returns the point dstance given x_0,x_1, y_0, y_1
    """
    x_dist = x_1 - x_0
    y_dist = y_1 - x_0
    point_distance = math.sqrt( (x_dist)**2 + (y_dist)**2)
    return point_distance
    
# Input for Ex 1: miles_to_feet
miles = 13
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")

miles = 57
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")

miles = 82.67
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")

# Input for Ex 2: total_seconds
hours, minutes, seconds = 7, 21, 37
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

hours, minutes, seconds = 10, 1, 7
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

hours, minutes, seconds = 1, 0, 1
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")
      
# Input for Ex 3: perimeter
width, height = 4, 7
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")

width, height = 7, 4
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")

width, height = 10, 10
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")
