import matplotlib.pyplot as plt

def count():
    file = open('dada.txt', 'w')
    for i in range(-10000, 10000):
        x = str(i // 100)
        y = str((i // 100) ** 2)
        s = x + ' ' + y + '\n'
        file.write(s)


def rects():
    file = open('dada.txt', 'w')
    for i in range(10):
        x = str(i)
        y = str(0)
        h = str(i + 1)
        s = x + ' ' + y + ' ' + h + '\n'
        file.write(s)


def f(x):
    # Здесь определяется функция, которую вы хотите проинтегрировать
    return x**2  # Пример: интеграл x^2

def integral_sum(f, a, b, n):
    delta_x = (b - a) / n  # Длина каждого подынтервала
    integral = 0
    for i in range(n):
        x_i = a + i * delta_x  # Начальная точка подынтервала
        x_i_star = x_i + delta_x  # Точка внутри подынтервала (в данном случае, правая граница подынтервала)
        integral += f(x_i_star) * delta_x  # Добавляем площадь прямоугольника
    return integral

rects()
file = open("dada.txt")
data = file.readlines()
x_values = []
y_values = []
heights = []
for line in data:
    x, y, h = map(float, line.strip().split())
    x_values.append(x)
    y_values.append(y)
    heights.append(h)
plt.plot(x_values, y_values)
plt.xlabel('X')
plt.ylabel('Y', rotation=0)

for i in range(len(x_values)):
    rectangle = plt.Rectangle((x_values[i], y_values[i]), 1, heights[i], edgecolor='r', facecolor='pink')
    plt.gca().add_patch(rectangle)
plt.xlim(0, 6)
plt.ylim(0, 6)

plt.grid(True)
plt.show()
