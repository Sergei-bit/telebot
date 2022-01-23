# -*- coding: utf-8 -*-

"""
Бот для Telegram
Use Python 3.9
"""

import telebot
import logging
from intents import INTENTS
from handlers import handler_name
from handlers import handler_email
from models import UserData
from pony.orm import db_session
from generate_ticket import create_ticket

try:
    import settings  # ваш токен Telegram
except ImportError:
    exit("DO cp settings.py.default settings.py and set token!")

BOT_LOGGING_PATH = "bot.log"


bot = telebot.TeleBot(token=settings.token)

log = logging.getLogger(name="bot")


class Storage:
    """хранилище"""

    def __init__(self):
        self.id_user = ""
        self.name_user = ""
        self.email_user = ""
        self.user_state = "step0"


storage_object = Storage()


@db_session
def create_table(cls):
    """создать_таблицу"""
    UserData(
        id_user=cls.id_user,
        name_user=cls.name_user,
        email_user=cls.email_user,
        user_state=cls.user_state,
    )


def configure_logging():
    """логирование"""
    file_hendler = logging.FileHandler(BOT_LOGGING_PATH)
    file_hendler.setFormatter(logging.Formatter(
        "%(asctime)s %(levelname)s %(message)s"))
    log.addHandler(file_hendler)
    log.setLevel(logging.DEBUG)
    file_hendler.setLevel(logging.DEBUG)


@bot.message_handler(commands=["start"])
def start_bot(message):
    """команда (старт бот)"""
    bot.send_message(message.chat.id, "Привет! Я телебот!")
    bot.send_message(message.chat.id, "Для помощи набери /help")
    log.info(
        f"содержание: {message.text} id_сообщения: {message.id} id_пользователя: {message.chat.id}")
    return message.text


@bot.message_handler(commands=["help"])
def help_bot(message):
    """команда (помошь)"""
    bot.send_message(
        message.chat.id, "Чтобы узнать дату введите: Дата\nЧтобы узнать место введите: Где\nЧтобы зарегистрироваться введите: /reg")
    log.info(
        f"содержание: {message.text} id_сообщения: {message.id} id_пользователя: {message.chat.id}")
    return message.text


@bot.message_handler(commands=["reg"])
def registration(message):
    """команда (регистрация)"""
    msg = bot.send_message(message.chat.id, "Введите ваше имя")
    bot.register_next_step_handler(msg, name_registration)
    return msg.text


@bot.message_handler(content_types=["text"])
def date_and_place_of_meeting(message):
    """дата и место встречи"""
    for intents in INTENTS:
        if message.text in intents["tockens"]:
            bot.send_message(message.chat.id, intents["answer"])
            log.info(
                f"содержание: {message.text} id_сообщения: {message.id} id_пользователя: {message.chat.id}")
    return message.text


def name_registration(message):
    """регистрация имени"""
    if handler_name(text=message.text):
        bot.send_message(message.chat.id, f"Ok {message.text}")
        msg = bot.send_message(message.chat.id, "Введите ваш email")
        bot.register_next_step_handler(msg, registration_email)
        log.info(
            f"содержание: {message.text} id_сообщения: {message.id} id_пользователя: {message.chat.id}")
        storage_object.id_user = str(message.id)
        storage_object.name_user = message.text
        storage_object.user_state = "step1"
        return message.text
    else:
        bot.send_message(message.chat.id, "Не правильное имя")
        log.info(
            f"содержание error: {message.text} id_сообщения: {message.id} id_пользователя: {message.chat.id}")


def registration_email(message):
    """регистрация емейла"""
    if handler_email(message.text):
        bot.send_message(message.chat.id, f"Ok {message.text}")
        log.info(
            f"содержание: {message.text} id_сообщения: {message.id} id_пользователя: {message.chat.id}")
        storage_object.email_user = message.text
        storage_object.user_state = "step2"
        create_table(storage_object)
        bot.send_photo(message.chat.id, create_ticket(
            storage_object.name_user, storage_object.email_user))
        return message.text
    else:
        bot.send_message(message.chat.id, "Не правильный email")
        log.info(
            f"содержание error: {message.text} id_сообщения: {message.id} id_пользователя: {message.chat.id}")


if __name__ == "__main__":
    configure_logging()
    bot.infinity_polling()
