from TOKEN import TOKEN
from telegram.ext import Updater, CommandHandler


def main():
    """
    Минимальное тело 
    """
    mybot = Updater(token=TOKEN)

    #Диспечер
    dp = mybot.dispatcher 

    #Обработка старт
    dp.add_handler(CommandHandler('start', greet_user))


    
    mybot.start_polling()
    mybot.idle()

def greet_user(bot, update):
    print('Вызван /start')


main()