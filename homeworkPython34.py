class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


test = Rectangle(5, 4)

print(test.get_area())

test.height, test.width = 7, 5

print(test.get_area())

#-----------------------------------------------------------------------------------------------------------------------

class Counter:
    def __init__(self):
        self.num = 0

    def plus(self):
        self.num += 1
        print(f"Значение увеличено, текущее: {self.num}")

    def minus(self):
        self.num -= 1
        print(f"Значение уменьшено, текущее: {self.num}")

    def show_number(self):
        return self.num

test2 = Counter()

test2.plus()
test2.plus()
test2.plus()

test2.minus()

print(test2.show_number())



