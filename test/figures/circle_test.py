import unittest
from hacklab.figures.circle import Circle
from hacklab.figure import PI


class CircleTest(unittest.TestCase):

    def testCircle(self):
        my_ircle = Circle(radio=1)
        my_ircle.calculate_area()
        self.assertEqual(my_ircle.area, PI)

    def test_other_radio(self):
        my_ircle = Circle(radio=4)
        my_ircle.calculate_area()
        self.assertEqual(my_ircle.area, PI * (4 ** 2))

    def test_default_radio(self):
        my_ircle = Circle(radio=4)
        self.assertEqual(my_ircle.area, 0)
