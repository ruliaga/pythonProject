# Задача Измените код одной-двух решенных ранее задач 
# (с прошлых семинаров или домашних работ), 
# применив лямбды, filter, map, zip, enumerate, списочные выражения.

# 1 - Homework2 Task1
# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

# Решение
# num = input('Введите вещественное число: ')
# sum = 0
# for i in num:
#     if i != '.' and i != '-':
#         x = int(i)
#         sum = sum + x
# print(f'{num} --> {sum}')

num = list(filter(lambda x: x != '.' and x != '-', input('Введите число: ')))
summa = sum(map(int,num))
print(summa)