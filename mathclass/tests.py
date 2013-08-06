"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from mathclass.fizzbuzz import * 

#does not work without database configuration

class FizzBuzzTest(TestCase):
    def test_multiple_three(self):
        """
        Tests that multiples of three are Fizz
        """
        for i in range(100):
            self.assertEqual(isFizz(i*3) == True)

    def test_multiple_five(self):
        """
        Tests that multiples of five are Buzz
        """
        for i in range(100):
            self.assertEqual(isBuzz(i*5) == True)

    #etc
