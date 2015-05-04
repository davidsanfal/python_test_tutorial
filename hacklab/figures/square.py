from hacklab.figure import Figure


class Square(Figure):
    def __init__(self, side1, side2, name='Square'):
        self.side1 = side1
        self.side2 = side2
        super(Square, self).__init__(name)

    def print_name(self):
        print(self.name)

    def calculate_area(self):
        self.area = self.side1 * self.side2