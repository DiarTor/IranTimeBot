from telebot import TeleBot
from telebot.types import Message

from bot.job.datetime import DateAndTime


class MessageHandler:

    def handle_message(self, msg: Message, bot: TeleBot):
        if msg.text == "📅 امروز چندمه؟":
            DateAndTime().proccess(msg, bot)
