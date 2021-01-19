from ClassRectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

square_1 = Square(5)
square_2 = Square(10)

circle_1 = Circle(7)
circle_2 = Circle(14)

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure, Rectangle):
        print(f'Площадь прямоугольника со сторонами {figure.a}x{figure.b} равна {figure.get_area()}')
    elif isinstance(figure, Square):
        print(f'Площадь квадрата со стороной {figure.a} равна {figure.get_area()}')
    else:
        print(f'Площадь кругом с радиусом {figure.r} равна {figure.get_area()}')

