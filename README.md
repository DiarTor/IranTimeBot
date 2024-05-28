# Today Date Bot

Today Date Bot is a simple Telegram bot that sends the current date when you press a button.

## Features

- Displays the current date in a user-friendly format.
- Easy to use with a single button press.

## Getting Started

These instructions will help you set up and run the bot on your local machine.

### Prerequisites

- Python 3.6+
- A Telegram account
- A Telegram bot token (You can get this from the [BotFather](https://core.telegram.org/bots#botfather))

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/DiarTor/dailytimeir.git
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `config.py` file and add your bot token:

    ```python
    # config.py
    BOT_TOKEN = 'your-telegram-bot-token'
    ```

### Running the Bot

Run the bot using the following command:

```bash
python main.py
```

### Usage

1. Start a chat with your bot on Telegram.
2. Press the button labeled "امروز چندمه؟ 📅".
3. The bot will respond with the current date.

## Code Overview

### `bot.py`

This is the main script that runs the bot. It sets up the bot, defines the command handlers, and starts polling for updates.

```python
import telebot
from jdatetime import datetime
from telebot import types

import config

bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    itembtn = types.KeyboardButton('امروز چندمه؟ 📅')
    markup.add(itembtn)
    bot.send_message(message.chat.id, "خوش آمدید! برای دریافت تاریخ امروز دکمه را فشار دهید.", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "امروز چندمه؟ 📅")
def send_date(message):
    today_date = datetime.now().strftime("%Y/%m/%d")
    bot.send_message(message.chat.id, f"امروز مورخ {today_date} میباشد.")


bot.infinity_polling()
```

## Built With

- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) - A Python wrapper for the Telegram Bot API

## Contributing

Feel free to submit issues and enhancement requests.


## Acknowledgments

- Thanks to the [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) contributors for their excellent library.

---