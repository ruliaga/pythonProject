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
        view.show_export_txt()
        main_menu()
    elif select == 3:
        model.import_txt()
        view.show_import_txt()
        main_menu()
    elif select == 4:
        model.export_csv(database.database)
        view.show_export_csv()
        main_menu()
    elif select == 5:
        model.import_csv()
        view.show_import_csv()
        main_menu()
