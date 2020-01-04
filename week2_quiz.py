"""
week2_quiz.py
This is my scratch file for my python3 quiz
Author: ConradU
Date: 1/4/2020
"""
def project_to_distance(point_x, point_y, distance):
    dist_to_origin = (point_x ** 2 + point_y ** 2) ** 0.5
    scale = distance / dist_to_origin
    print(point_x * scale, point_y * scale)

project_to_distance(2, 7, 4)

def math_function(x):
    """
    Implement f(x) = -5x**5 + 67x**2 - 47 and return a value
    """
    result = -5*(x**5) + 67*(x**2) - 47
    return result

print("f(0): ", math_function(0))
print("f(1): ", math_function(1))
print("f(2): ", math_function(2))
print("f(3): ", math_function(3))

def future_value(present_value, annual_rate, periods_per_year, years):
    """
    Input: the numbers present_value, annual_rate, periods_per_year, years
    Output: future value based on formula given in question
    """
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    future_value = present_value * (1 + rate_per_period)**periods
    return future_value


print("$500 at 4% compounded daily for 10 years yields $", future_value(500, .04, 10, 10))
print("$1000 at 2% compounded daily for 4 years yields $", future_value(1000, .02, 365, 4))

def area_eq_tri(side):
    """
    This section calculates the area of an equalateral triangle
    """
    area_eq_tri = ((3**0.5) / 4) * side**2
    return area_eq_tri

print("Area of a equalateral triangle with a side of 2 is:", area_eq_tri(2))
print("Area of a equalateral triangle with a side of 5 is:", area_eq_tri(5))
