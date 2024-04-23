""" Sample test """
from django.test import SimpleTestCase
import calc


class CalcTest(SimpleTestCase):
    """ Test the calc functions """
    
    def test_add_numbers(self):
        """ test for adding numbers """
        res = calc.add(5, 6)

        self.assertEqual(res, 11)
