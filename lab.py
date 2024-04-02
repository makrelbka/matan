import matplotlib.pyplot as painter
import math

class Point:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y

def get_formula_value_at(x: int) -> int:
    return math.e ** x

def calculate_step(start: int, end: int, accuracy: int) -> int:
    return (end - start) / accuracy

def calculate_graph_points(start: int, end: int, accuracy: int) -> list[Point]:
    points = []

    step = calculate_step(start, end, accuracy)
    x = start
    while (x < end):
        points.append(Point(x, get_formula_value_at(x)))
        x += step

    return points

def create_integral_shape(points: list[Point], accuracy: int) -> list[painter.Rectangle]:
    rectangles = []

    step = calculate_step(points[0].x, points[-1].x, accuracy)
    for point in points:
        rectangles.append(painter.Rectangle((point.x, 0), step, point.y, edgecolor='r', facecolor='black'))

    return rectangles
        
def create_window() -> None:
    painter.xlim(0, 3)
    painter.ylim(0, 3)
    painter.grid(True)
    painter.show()

def main(start: int, end: int, accuracy: int):
    points = calculate_graph_points(start, end, accuracy)
    rectangles = create_integral_shape(points, accuracy)
    for rectangle in rectangles:
        painter.gca().add_patch(rectangle)
    create_window()

main(0, 1, 100)