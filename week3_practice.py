"""
week3_practice.py
This is my scratch file for my python3 practice
Author: ConradU
Date: 1/4/2020
"""
import set
# Ex 1; is even
def is_even(number): 
    """
    returns True if number is even and False if number is odd
    """
    if ((number%2) == 0): 
        return True
    else:
        return False
        
# Ex 2; is_cool
def is_cool(name): 
    """
    returns true if name is cool or false if otherwise
    """
    if (name == "Joe") or (name == "John") or (name == "Stephen"):
        return True
    else: 
        return False

# Ex 3: is_lunchtime
def is_lunchtime(hour, is_am): 
    """
    Returns true if hour corresponds to 11am or 12 pm
    """
    if (hour > 1) and (hour <= 12): 
        if (hour == 11) and (is_am == True): 
            return True
        elif (hour == 12) and (is_am == False): 
            return True
        else: 
            return False

# Ex 4: is_leap_year
def is_leap_year(year): 
    """
    if (year is not divisible by 4) then (it is a common year)
    else if (year is not divisible by 100) then (it is a leap year)
    else if (year is not divisible by 400) then (it is a common year)
    else (it is a leap year)
    """
    if (year % 4) != 0: 
        return False
    elif (year % 100) != 0:
        return True
    elif (year % 400) != 0: 
        return False
    else: 
        return True

# Ex 5: interval_intersect
def interval_intersect(a, b, c, d):
    """
    returns True if intervals [a,b]  and [c, d] intersect and False otherwise
    """
    if (c <= b) and (a <= d): 
       return True
    else: 
       return False 
        
        
print("Is 1 even?", is_even(1))
print("Is Joe cool?", is_cool("Joe"))
interval_intersect(1, 2, 0, 1)