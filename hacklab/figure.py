PI = 3.1416


class Figure(object):
    def __init__(self, name):
        self.name = name
        self.area = 0

    def print_area(self):
        print(self.area)

    def calculate_area(self):
        raise Exception("Define me!")
