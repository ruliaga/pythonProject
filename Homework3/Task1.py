# Задайте список из нескольких чисел.
#  Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

ls = input('Задайте элементы списка, введите числа через пробел: ').split(' ')
print(f'{ls} ---> на нечётных позициях элементы ', end='')
sum = 0
for i in range(0, len(ls)-1):
    if i % 2 > 0:
        sum = sum + int(ls[i])
        print(f'{ls[i]} ', end='') 
print(f'. Ответ: {sum}', end='')
        