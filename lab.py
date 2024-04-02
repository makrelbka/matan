import matplotlib.pyplot as painter
import math
import random
import sys
from enum import Enum

class Equipment(Enum):
    LEFT = 1
    RIGHT = 2
    MIDDLE = 3
    RANDOM = 4


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

def calculate_delta_x(start: int, end: int, accuracy: int) -> int:
    return (end - start) / accuracy

def calculate_graph_points(start: int, end: int, accuracy: int) -> list[Point]:
    points = []

    delta_x = calculate_delta_x(start, end, accuracy)
    for i in range(accuracy + 1):
        x = start + i * delta_x
        points.append(Point(x, get_formula_value_at(x)))

    return points

def calculate_integral_shape_shift(delta_x: int, equipment: Equipment):
    match equipment:
        case Equipment.LEFT:   return 0
        case Equipment.RIGHT:  return delta_x
        case Equipment.MIDDLE: return delta_x / 2
        case Equipment.RANDOM: return random.uniform(0, delta_x)
        case _:                raise Exception('Invalid equipment')

def create_integral_rectangle(point: Point, delta_x: int, delta_x_shift: int) -> painter.Rectangle:
    return painter.Rectangle((point.x - delta_x_shift, 0), delta_x, point.y, edgecolor='r', facecolor='black')

def create_integral_shape(points: list[Point], accuracy: int, equipment: Equipment) -> list[painter.Rectangle]:
    rectangles = []

    delta_x = calculate_delta_x(points[0].x, points[-1].x, accuracy)
    delta_x_shift = calculate_integral_shape_shift(delta_x, equipment)
    for point in points:
        rectangles.append(create_integral_rectangle(point, delta_x, delta_x_shift))

    return rectangles

def create_window(x_axis_size: tuple[int, int], y_axis_size: tuple[int, int]) -> None:
    painter.xlim(x_axis_size[0], x_axis_size[1])
    painter.ylim(y_axis_size[0], y_axis_size[1])
    painter.grid(True)
    painter.show()

def draw_integral_sum(start: int, end: int, accuracy:int, equipment: Equipment) -> None:
    points = calculate_graph_points(start, end, accuracy)
    rectangles = create_integral_shape(points, accuracy, equipment)
    for rectangle in rectangles:
        painter.gca().add_patch(rectangle)
    create_window((start, end), (0, max(point.y for point in points)))

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print('Usage: python3 lab.py <start> <end> <accuracy> <equipment>')
        sys.exit(1)

    start = int(sys.argv[1])
    end = int(sys.argv[2])
    accuracy = int(sys.argv[3])
    equipment = Equipment(int(sys.argv[4]))
    draw_integral_sum(start, end, accuracy, equipment)