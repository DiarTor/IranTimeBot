from telebot import TeleBot

from bot.handlers.start_handler import StartCommandHandler
from config.bot_token import main_token

bot = TeleBot(main_token)

bot.register_message_handler(StartCommandHandler().welcome_message, commands=['start'], pass_bot=True)

if __name__ == "__main__":
    bot.infinity_polling()
