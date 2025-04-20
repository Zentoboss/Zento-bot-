import telebot

bot = telebot.TeleBot("ВАШ_7651020708:AAE55lbMYpgBvNe82XLUnheBgWf1wleqchIТОКЕН")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я ZentoBot!")

bot.polling()
