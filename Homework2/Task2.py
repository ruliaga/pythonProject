# Напишите программу, которая принимает на вход 
# число N и выдает набор произведений чисел от 1 до N.

num = int(input('Введите число N: '))
ls = []
x = 1
for i in range (1, num+1):
    x = x*i
    ls.append(x)
print(f'Пусть N = {num}, тогда {ls}')