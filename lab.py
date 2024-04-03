import matplotlib.pyplot as plt
import math
import random
import sys
from dataclasses import dataclass
from enum import Enum

class Equipment(Enum):
    LEFT = 1
    RIGHT = 2
    MIDDLE = 3
    RANDOM = 4

@dataclass
class Point:
    x: int
    y: int

@dataclass
class Settings:
    task: int
    start: int
    end: int
    accuracy: int
    equipment: Equipment

class CalculatorUtils:
    @staticmethod
    def get_formula_value_at(x: int, settings: Settings) -> int:
        match settings.task:
            case 2: return math.e ** x
            case 10: return math.e ** (2 * x)
            case _: raise Exception('Unsupported task')

    @staticmethod
    def calculate_graph_points(settings: Settings) -> list[Point]:
        points = []

        delta_x = CalculatorUtils.calculate_delta_x(settings)
        for i in range(settings.accuracy + 1):
            x = settings.start + i * delta_x
            points.append(Point(x, CalculatorUtils.get_formula_value_at(x, settings)))

        return points

    @staticmethod
    def calculate_delta_x(settings: Settings) -> int:
        return (settings.end - settings.start) / settings.accuracy

    @staticmethod
    def calculate_integral_shape_shift(settings: Settings) -> int:
        delta_x = CalculatorUtils.calculate_delta_x(settings)
        match settings.equipment:
            case Equipment.LEFT:   return 0
            case Equipment.RIGHT:  return delta_x
            case Equipment.MIDDLE: return delta_x / 2
            case Equipment.RANDOM: return random.uniform(0, delta_x)
            case _:                raise Exception('Unsupported equipment')

class Drawer:
    def __init__(self, settings: Settings):
        self.__settings = settings
        self.__points = CalculatorUtils.calculate_graph_points(settings)

    def create_integral_shape(self) -> list[plt.Rectangle]:
        rectangles = []

        delta_x = CalculatorUtils.calculate_delta_x(self.__settings)
        delta_x_shift = CalculatorUtils.calculate_integral_shape_shift(self.__settings)
        for point in self.__points:
            rectangles.append(self.create_integral_rectangle(point, delta_x, delta_x_shift))

        return rectangles

    def create_integral_rectangle(self, point: Point, delta_x: int, delta_x_shift: int) -> plt.Rectangle:
        return plt.Rectangle((point.x - delta_x_shift, 0), delta_x, point.y, edgecolor='red', facecolor='red')

    def create_window(self) -> None:
        plt.xlim(self.__settings.start, self.__settings.end)
        plt.ylim(0, max(point.y for point in self.__points))
        plt.grid(linestyle="--",alpha=0.5,zorder=1)
        plt.show()

    def draw_integral_sum(self) -> None:
        rectangles = self.create_integral_shape()
        for rectangle in rectangles:
            plt.gca().add_patch(rectangle)

    def draw_graph(self) -> None:
        settings_for_graph = Settings(
            task = self.__settings.task,
            start = self.__settings.start,
            end = self.__settings.end,
            accuracy = 1000000,
            equipment = Equipment.RANDOM
        )
        points = CalculatorUtils.calculate_graph_points(settings_for_graph)
        plt.plot([point.x for point in points], [point.y for point in points], color='black', linewidth=0.8)
        
    def draw(self) -> None:
        self.draw_graph()
        self.draw_integral_sum()
        self.create_window()

def read_settings(args: list[str]) -> Settings:
    # if len(args) < 5:
    #     print('Usage: python3 lab.py <start> <end> <accuracy> <equipment>')
    #     sys.exit(1)

    # settings = Settings(
    #     task = 2,
    #     start = int(args[1]),
    #     end = int(args[2]),
    #     accuracy = int(args[3]),
    #     equipment = Equipment(int(args[4]))
    # )
    settings = Settings(
        task = 2,
        start = 0,
        end = 1,
        accuracy = 30,
        equipment = Equipment.RANDOM
    )
    return settings

if __name__ == '__main__':
    drawer = Drawer(read_settings(sys.argv))
    drawer.draw()