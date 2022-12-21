# Орел и решка
# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". 
# Буква "О" – соответствует выпадению Орла, а буква "Р" – 
# соответствует выпадению Решки. 
# Напишите программу, которая подсчитывает наибольшее количество подряд 
# выпавших Решек.
# Формат входных данных:
# На вход программе подается строка текста, состоящая из букв русского 
# алфавита "О" и "Р".
# Формат выходных данных:
# Программа должна вывести наибольшее количество подряд выпавших Решек.
# Примечание. Если выпавших Решек нет, то необходимо вывести число 0.
# Входные данные Выходные данные
# ОРРОРОРООРРРО 3
# ООООООРРРОРОРРРРРРР 7
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР 31

string = [i for i in input('Введите последовательность из букв О и Р: ')]
counter = 0
total = 0
for i in range(0,len(string)-1):
    if string[i] == 'Р':
        counter = counter + 1
    else: 
        if counter > total:
         total = counter
         counter = 0
print(f'{"".join(string)} --> {total}')

