# Реализуйте алгоритм перемешивания списка 
# (shuffle использовать нельзя, другие методы из библиотеки random - можно)
from random import randint

string = input('Введите любое слово для формирования списка: ')
ls = []
for i in range (0, len(string)):
    ls.append(string[i]+'ути' + str(i))
print(f'список {ls} ----> ')
temp = ''
for i in range (0, len(ls)-1):
    random_num = randint(0, len(ls)-1)
    temp = ls[i] 
    ls[i] = ls[random_num]
    ls[random_num] = temp
print(f'перемешанный список {ls}')