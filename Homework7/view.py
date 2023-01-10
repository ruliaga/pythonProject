import controller
import database


def hallo ():
    print(' _________________________________________')
    print('|Добро пожаловать в телефонный справочник.|')
    print(' ------------------------------------------')


def main_menu ():
    print('_____________________________________________')
    print('Выберите одно из следующих действий:')
    print('1 - просмотр справочника')
    print('2 - экспорт данных в txt\n3 - импорт данных из txt')
    print('4 - экспорт данных в csv\n5 - импорт данных из csv')
    select = int(input('Выбор: '))
    print('_____________________________________________')
    return select

def show_data ():
    data = database.database
    for i in data:
        print(f'{"  ".join(i)}')

def show_export_txt():
    print('Данные телефонного справочника добавлены в файл txt.')

def show_export_csv():
    print('Данные телефонного справочника добавлены в файл csv.')

def show_import_txt():
    print('Данные телефонного справочника добавлены из файла txt.')

def show_import_csv():
    print('Данные телефонного справочника добавлены из файла csv.')