import model
import view
import database

def start ():
    view.hallo()
    main_menu()



def main_menu ():
    select = view.main_menu()
    if select == 1:
        view.show_data()
        main_menu()
    elif select == 2:
        model.export_txt(database.database)
        print('Данные телефонного справочника добавлены в файл txt.')
        main_menu()
    elif select == 3:
        model.import_txt()
        print('Данные телефонного справочника добавлены из файла txt.')
        main_menu()
    elif select == 4:
        model.export_csv(database.database)
        print('Данные телефонного справочника добавлены в файл csv.')
        main_menu()
    elif select == 5:
        model.import_csv()
        print('Данные телефонного справочника добавлены из файла csv.')
        main_menu()
