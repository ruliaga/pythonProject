from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from random import randint
import controller
import view
import model




bot_token = '5776016230:AAELzz05vWdlfBKoq0MM8Axz-79hagshz6Y'
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher


def menu(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет. Это игра про конфеты. "
    "/start - начало игры\n"
    "/exit - выйти из приложения")


def exit (update, context):
    context.bot.send_message(update.effective_chat.id, "До встречи!")



def start (update, context):
    update.message.reply_text("Как вас зовут?\n")
    
    return 1

def stop(update, context):
    
    return ConversationHandler.END

def response_start(update, context):
    player = update.message.text
    conf = view.conf_num(player)
    update.message.reply_text(f'Итак, на столе лежит {conf} конфет.')
        

    return ConversationHandler.END


    
start_handler = ConversationHandler(
entry_points=[CommandHandler('start', start)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, response_start)],
            
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