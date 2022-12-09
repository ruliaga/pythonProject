# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

ls = input('Задайте элементы списка, введите числа через пробел: ').split(' ')
numList = []
for i in range(0, len(ls)):
    if float(ls[i])%1>0:
        numList.append(float(ls[i]))
print(f'{numList} ---> ', end='')

for i in range (0, len(numList)):
    numList[i] = numList[i]%1
print(round(max(numList)-min(numList), 3))



