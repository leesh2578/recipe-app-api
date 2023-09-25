"""
Sample tests
"""

from django.test import SimpleTestCase

from . import calc

class Caltests(SimpleTestCase):
    def test_add_number(self):
        res = calc.add(5,6)

        self.assertEqual(res,11)
    
    def test_subtract_number(self):
        res = calc.subtract(15,10)

        self.assertEqual(res, 5)