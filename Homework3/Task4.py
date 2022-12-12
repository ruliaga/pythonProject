# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num = int(input('Введите целое десятичное число: '))
ls = []
def to_bi_sys (x):
    if x%2 > 0:
        ls.append('1')
    else:
        ls.append('0')
    if x>1:
        x = x//2
        to_bi_sys (x)
to_bi_sys (num)
str(ls.reverse())
bin = ''
for i in ls:
    bin = bin + i
print (f'Десятичное число {num} - двоичное число {bin}')

    