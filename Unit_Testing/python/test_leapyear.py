# -*- coding: utf-8 -*-
'''
Unit test for leapyear.py
Student version
'''

import unittest
import leapyear
class KnownValues(unittest.TestCase):
    known_values = ((2000, "is a leap year"),
                    (1904, "is a leap year"),
                    (2400, "is a leap year"),
                    (2020, "is a leap year"),
                    (2010, "is not a leap year"),
                    (1900, "is not a leap year"),
                    (1800, "is not a leap year"),
                    (2002, "is not a leap year"))
    
    def test_to_leapyear_values(self):                                             
        ''' should give known result with known input'''
        for year, numeral in self.known_values:
            result = leapyear.to_leap_year(year) 
            self.assertEqual(numeral, result)


class LeapYearBadInput(unittest.TestCase):
    '''Your Abc unittests code goes here'''
    def test_blank_string(self):                                             
        '''should fail with blank string'''
        self.assertRaises(leapyear.NotIntegerError, leapyear.to_leap_year, "")
    def test_negativ(self):                                             
        '''should fail with negative input'''
        self.assertRaises(leapyear.OutOfRangeError, leapyear.to_leap_year, -1)
    def test_non_integer(self):                                             
        '''should fail with non-integer input'''
        self.assertRaises(leapyear.NotIntegerError, leapyear.to_leap_year, 0.5)
    def test_string(self):                                             
        '''should fail with string input'''
        self.assertRaises(leapyear.NotIntegerError, leapyear.to_leap_year, "V")


if __name__ == '__main__':
    unittest.main()
