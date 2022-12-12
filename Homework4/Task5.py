# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

data1 = open("Homework4/data1.txt", 'r')
str1 = data1.readline()
data1.close()
data2 = open("Homework4/data2.txt", 'r')
str2 = data2.readline()
data2.close()

str1 = str1 [:-3]
str1 = str1.split('+')
str1new = []
for i in range(0,len(str1)-1):
    temp = str1[i].split("x")
    str1new.append(temp[0])
str1new.append(str1[-1])
str1new.reverse()

str2 = str2 [:-3]
str2 = str2.split('+')
str2new = []
for i in range(0,len(str2)-1):
    temp = str2[i].split("x")
    str2new.append(temp[0])
str2new.append(str2[-1])
str2new.reverse()

str_result = str1new
for i in range(0, max(len(str1new),len(str2new))-1):
       str_result[i] = int(str_result[i])+int(str2new[i])

for i in range(len(str_result)-1,-1,-1):
    if i>1:
        print(f'{str_result[i]}x^{i} + ',end='')
    elif i == 1:
       print(f'{str_result[i]}x',end='')
    elif i < 1:
       print(f' + {str_result[i]}',end='')

print(' = 0')


        
        

    



