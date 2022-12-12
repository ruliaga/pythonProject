# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

k = int(input('Введите число k: '))
ls = [0,1]
def fibo (k):
    for i in range (0,k-1):
        ls.append(ls[i]+ls[i+1])
    for i in range (0, k):
        ls.insert(0, ls[1]-ls[0])
fibo (k)
print(f'Для {k} список будет выглядеть так: {ls}')
