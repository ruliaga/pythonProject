# Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N.

num = int(input('Введите число N: '))
ls = []
def mnozh (N):
    for i in range(2, N+1):
        if N%i == 0:
            N = N//i
            ls.append(i)   
    if N > 1:
        mnozh (N)
mnozh (num)
print(ls)

