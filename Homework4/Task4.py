# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.

import random

k = int(input('Введите значение степени k: '))

list1 = []

for i in range (0, k):
    list1.append(random.randint(0,100))
print(list1)

data = open('Homework4/Task4.txt','w')
string = ''
for i in range (k-1,-1,-1):
    if i>1:
      string = str(list1[i]) + "x^" + str(i) + " + "
      data.writelines(string)
    elif i == 1:
        string = str(list1[i]) + "x" 
        data.writelines(string) 
    elif i < 1:
        string = " + " + str(list1[i]) 
        data.writelines(string)
string = " = 0 " 
data.writelines(string) 
data.close()
