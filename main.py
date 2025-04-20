import telebot

bot = telebot.TeleBot("7651020708:AAE55lbMYpgBvNe82XLUnheBgWf1wleqchI")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот.")

bot.polling()
