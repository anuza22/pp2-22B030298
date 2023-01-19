import telebot

bot = telebot.TeleBot("5830481540:AAEO4NvLEwg9an6dX2rBdfDWlx2mM5e4", parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello')

bot.polling(none_stop=True)
