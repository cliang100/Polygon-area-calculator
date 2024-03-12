**Polygon Area Calculator**

---

**Introduction**

The Polygon Area Calculator is a Python program designed to calculate the area, perimeter, and other properties of rectangles and squares. It consists of two classes: `Rectangle` and `Square`, which are used to represent rectangles and squares, respectively. This program demonstrates object-oriented programming principles in Python, including inheritance and method overriding.

---

**Features**

1. **Rectangle Class**: Represents a rectangle with given width and height.
   - Provides methods to set width and height.
   - Calculates area, perimeter, diagonal, and checks if the rectangle is too large for a picture.
   - Generates a picture representation of the rectangle using asterisks.

2. **Square Class**: Inherits from the Rectangle class, representing a square with a given side length.
   - Ensures that the width and height are always equal, as squares have equal sides.
   - Overrides the `__str__` method to provide a customized string representation for squares.

3. **Comparing Shapes**:
   - The `get_amount_inside` method in the Rectangle class enables comparison between shapes by calculating how many times one shape can fit inside another.

---

**Usage**

1. **Rectangle Class**:
   ```python
   rect = Rectangle(10, 5)
   print(rect.get_area())  # Output: 50
   rect.set_height(3)
   print(rect.get_perimeter())  # Output: 26
   print(rect)  # Output: Rectangle(width=10, height=3)
   print(rect.get_picture())  # Output: **********
                                **********
                                **********
   ```

2. **Square Class**:
   ```python
   sq = Square(9)
   print(sq.get_area())  # Output: 81
   sq.set_side(4)
   print(sq.get_diagonal())  # Output: 5.656854249492381
   print(sq)  # Output: Square(side=4)
   print(sq.get_picture())  # Output: ****
                                ****
                                ****
                                ****
   ```

3. **Comparing Shapes**:
   ```python
   rect.set_height(8)
   rect.set_width(16)
   print(rect.get_amount_inside(sq))  # Output: 8
   ```

---

**Conclusion**

The Polygon Area Calculator provides a simple yet effective way to work with rectangles and squares in Python. It demonstrates fundamental concepts of object-oriented programming and serves as a useful tool for calculating various properties of polygons.

---
