"""
11/01/2023

"""

from transliterate import to_cyrillic, to_latin
import telebot
#text = input("Enter your letter : ")

TOKEN = '5707184085:AAHFMIyvU7SkDa_9QAlyKn7jXVB9FxHBBmo'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    answer = "Hi, how are you doing?"
    answer += "\nEnter your letter : "
    bot.reply_to(message=message, text=answer)

@bot.message_handler(func = lambda message : True)
def echo_all(message):
    msg = message.text
# if text.isascii():
#     print(to_cyrillic(text))
# else:
#     print(to_latin(text))
    answer = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, answer(msg))

bot.polling()



