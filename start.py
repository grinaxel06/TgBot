import telebot
from telebot import types

bot = telebot.TeleBot('5418375222:AAFImnnXCxewTxKM4d9RmRIAqhnQ-KrVfoQ')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Если тебя зовут Эльвира, то привет. Остальным - на выход', parse_mode='html')

bot.message_handler(commands=[''])
def start(message):
    bot.send_message(message.chat.id, 'Если тебя зовут Эльвира, то привет. Остальным - на выход', parse_mode='html')

print("Бот запущен")
bot.polling(none_stop=True)