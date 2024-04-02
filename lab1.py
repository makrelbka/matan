import matplotlib.pyplot as painter
import math



# def start(i, formula):
#     return painter.Rectangle(((i+1)*step_len, 0), step_len, formula, edgecolor='r', facecolor='black')

# def end(i, formula):
#     return painter.Rectangle((i*step_len, 0), step_len, formula, edgecolor='r', facecolor='black')

# def middle():
#     return 0


 

n = 100
start = 1
end = 2
step_len = (end - start) / n
x = start
while (x < end):
    formula = math.e ** x # формула
    rectangle = painter.Rectangle((x, 0), step_len, formula, edgecolor='r', facecolor='black')
    x += step_len
    painter.gca().add_patch(rectangle)

# координаты начала, длина, высота, красота 
painter.xlim(0, 2)
painter.ylim(0, 10)
painter.grid(True)
painter.show()
