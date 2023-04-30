# -*- coding: utf-8 -*-
'''
There is a leap year every year whose number is perfectly divisible by four - 
except for years which are both divisible by 100 and not divisible by 400. 
The second part of the rule effects century years. 
For example; the century years 1600 and 2000 are leap years, 
but the century years 1700, 1800, and 1900 are not.
'''

class NotIntegerError(ValueError): pass
class OutOfRangeError(ValueError): pass

def to_leap_year(year):
    if (year == "" or isinstance(year, str) == True):                                       
        raise NotIntegerError("Fail with blank string")
    if not (0 < year < 3000):
        raise OutOfRangeError("number out of range (must be 1...3000)")
    if not isinstance(year, int):                                       
        raise NotIntegerError('non-integers can not be converted')
   
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "is a leap year")
                return "is a leap year"
            else:
                print(year, "is not a leap year")
                return "is not a leap year"
        else:
            print(year, "is a leap year")
            return "is a leap year"
    else:
        print(year, "is not a leap year")
        return "is not a leap year"

    


if __name__ == '__main__':
    to_leap_year(2021)
