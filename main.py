import telebot
from jdatetime import datetime
from telebot import types

import config

bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    itembtn = types.KeyboardButton('📅 امروز چندمه؟')
    markup.add(itembtn)
    bot.send_message(message.chat.id, "خوش آمدید! برای دریافت تاریخ امروز دکمه را فشار دهید.", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "📅 امروز چندمه؟")
def send_date(message):
    today_date = datetime.now().strftime("%Y/%m/%d")
    bot.send_message(message.chat.id, f"امروز مورخ {today_date} میباشد.")


bot.infinity_polling()
