from TOKEN import TOKEN
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s - %(name)s', level=logging.INFO, filename='bot.log')

def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    # print(dir(bot))
    bot.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = bot.message.text
    logging.info(user_text)
    bot.message.reply_text(user_text)

def main():

    logging.info('Бот запускается')
    """
    Минимальное тело 
    """
    mybot = Updater(token=TOKEN)

    #Диспечер
    dp = mybot.dispatcher 

    #Обработка старт
    dp.add_handler(CommandHandler('start', greet_user))

    #Обработка сообщиний
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    
    mybot.start_polling()
    mybot.idle()




main()