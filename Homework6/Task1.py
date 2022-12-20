# Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b), 
# возвращающая наибольший общий делитель (НОД) двух чисел.
#  Вычислите и напечатайте наибольший общий делитель для списка 
# натуральных чисел. Ввод чисел продолжается до ввода пустой строки.
import math

print ("Введите число и нажмите Enter. Для окончания введите путую строку. ")
ls = []
temp = ' '
while temp != '':
    num = input()
    ls.append(num)
    temp = num
del ls[-1]



def fun_gdc (ls):
    ls_gdc = []
    a = 0
    for i in range(0,len(ls)-1):
        gdc = math.gcd(int(ls[i]),int(ls[i+1]))
        ls_gdc.append(gdc)
    if len(ls_gdc)!=1:
        fun_gdc(ls_gdc)
    else:
        print(gdc)
    
    
fun_gdc(ls)
   


