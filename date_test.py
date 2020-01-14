"""
Your module description
"""
import datetime 


def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    input_date = datetime.date(year, month, 1)
    if (month > 0) and (month < 12): 
        # need to month after to be able to figure out days in the month
        month_after = datetime.date(year, month+1, 1)
    elif (month == 12):
        # If it is december 2019, then next year is 2020, Jan, 1
        month_after = datetime.date(year+1, 1, 1)
    else: 
        print("Invalid month")
        return
    days_per_month = month_after - input_date
    return days_per_month.days

def is_valid_date(year, month, day): 
    """
    Inputs: 
        year - integer representing the year
        month - integer representing the month
        day - an integer representing the day 
        
    Returns: 
        True -f year-month-day is a valid date and 
        False otherwise
    """
    MAX_YEAR = datetime.MAXYEAR
    print ("Max year is:", MAX_YEAR)
    MIN_YEAR = datetime.MINYEAR
    print ("Min year is:", MIN_YEAR)
    if (year >= MIN_YEAR) and (year <= MAX_YEAR): 
        print("The year", year, "is valid")
    else: 
        return False
    if (month > 0) and (month <=12): 
        print("month", month, "is valid")
    else:
        print("Invalid month")
        return False
    if (day > 0) and (day <= days_in_month(year,month)): 
        print("Days in month is valid", day)
    else: 
        print("Invalid number of days in the month")
        return False
    return True
def days_between(year1, month1, day1, year2, month2, day2): 
    """
    year1 0 integer representing year1
    month1 integer representing month1
    day1, year, representing day1
    """"
    if (is_valid_date(year1, month1, day1)):
        print("Valid date1!")
        valid_date1 = datetime.date(year1, month1, day1)
        print("date1 is", valid_date1)
    else:
        print("Invalid date1!")
        return 0
    if (is_valid_date(year2, month2, day2)):
        print("Valid date2!")
        valid_date2 = datetime.date(year2, month2, day2)
        print("date2 is", valid_date2)
    else:
        print("invalid date2!")
        return 0
    if (valid_date2 < valid_date1): 
        print("error date2 earlier than date1!")
        return 0 
    else: 
        days_between_dates = valid_date2 - valid_date1
        print("days between dates is:", days_between_dates.days)
        return days_between_dates
    return 0 

# Main Routine
print ("Number of days in December 2019 is:", days_in_month(2019, 12))
print ("Number of days in February 2018 is:", days_in_month(2018, 2))
print ("Number of days in February 2008 is:", days_in_month(2008, 2))
print ("Number of days in March 1967 is:", days_in_month(1967, 3))
print ("Number of days in June 1971 is:", days_in_month(1971, 6))
print ("Number of days in September 2001 is:", days_in_month(2001, 9))

print ("Testing second function:", is_valid_date(2019, 12, 26))
#date1 = datetime.date(2016, 1, 1)
#date2 = datetime.date(2016, 2, 1)
#delta = date2-date1

#print(date1)
#print(date1.year)
#print(date1.month)
#print(date1.day)
#print("number of days is", date2 - date1)
#print("days", delta.days)

date1 = datetime.date(2018, 12, 1)
date2 = datetime.date(2020, 1, 1)
difference = date2 - date1
print("The differenc in days between 2018, 12, 1 and 2020, 1,1 is", difference.days) 

#print(difference)
#print(difference.days)

#date3 = date1 + difference
#print(date2 == date3)

