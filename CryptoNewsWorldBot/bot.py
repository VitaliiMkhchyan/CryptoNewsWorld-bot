""" Телеграм бот """

import time
from typing import Any
import telebot
from loguru import logger
from config import config
import parser

bot: telebot.TeleBot = telebot.TeleBot(config.BOT_TOKEN)

logger.debug("Запуск бота")


@bot.message_handler(commands=["start"])
def start(message):
    title_cryptonews: Any = None
    while True:
        data: dict = parser.get_news()
        text: str = data["date"] + " назад" + "\n" + data["title"] + "\n\n" + data["content"] + "\n\n" + data["full_url"]

        if title_cryptonews != data["title"]:
            if len(text) > 4096:
                len_text: int = len(text) + 1
                part_1: str = text[0:len_text // 2]
                part_2: str = text[len_text // 2:]

                bot.send_message(message.chat.id, part_1)
                bot.send_message(message.chat.id, part_2)
            else:
                bot.send_message(message.chat.id, text)

            title_cryptonews: str = data["title"]
        time.sleep(config.TIMEOUT_GET_DATA)
