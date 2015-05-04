from hacklab.figure import Figure, PI


class Circle(Figure):
    def __init__(self, radio, name='Circle'):
        self.radio = radio
        super(Circle, self).__init__(name)

    def print_name(self):
        print(self.name)

    def calculate_area(self):
        self.area = PI * (self.radio ** 2)