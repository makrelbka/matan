import matplotlib.pyplot as f
import math



# def start(i, exp):
#     return f.Rectangle(((i+1)*exact_len, 0), exact_len, exp, edgecolor='r', facecolor='black')

# def end(i, exp):
#     return f.Rectangle((i*exact_len, 0), exact_len, exp, edgecolor='r', facecolor='black')

# def middle():
#     return 0


 

n = 100
start = 1
end = 2
exact_len = (end - start) / n
x = start
while (x < end):
    exp = math.e ** x # формула
    rectangle = f.Rectangle((x, 0), exact_len, exp, edgecolor='r', facecolor='black')
    x += exact_len
    f.gca().add_patch(rectangle)

# координаты начала, длина, высота, красота 
f.xlim(0, 2)
f.ylim(0, 10)
f.grid(True)
f.show()
