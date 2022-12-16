# Создайте программу для игры в ""Крестики-нолики""
import random

player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя первого игрока: ')
flag = random.choice([True,False])
if flag == True:
    print(f'Первым ход делает {player1}!!!')
elif flag == False: 
    print(f'Первым ход делает {player2}!!!')


field = [[1,2,3],[4,5,6],[7,8,9]]

slovar = {1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0),
5: (1,1), 6: (1,2), 7: (2,0), 8: (2,1), 9: (2,2)}

def chk_win (field):
    win_coord = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
    for row in win_coord:
        result = []
        for elem in row:
            x, y = slovar[elem]
            result.append(field [x][y])
        if result[0]==result[1]==result[2]:
            return True
            break
        else:
            continue
    return False



def game (flag):
    print(f'{field[0]}\n{field[1]}\n{field[2]}')
    if flag == True:
        hod = int(input(f'{player1}, ваш ход. Выберите незанятую позицию от 1 до 9. Ответ: '))
        if hod <= 9 and hod >=1:
                x, y = slovar[hod]
                if field [x][y] !='X' and field [x][y] !='O':
                    field [x][y] = 'X' 
                else:
                    print('Позиция занята. Выберите другую!')
                    game(flag)
        else:
                print('Введите число от 1 до 9')
                game(flag)   
    elif flag == False: 
            hod = int(input(f'{player2}, ваш ход. Выберите незанятую позицию от 1 до 9. Ответ: '))
            if hod <= 9 and hod >= 1:
                x, y = slovar[hod]
                if field [x][y] !='X' and field [x][y] !='O':
                    field [x][y] = 'O' 
                else:
                    print('Позиция занята. Выберите другую!')
                    game(flag)
            else:
                print('Введите число от 1 до 9')
                game(flag)
    chek = False 
    chek = chk_win(field)
    if chek == False:
        flag = not flag 
        game(flag)  
    else: 
        if flag == True:
            print(f'{field[0]}\n{field[1]}\n{field[2]}')
            print(f"Победил {player1}")
        else:
            print(f'{field[0]}\n{field[1]}\n{field[2]}')
            print(f"Победил {player2}")

game(flag)
