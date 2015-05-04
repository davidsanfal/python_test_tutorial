import unittest
from hacklab.figures.square import Square


test_sides = ((1, 1),
              (1, 2),
              (4, 4),
              (12, 22))


class SquareTest(unittest.TestCase):

    def testSquare(self):
        my_square = Square(1, 2)
        my_square.calculate_area()
        self.assertEqual(my_square.area, 2)

    def test_other_size(self):
        my_square = Square(4, 20)
        my_square.calculate_area()
        self.assertEqual(my_square.area, 4 * 20)

    def test_default_area(self):
        my_square = Square(1, 2)
        self.assertEqual(my_square.area, 0)

    def test_multi_area(self):
        for side1, side2 in test_sides:
            my_square = Square(side1, side2)
            my_square.calculate_area()
            self.assertEqual(my_square.area,
                             self.area(side1, side2))

    def area(self, a, b):
        return a * b
