from django.test import TestCase
from .change_link import change_link
from .day_computed import day_computed
# Create your tests here.

class TestCi(TestCase):

    def test(self):
        self.assertEqual(1, 1)
    
    def test_daycomputed(self):
        self.assertEqual(day_computed('2022-01-21'), 1)

    def test_change_link(self):
        self.assertEqual(change_link(''), )