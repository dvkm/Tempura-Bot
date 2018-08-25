import telebot
from telebot import types

import traceback
import logging
import time

import config

from _thread import start_new_thread

logging.basicConfig(level=logging.INFO)

API_TOKEN = config.api_key
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hello, I am ShrimpTempuraBot.
If you need help with anything, uh... you're talking to the wrong bot.    
    """)


@bot.message_handler(regexp='OAO')
def oao_reply(message):
    username = "unknown"
    username = message.from_user.username
    if username is None:
        username = message.from_user.first_name

    reply = f'OAO {username} OAO'
    bot.send_message(chat_id=message.chat.id, text=reply, disable_notification=True)
    # bot.send_message()

@bot.message_handler()
def handle_messages(message):
    pass

if __name__ == "__main__":
    while True:
        try:
            bot.polling()
        except:
            traceback.print_exc()
            time.sleep(5)