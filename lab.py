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
            case 1:  return math.sin(x)
            case 2:  return math.e ** x
            case 10: return math.e ** (2 * x)
            case 22: return x ** 3
            case 26: return math.e ** (2 * x)
            case 31: return 3 ** x 
            case _:  raise Exception('Unsupported task')

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

    def get_formula_text(self) -> str:
        match self.__settings.task:
            case 2:  return r'$y = e^x$'
            case 10: return r'$y = e^{2x}$'
            case 22: return r'$y = x^3$'
            case 26: return r'$y = e^{2x}$'
            case 31: return r'$y = 3^x$'
            case _:  raise Exception('Unsupported task')

    def create_window(self) -> None:
        plt.subplots_adjust(bottom=0.25)
        plt.title(self.get_formula_text(), fontsize=20)
        plt.xlim(self.__settings.start, self.__settings.end)
        plt.ylim(min(point.y for point in self.__points) - 1, max(point.y for point in self.__points) + 1)
        plt.grid(linestyle="--", alpha=0.5, zorder=0)

    def draw_integral_sum(self) -> None:
        rectangles = self.create_integral_shape()
        for rectangle in rectangles:
            plt.gca().add_patch(rectangle)

    def draw_graph(self) -> None:
        fig, ax = plt.subplots()
        x = np.linspace(0, 2*np.pi, 100)
        y = np.sin(x)
        line, = ax.plot(x, y)
        ax.set_title('График функции синуса')
        ax.set_xlabel('Угол')
        ax.set_ylabel('Значение функции синуса')
        ax.grid(True)

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
        task = 1,
        start = -5,
        end = 5,
        accuracy = 100,
        equipment = Equipment.MIDDLE
    )
    return settings

if __name__ == '__main__':
    Drawer(read_settings(sys.argv)).draw()
    plt.show()
