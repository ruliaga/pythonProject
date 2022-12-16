# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

answer = int(input('Какую операцию вы хотите совершить. 1 - сжатие, 2 - восстановление. Ответ: '))



def compression():

    data = open('Homework5/data.txt', 'r')
    ls = list(data.readline())
    data.close()
    ls_new = []
    count = 1
    for i in range(0, len(ls)-1):
        if ls[i] == ls[i+1]:
            count = count + 1
        else:
            ls_new.append(str(count)+ls[i-1])
            count = 1
    ls_new.append(str(count)+ls[-1])

    result = open('Homework5/result.txt','w')
    result.writelines(i for i in ls_new)
    result.close()
    print('Сжатие завершено. Проверьте файл result.txt')


def recovery():

    result = open('Homework5/result.txt', 'r')
    ls = list(result.readline())
    result.close()
    temp = ''
    data_string = ''
    ls_new = []
    for i in range (0, len(ls)-1):
        if ls[i].isdigit() == True:
            temp = temp + ls[i]
        elif ls[i].isdigit() == False:
            data_string = data_string + int(temp)*ls[i]
            temp = ''
    data_string = data_string + int(temp)*ls[-1]
            
    data = open('Homework5/data.txt', 'w')
    data.writelines(data_string)
    data.close()
    print('Восстановление завершено. Проверьте файл data.txt')




if answer == 1:
        compression()
elif answer == 2:
    recovery()
else:
    print("Неправильный ввод. Введите 1 или 2")
        
    



