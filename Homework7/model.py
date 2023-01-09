
def export_txt (database):
    data = open('Homework7/database.txt','w',encoding="UTF-8")
    ls = list(database)
    for i in ls:
        a = ' '.join(i)
        data.write(a + '\n')
    data.close()

    

def export_csv ():
    pass

def import_txt ():
    data = open('Homework7/database.txt','r',encoding='UTF-8')
    ls = list(data.readlines())
    print(ls)
    data.close()

def import_csv ():
    pass


