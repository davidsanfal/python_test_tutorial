import unittest
from hacklab.figure import Figure


class FigureTest(unittest.TestCase):

    def test_figure(self):
        my_figure = Figure('test_name')
        self.assertEqual(my_figure.name, 'test_name')
        self.assertRaises(Exception, my_figure.calculate_area)
        my_figure.name = 'other_test_name'
        self.assertEqual(my_figure.name, 'other_test_name')

    def test_new_figure(self):
        class MyOtherFigure(Figure):
            pass

        my_other_figure = MyOtherFigure('hello')
        self.assertRaises(Exception, my_other_figure.calculate_area)

        class MySuperOtherFigure(Figure):
            def calculate_area(self):
                self.area = 10

        my_other_figure = MySuperOtherFigure('hello')
        my_other_figure.calculate_area()
        self.assertEqual(my_other_figure.area, 10)