import telebot

bot = "6975787164:AAGor4fn6C2aVjPNB3YWPBV8FtV0zjx33gc"
bot = telebot.TeleBot(bot)


@bot.message_handler(commands=["start"])
def start(message):
    
    
    bot.send_message(message.chat.id, f'''
مرحبا بك ''')


print('bot run')
bot.polling()
