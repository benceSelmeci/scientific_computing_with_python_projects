import shape_calculator


rect = shape_calculator.Rectangle(5, 10)
print(rect.get_area())       # "50"
rect.set_width(3)
print(rect.get_perimeter())  # "26"
print(rect)                  # "Rectangle(width=3, height=10)""

sq = shape_calculator.Square(9)
print(sq.get_area())         # "81"
sq.set_side(4)
print(sq.get_diagonal())     # "5.656854249492381"
print(sq)                    # "Square(side=4)"
