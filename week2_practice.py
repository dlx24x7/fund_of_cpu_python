"""
Week2_practice.py
This program is about week 2 programming
"""
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