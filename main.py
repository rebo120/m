
import telebot
import requests
from telebot import types


token1 = "6677219441:AAFG-24eyUqR5-V8DCFbf9q3lz0LnR1uUxY"
bot = telebot.TeleBot(token1)

ah = types.InlineKeyboardButton("قناة المطور", url=f"https://t.me/DevMohaumn")
@bot.message_handler(commands=["start"])
def start(message):
	MOHAUMN = types.InlineKeyboardMarkup()
	MOHAUMN.row_width = 2
	MOHAUMN.add(ah)
	name = message.from_user.first_name
	bot.reply_to(message,f"""
    *مرحبا بك {message.from_user.first_name} في بوت تحميل من تيك توك ارسل الرابط وانتظر 💿*""", parse_mode='markdown', reply_markup=MOHAUMN)
	
@bot.message_handler(func=lambda MOHAUMN:True)
def Url(message):
		try:
			msgg = bot.send_message(message.chat.id, "*جاري التحميل ...*",parse_mode="markdown")
			msg = message.text
			url = requests.get(f'https://tikwm.com/api/?url={msg}').json()
			music = url['data']['music']
			region = url['data']['region']
			tit = url['data']['title']
			vid = url['data']['play']
			ava = url['data']['author']['avatar']
			##
			name = url['data']['music_info']['author']
			time = url['data']['duration']
			sh = url['data']['share_count']
			com = url['data']['comment_count']
			wat = url['data']['play_count']
			bot.delete_message(chat_id=message.chat.id, message_id=msgg.message_id)
			btn1 = types.InlineKeyboardButton(text='جلب معلومات الحساب', callback_data='check')
			am = types.InlineKeyboardButton("قناة المطور", url=f"https://t.me/DevMohaumn")
			bro = types.InlineKeyboardMarkup()
			bro.row_width = 2
			bro.add(btn1)
			@bot.callback_query_handler(func=lambda call: True)
			def ip(call):
				bot.send_photo(message.chat.id,ava,caption=f'- اسم الحساب : *{name}*\n - دوله الحساب : *{region}*\n\n- عدد مرات المشاهدة : *{wat}*\n- عدد التعليقات : *{com}*\n- عدد مرات المشاركة : *{sh}*\n- طول الفيديو : *{time}*',parse_mode="markdown")
			
			
			bot.send_video(message.chat.id,vid, caption=f"{tit}", reply_markup=bro)
		except:
			pass
			bot.delete_message(chat_id=message.chat.id, message_id=msgg.message_id)
			bot.reply_to(message,'error );')


print('RUN')

bot.infinity_polling()



