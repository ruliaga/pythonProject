import csv
import database

def export_txt (database):
    data = open('Homework7/database.txt','w',encoding="UTF-8")
    ls = list(database)
    for i in ls:
        a = ' '.join(i)
        data.write(a + '\n')
    data.close()

    

def export_csv (database):
    with open('Homework7/database.csv','w',newline='', encoding='UTF-8') as d:
        writer = csv.writer(d)
        writer.writerows(database)

def import_txt ():
    data = open('Homework7/database.txt','r',encoding='UTF-8')
    ls = list(map(lambda x: x.replace('\n', ''), data.readlines()))
    database_new = []
    for i in ls:
       a = i.split(' ')
       database_new.append(a)
    database.database = database_new
    data.close()

def import_csv ():
    with open('Homework7/database.csv','r', encoding='UTF-8') as d:
        reader = csv.reader(d, delimiter=',')
        database.database = list(reader)
        


