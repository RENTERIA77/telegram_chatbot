from lib2to3.pgen2 import token
from telegram.ext import Uptader, CommandHandler

def start(update, context):
    update.message.reply_text("Hola")


if __name__ =='__mai__':
    uptader = Uptader(token='5497756593:AAGctXoJJaYepmtATW-MXjD5dwlwXLUIXLY', use_context=True)
    dp = uptader.dispacher

    dp.add_handler(CommandHandler('start',start))
    
    uptader.start_polling()
    uptader.idle()