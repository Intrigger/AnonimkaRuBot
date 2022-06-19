import telebot

bot = telebot.TeleBot("5509343879:AAEInHGKgWXr0Y1xA9HHMEgIXTXoyvOkMKk", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, "Hello, your id is {}".format(message.from_user.id))


bot.infinity_polling()
