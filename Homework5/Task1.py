# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input('Введите текст: ').split(' ')
text = list(filter(lambda x: not 'абв' in x, text))
text = ' '.join(text)
print(text)