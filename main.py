import requests
import telebot

token = "6975787164:AAEFyZnn_XtrsEYpGOswOMV4TU_lEJ7PUhA"

bot = telebot.TeleBot(token, num_threads=100, skip_pending=True, parse_mode="markdown", disable_web_page_preview=True)

@bot.message_handler(commands=["start"])
def welcome(msg):
    bot.reply_to(msg, "*أهلا بك عزيزي في بوت أيبي انفو\nفقط أرسل الايبي\n------   -------   ------\nتم البرمجة بواسطة => @susiraq*")

@bot.message_handler(func=lambda message: True)
def send(msg):
    ip = msg.text
    rq = requests.get(f'http://ip-api.com/json/{ip}?fields=status,message,continent,country,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,proxy,query')
    iss = rq.json()["status"]
    if iss == "success":
        qara = rq.json()["continent"]
        country = rq.json()["country"]
        region = rq.json()["regionName"]
        city = rq.json()["city"]
        district = rq.json()["district"]
        zip = rq.json()["zip"]
        lat = rq.json()["lat"]
        lan = rq.json()["lon"]
        ah = f"{lan} {lat}"
        timezone = rq.json()["timezone"]
        currency = rq.json()["currency"]
        org = rq.json()["org"]
        proxy = str(rq.json()["proxy"])
        ip = rq.json()["query"]
        if proxy == "True":
            what = proxy.replace("True", "بروكسي")
        elif proxy == "False":
            what = proxy.replace("False", "ايبي حقيقي")
        bot.reply_to(msg, f'''*- معلومات الايبي* `{ip}`:
*القارة: {qara}.
الدولة: {country}.
المحافظة: {region}.
الناحية: {city}.
الرمز البريدي:* `{zip}`.
*خطوط الطول و العرض:* `{ah}`.
*المنطقة الزمنية: {timezone}.
عملة البلد: {currency}.
شركة الإتصالات: {org}.
ايبي حقيقي لو بروكسي: {what}.*
[تابعنا للمزيد](t.me/teamon404)''')
    else:
        bot.reply_to(msg, "*حدث خطأ\nحاول مجددا لاحقا*")

print("-- Bot Started...")
bot.infinity_polling()