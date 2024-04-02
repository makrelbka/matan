from xml.parsers import expat
import matplotlib.pyplot as f
import math


# координаты начала, длина, высота, красота 
def start(i, exp):
    return f.Rectangle(((i+1)*exact_len, 0), exact_len, exp, edgecolor='r', facecolor='black')

def end(i, exp):
    return f.Rectangle((i*exact_len, 0), exact_len, exp, edgecolor='r', facecolor='black')

def middle():
    return 0


 

n = 4
end = 2
start = 1
exact_len = (end - start) / n
i = 0
while (i*exact_len < end):
    x = i*exact_len
    exp = math.e ** x # формула
    rectangle = f.Rectangle((i*exact_len, 0), exact_len, exp, edgecolor='r', facecolor='black')
    i += 1
    if (i*exact_len < start):
        continue
    f.gca().add_patch(rectangle)


f.xlim(0, 2)
f.ylim(0, 10)
f.grid(True)
f.show()
