# Задайте список из n чисел последовательности 
# (1+1/n)^n и выведите на экран их сумму.

num = int(input('Введите число N: '))
ls = []
sum = 0
for i in range(1, num):
    ls.append(round((1 + 1/i)**i,2))
    sum = sum + ls[i-1]
print(f'{ls} ---> сумма равна {sum}')