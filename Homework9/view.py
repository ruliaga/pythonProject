import controller
import database


def hallo ():
    print(' _________________________________________')
    print('|Добро пожаловать в телефонный справочник.|')
    print(' ------------------------------------------')


def main_menu ():
    print('_____________________________________________')
    print('Выберите одно из следующих действий:')
    print('1 - просмотр телефонного справочника')
    print('2 - экспорт данных в txt\n3 - импорт данных из txt')
    print('4 - экспорт данных в csv\n5 - импорт данных из csv')
    print('6 - добавить контакт в телефонный справочник\n7 - удалить контакт из телефонного справочника')
    print('8 - завершение работы')
    select = int(input('Выбор: '))
    print('_____________________________________________')
    return select

def show_data ():
    row1 = ('№\tФамилия\t\tИмя\tНомер\t\tКомментарий')
    print(row1)
    data = database.database
    rows = ''
    for i,p in enumerate(data, start=1):
        print(i,*p,sep='\t')
        string = ''
        for j in p:
            string = string + ' ' + str(j)
        rows = rows + str(i) + '\t' + string + '\n'
    return row1 + "\n" + rows
        

def show_message(msg):
    print(msg)

def add_contact():
    print('Введите контакт !через пробел! в формате Фамилия/Имя/Номер телефона/Комментарий: ')
    person = input('Контакт: ').split(' ')
    return person

def delete_contact():
    print('Введите номер строки телефонного справочника, который желаете удалить.')
    del_num = int(input('Номер строки для удаления: '))
    return del_num


