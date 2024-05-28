from jdatetime import datetime
from telebot import TeleBot
from telebot.types import Message

from languages.persian import job


class DateAndTime:
    def _get_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        return current_time

    def _get_date(self):
        current_date = datetime.now().date().strftime("%Y/%M/%d")
        return current_date

    def proccess(self, msg: Message, bot: TeleBot):
        final_message = job.get("what_is_today").format(self._get_date())
        bot.send_message(chat_id=msg.chat.id, text=final_message)
