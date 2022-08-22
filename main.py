import telebot
from decouple import config


BOT_TOKEN = config("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start","help"])
def start(message):
    bot.send_message(message.chat.id," بسم الله الرحمن الرحيم\n\n  Welcome to ABTKR bot ")



bot.polling()
