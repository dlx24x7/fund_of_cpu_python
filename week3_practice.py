"""
week3_practice.py
This is my scratch file for my python3 practice
Author: ConradU
Date: 1/4/2020
"""

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

# Ex 6: name and age
def name_and_age(name, age):
    """
    This function returns a string in the form of name and age
    """
    if age > 0:
        name_age = name + " is " + str(age) + " years old."
    else:
        name_age = "Error: Invalid age"
    return name_age

# Ex 7: print_digits
def print_digits(number):
    """
    prints message the tens digit is % and the ones digit is % where the % is replaced with
    the correct values.  The function should error check when the number is negative or great than or equal to 100
    """
    if number > 0 and number <= 100:
        tens_digit = int(number / 10);
        ones_digit = int(number % 10);
        total_digits = "The tens digit is " + str(tens_digit) + ", and the ones digit is " + str(ones_digit) + "."
    else:
        total_digits = "Error: Input is not a two-digit number."
    return print(total_digits)

# Ex 8: name_lookup 
def name_lookup(first_name): 
    """
    takes valid firstname and returns last name else returns error
    """
    if first_name == "Joe": 
        last_name = "Warren"
    elif first_name == "Scott": 
        last_name = "Rixner"
    elif first_name == "John": 
        last_name = "Greiner"
    elif first_name == "Stephen":
        last_name = "Wong"
    else: 
        last_name = "Error: Not an instructor"
    return last_name

# Ex 9: pig latin
def pig_latin(word): 
    """
    takes a string world and apply the following rules to return the pig latin version of the word
    """
    first_letter = word[0]
    rest_of_word = word[1 : ]
    #print("First letter is", first_letter)
    #print("rest_of_word is", rest_of_word)
    if first_letter == 'a' or first_letter == 'e' or first_letter == 'i' or first_letter == 'o' or first_letter == 'u': 
        pig_latin_word = word + 'way'
    else: 
        pig_latin_word = rest_of_word + first_letter + 'ay'
    return pig_latin_word
    
print("Is 1 even?", is_even(1))
print("Is Joe cool?", is_cool("Joe"))
print(interval_intersect(1, 2, 0, 1))
