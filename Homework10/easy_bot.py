from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from random import randint
import controller
import view
import model
import main






bot_token = '5776016230:AAELzz05vWdlfBKoq0MM8Axz-79hagshz6Y'
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher
conf = 0

def menu(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет. Это игра про конфеты. "
    "/start - начало игры\n"
    "/exit - выйти из приложения")


def exit (update, context):
    context.bot.send_message(update.effective_chat.id, "До встречи!")


def play(update, context):
    update.message.reply_text("Как вас зовут?\n")
    
    return 1



def stop(update, context):
    
    return ConversationHandler.END

def response_play1(update, context):
    global player 
    player = update.message.text
    update.message.reply_text(f'{player}, введите количество конфет, лежащих на столе.')
    return 2

def response_play2(update, context):
    conf = int(update.message.text)
    main.conf = conf
    update.message.reply_text(f'Итак, на столе лежит {conf} конфет.')
    flag = model.flag_choice() 
    if flag == True:
        update.message.reply_text('Вы делаете ход первым\n')
        update.message.reply_text('Сколько конфет вы берёте со стола?\n')
        return 3 
    else: 
        update.message.reply_text('Первым ходит компьютер. Ок?')
        return 4
    

def response_play3(update, context):
    player_motion = int(update.message.text)
    if player_motion <= 28 and player_motion >= 1:
        main.conf = main.conf - player_motion
        if main.conf >=1:
            update.message.reply_text(f'На столе осталось лежать {main.conf} конфет.'
            'Теперь ход компьютера. Ок?')
            return 4
        else:
            update.message.reply_text('На столе не осталось конфет. Вы победили!!!')
    else:
        update.message.reply_text('Ошибка. Введите число от 1 до 28.\n')
        return 3
      

def response_play4(update, context):
    computer_motion = model.computer_motion(main.conf)
    main.conf = main.conf - computer_motion
    if main.conf >=1:
        update.message.reply_text(f'Компьютер забирает со стола {computer_motion} конфет')
        update.message.reply_text(f'На столе осталось лежать {main.conf} конфет.'
        'Теперь ваш ход.')
        return 3
    else:
        update.message.reply_text(f'Компьютер забирает со стола {computer_motion} конфет')
        update.message.reply_text('На столе не осталось конфет. Победил компьютер.')

    
start_handler = ConversationHandler(
entry_points=[CommandHandler('start', play)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, response_play1)],
        2: [MessageHandler(Filters.text & ~Filters.command, response_play2)],
        3: [MessageHandler(Filters.text & ~Filters.command, response_play3)],
        4: [MessageHandler(Filters.text & ~Filters.command, response_play4)],    
            },
            

    fallbacks=[CommandHandler('stop', stop)]
    )



menu_handler = CommandHandler('menu', menu)
exit_handler = CommandHandler('exit', exit)


dispatcher.add_handler(menu_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(exit_handler)


updater.start_polling()
updater.idle()