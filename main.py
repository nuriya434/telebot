import telebot
import env

bot = telebot.TeleBot(env.BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello!!!")

@bot.message_handler(commands=['info'])
def info_bot(message):  # Добавьте параметр message, так как это стандартная практика в telebot
    bot.send_message(message.chat.id, "Это телеграм бот! \nТелеграм бот создан 03.12.2023")

bot.polling()
