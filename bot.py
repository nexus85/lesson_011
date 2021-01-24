from TOKEN import TOKEN
from telegram.ext import Updater, CommandHandler
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', lovel=logging.INFO, filename='bot.log')

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    # print(dir(bot))
    bot.message.reply_text(text)


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




main()