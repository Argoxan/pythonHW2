

class Shape:
    def __init__(self, name):
        self.name = name

    def name_upper(self):
        return self.name.upper()


class Rectangle(Shape):

    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

    def perimetr_calc(self):
        return (self.width*2 + self.height*2)

    def area_calc(self):
        return (self.width * self.height)

class Square(Rectangle):

    def __init__(self, name, side):
        self.name = name
        self.width = side
        self.height = side
        self.side = side

Shape1 = Shape("Some_shape")
Shape2 = Rectangle("Shape_1", 2, 4)
Shape3 = Square("Shape_2", 5)

print(Shape1.name_upper())      #Some functionalaty for Class Shape

print(Shape2.perimetr_calc())   #Using new method 

print(Shape3.area_calc())       #Showing inheretance from Rectangle
