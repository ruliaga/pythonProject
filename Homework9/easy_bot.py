from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from random import randint
from view import show_data
from controller import find_num
from database import database
from model import add_contact, delete_contact


bot_token = '5776016230:AAELzz05vWdlfBKoq0MM8Axz-79hagshz6Y'
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher


def menu(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет. Я бот - телефонный справочник. "
    "Вот, что я умею:\n"
    "/sprav - показать телефонный справочник\n"
    "/add - добавить контакт\n"
    "/del - удалить контакт\n"
    "/find - найти номер телефона по фамилии\n"
    "/exit - выйти из приложения")


def exit (update, context):
    context.bot.send_message(update.effective_chat.id, "До встречи!")


def sprav (update, context):
    context.bot.send_message(update.effective_chat.id, show_data())
    context.bot.send_message(update.effective_chat.id, "Для выхода в главное меню нажмите /menu")

def add (update, context):
    update.message.reply_text("Для добавления в телефонный справочник "
        "введите данные контакта !через пробел! в формате Фамилия/Имя/Номер телефона/Комментарий")
    return 1
    



def delete (update, context):
    update.message.reply_text("Для удаления контакта введите номер строки, "
    "которую желаете удалить: ")
        
    return 1


def find (update, context):
    update.message.reply_text("Для поиска номера введите фамилию контакта\n")
    
    return 1

def stop(update, context):
    
    return ConversationHandler.END

def response_find(update, context):
    surname = update.message.text
    answer = find_num(database, surname)
    update.message.reply_text(answer)
    update.message.reply_text("Введите номер контакта\n"
    "Для выхода в главное меню нажмите /menu\n ")
    

    return

def response_add(update, context):
    person = update.message.text
    person = str(person).split(' ')
    add_contact(person)
    update.message.reply_text("Контакт добавлен в телефонный справочник\n"
    "Для выхода в главное меню нажмите /menu \n")

    return ConversationHandler.END
    
def response_del(update, context):
    num_str = update.message.text
    delete_contact(int(num_str))
    update.message.reply_text(f"Контакт {num_str} удален из телефонного справочника\n"
    "Для выхода в главное меню нажмите /menu \n")

    return ConversationHandler.END



conv_handler = ConversationHandler(
entry_points=[CommandHandler('find', find)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, response_find)],
            
            },

    fallbacks=[CommandHandler('stop', stop)]
    )

add_handler = ConversationHandler(
entry_points=[CommandHandler('add', add)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, response_add)],
            
            },

    fallbacks=[CommandHandler('stop', stop)]
    )

del_handler = ConversationHandler(
entry_points=[CommandHandler('del', delete)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, response_del)],
            
            },

    fallbacks=[CommandHandler('stop', stop)]
    )

menu_handler = CommandHandler('menu', menu)
sprav_handler = CommandHandler('sprav', sprav)
exit_handler = CommandHandler('exit', exit)

dispatcher.add_handler(menu_handler)
dispatcher.add_handler(sprav_handler)
dispatcher.add_handler(exit_handler)

dispatcher.add_handler(conv_handler)
dispatcher.add_handler(add_handler)
dispatcher.add_handler(del_handler)
updater.start_polling()
updater.idle()