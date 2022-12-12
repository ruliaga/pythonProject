# Вычислить число c заданной точностью d

import math

d = input('Введите необходимую точность d: ')
d = int(len(d)-2)
num_pi = round(math.pi,d)
print(f'при d = {d}, Pi = {num_pi}')