# In this project you will use object oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle and inherit methods and attributes.

# Rectangle class

# When a Rectangle object is created, it should be initialized with width and height attributes. The class should also contain the following methods:

# set_width
# set_height
# get_area: Returns area (width * height)
# get_perimeter: Returns perimeter (2 * width + 2 * height)
# get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)
# get_picture: Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
# get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
# Additionally, if an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10)

# Square class

# The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. The __init__ method should store the side length in both the width and height attributes from the Rectangle class.

# The Square class should be able to access the Rectangle class methods but should also contain a set_side method. If an instance of a Square is represented as a string, it should look like: Square(side=9)

# Additionally, the set_width and set_height methods on the Square class should set both the width and height.



class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return "Area is: {}".format(self.width * self.height)

    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return "Perimeter is: {}".format(perimeter)

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return "Diagonal is: {}".format(diagonal)

    def get_picture(self):
        if (self.width > 50):
            return "Too big for picture."
        if (self.height > 50):
            return "Too big for picture."
        line = '*' * self.width  # Number of '*' in each line
        lines = [line for _ in range(self.height)]  # Number of lines in shape
        picture = '\n'.join(lines)
        return picture + "\n"

    def get_amount_inside(self, shape):
        w = self.width // shape.width
        h = self.height // shape.height

        return w * h

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return "Square (side= {})".format(self.width)



rect = Rectangle(40, 40)
print(rect.__str__())
print(rect.get_area())
print(rect.get_perimeter())
print(rect.get_picture())


sq = Square(9)
print(sq.get_area())
print(sq.get_diagonal())
print(sq.get_picture())
print(sq.__str__())
