import numpy as np

# случайные числа с равномерным распределением
rnd = np.random.random(100) * 1.1
print(rnd)
# Посчитаем среднее:
print('Среднее', np.mean(rnd))
# Максимум
print('Максимум', rnd.max())
# минимум
print('Минимум', rnd.min())



