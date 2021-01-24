from settings import TOKEN
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s - %(name)s', level=logging.INFO, filename='bot.log')

def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    # print(dir(bot))
    bot.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = bot.message.text
    # logging.info(f'Пользователь написал: {user_text}')
    logging.info('User, %s, Chat id, %s, Message: %s', bot.message.chat.username, 
    bot.message.chat.id, 
    bot.message.text, 
    )
    bot.message.reply_text('Привет {}!, Как дела? '.format(bot.message.chat.first_name))
    print(bot.message)
    # bot.message.reply_text()
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