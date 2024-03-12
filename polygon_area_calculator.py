class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        if width > 0:
            self.width = width
        else:
            return "Width must be a positive number."
    
    def set_height(self, height):
        if height > 0:
            self.height = height
        else:
            return "Height must be a positive number."
    
    def get_area(self):
        # Returns area (width * height)
        return self.width * self.height
    
    def get_perimeter(self):
        # Returns perimeter (2 * width + 2 * height)
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        # Returns diagonal ((width ** 2 + height ** 2) ** .5)
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        # Creates the rectangle with '*'
        # looks like this:
        # **********
        # **********
        # **********
        # Width/height limit is 50 ("Too big for picture")
        if self.width > 50 or self.height > 50:
            return "Too big for picture"
        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture
    
    def get_amount_inside(self, other_shape):
        # Takes another shape, square or rectangle, as an argument
        # Returns num of times other shape can fit in the shape
        return self.get_area() // other_shape.get_area()
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)  # Make height and width equal

    def set_side(self, side_length):
        self.width = side_length
        self.height = side_length
    
    def __str__(self):
        return f'Square(side={self.height})'
    

if __name__ == '__main__':
    # Rectangle test
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    # Square test
    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    # Compare shapes
    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))