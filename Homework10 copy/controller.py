import model
import view



def start():
    global player
    global conf
    player = view.hallo()
    conf = view.conf_num(player)
    game()

def game():
    flag = model.flag_choice()
    if flag == True:
        view.message('Вы делаете ход первым\n')
        player_hod(conf)
    else: 
        view.message('Первым ходит компьютер\n')
        computer_hod(conf)
        
    
def player_hod(conf):
    player_motion = view.player_motion(player)
    if player_motion <= 28 and player_motion >= 1:
        conf = conf - player_motion
        if conf >=1:
            view.message(f'На столе осталось лежать {conf} конфет.'
            'Теперь ход компьютера.')
            computer_hod(conf)
        else:
            view.message('На столе не осталось конфет. Вы победили!!!')
    else:
        view.message('Ошибка. Введите число от 1 до 28.\n')
        player_hod(conf)

def computer_hod(conf):
    computer_motion = model.computer_motion(conf)
    conf = conf - computer_motion
    if conf >=1:
        view.message(f'Компьютер забирает со стола {computer_motion} конфет')
        view.message(f'На столе осталось лежать {conf} конфет.'
        'Теперь ваш ход.')
        player_hod(conf)
    else:
        view.message('На столе не осталось конфет. Победил компьютер.')