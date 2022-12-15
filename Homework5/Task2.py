# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты 
# у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""



import random

mode = int(input('Выберете режим игры. 1 - Игра с человеком. 2 - Игра с ботом. Ответ: '))

if mode == 1:
    player1 = input('Введите имя первого игрока: ')
    player2 = input('Введите имя первого игрока: ')
    conf = int(input('Введите количество конфет, лежащих на столе: '))

    flag = random.choice([True,False])
    if flag == True:
        print(f'Первым ход делает {player1}!!!')
    else: 
        print(f'Первым ход делает {player2}!!!')


    def game (conf, flag):
        if flag == True:
            x = int(input(f'{player1}, сколько конфет вы забираете? Ответ: '))
            if x <= 28 and x >= 1:
                conf = conf - x
            else:
                print('Введите число от 1 до 28')
                game(conf, flag)   
        else: 
            x = int(input(f'{player2}, сколько конфет вы забираете? Ответ: '))
            if x <= 28 and x >= 1:
                conf = conf - x
            else:
                print('Введите число от 1 до 28')
                game(conf, flag)    
        if conf >= 1:
            flag = not flag
            print(f'На столе осталось {conf} конфет')
            game(conf, flag)
        else:
            if flag == True:
                print(f'Игра закончена! Победил {player1}')
            else:
                print(f'Игра закончена! Победил {player2}')
                
        


    game(conf, flag)

if mode == 2:
    player = input('Введите ваше имя: ')
    conf = int(input('Введите количество конфет, лежащих на столе: '))

    flag = random.choice([True,False])
    if flag == True:
        print(f'Вы делаете ход первым!!!')
    else: 
        print(f'Первым ход делает компьютер!!!')


    def game (conf, flag):
        if flag == True:
            x = int(input(f'{player}, сколько конфет вы забираете? Ответ: '))
            if x <= 28 and x >= 1:
                conf = conf - x
            else:
                print('Введите число от 1 до 28')
                game(conf, flag)   
        else: 
            if conf == 28:
                bot = 28
            elif conf ==30:
                bot = 1
            elif conf ==31:
                bot = 2 
            elif conf ==32:
                bot = 3
            elif conf ==33:
                bot = 4
            elif conf ==34:
                bot = 5
            else:
                bot = random.randint(1,28)
            conf = conf - bot
            print(f'Бот забирает со стола {bot} конфет. ')
              
        if conf >= 1:
            flag = not flag
            print(f'На столе осталось {conf} конфет')
            game(conf, flag)
        else:
            if flag == True:
                print(f'Игра закончена! Вы победили!!!')
            else:
                print(f'Игра закончена! Победил компьютер.')
                
        


game(conf, flag)