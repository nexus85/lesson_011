from TOKEN import TOKEN
from telegram.ext import Updater


def main():
    """
    Минимальное тело 
    """
    mybot = Updater(token=TOKEN)
    mybot.start_polling()
    mybot.idle()

main()