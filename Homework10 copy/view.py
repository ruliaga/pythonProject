

def hallo():
    print('__________________________'
    'Добро пожаловать в игру "Конфеты"'
    '__________________________')
    player_name = input('Как ваше имя?\n')
    return player_name

def conf_num(name):
    conf = int(input(f'{name}, введите количество конфет, участвующих в игре: \n'))
    return conf

def message(message):
    print(message)

def player_motion(name):
    player_motion = int(input(f'{name}, сколько конфет вы забираете со стола?\n'
'Введите число от 1 до 28: \n'))
    return player_motion
