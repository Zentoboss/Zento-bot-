import telebot

bot = telebot.TeleBot("ВАШ_Т7651020708:AAE55lbMYpgBvNe82XLUnheBgWf1wleqchIОКЕН")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот.")

bot.polling()
