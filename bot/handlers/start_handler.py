from telebot import TeleBot
from telebot.types import Message, KeyboardButton, ReplyKeyboardMarkup

from languages.persian import handlers


class StartCommandHandler:
    """
    This Class Handle /start Command
    """

    def _generate_keyboard(self):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        button = KeyboardButton("📅 امروز چندمه؟")
        return markup.add(button)

    def welcome_message(self, msg: Message, bot: TeleBot):
        bot.send_message(chat_id=msg.chat.id, text=handlers.get('welcome'),
                         reply_markup=self._generate_keyboard())
