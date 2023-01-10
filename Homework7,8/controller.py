import model
import view
import database

def start ():
    view.hallo()
    main_menu()



def main_menu ():
    while True:
        select = view.main_menu()
        if select == 1:
            view.show_data()
            main_menu()
        elif select == 2:
            model.export_txt(database.database)
            view.show_message('Данные телефонного справочника экспортированы в файл txt')
            main_menu()
        elif select == 3:
            model.import_txt()
            view.show_message('Данные телефонного справочника импортированы из файла txt')
            main_menu()
        elif select == 4:
            model.export_csv(database.database)
            view.show_message('Данные телефонного справочника экспортированы в файл csv')
            main_menu()
        elif select == 5:
            model.import_csv()
            view.show_message('Данные телефонного справочника импортированы из файла csv')
            main_menu()
        elif select == 6:
            person = view.add_contact()
            model.add_contact(person)
            view.show_message('Контакт добавлен в телефонную книгу.')
            main_menu()
        elif select == 7:
            del_num = view.delete_contact()
            model.delete_contact(del_num)
            view.show_message('Контакт удален из телефонной книги')
            main_menu()
        elif select == 8:
            view.show_message('Работа завершена. ')
        break