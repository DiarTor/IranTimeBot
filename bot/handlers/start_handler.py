from telebot import TeleBot
from telebot.types import Message

from languages.persian import start_command_texts


class StartCommandHandler:
    """
    This Class Handle /start Command
    """

    def welcome_message(self, msg: Message, bot: TeleBot):
        bot.send_message(chat_id=msg.chat.id, text=start_command_texts.get('welcome'))
