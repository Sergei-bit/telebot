# -*- coding: utf-8 -*-
from unittest.mock import Mock, patch
import pytest
import unittest
from generate_ticket import create_ticket
from echo_bot import *

bot_obj = Mock()
bot_obj.text = "User"
bot_obj.message = "User"
bot_obj.chat.id = 1588938341


class TestBot(unittest.TestCase):

    def test_create_ticket(self):
        """создать билет"""

        with open("ticket_template/alex@mail.com.png", "rb") as avatar_file:
            avatar_mock = Mock()
            avatar_mock.content = avatar_file.read()

        with patch("requests.get", return_value=avatar_mock):
            ticket_file = create_ticket("Alex", "alex@mail.com")

        with open("tickets/tickets.png", "rb") as expecteed_file:
            expecteed_byts = expecteed_file.read()

        assert ticket_file.read() == expecteed_byts

    def test_start_bot(self):
        """старт бот"""
        bot_obj.text = "/start"
        assert start_bot(bot_obj) == "/start"

    def test_help_bot(self):
        """помощь"""
        bot_obj.text = "/help"
        assert help_bot(bot_obj) == "/help"

    def test_registration(self):
        """регистрация"""
        assert registration(bot_obj) == "Введите ваше имя"

    def test_date_and_place_of_meeting(self):
        """дата и место встречи"""
        assert type(date_and_place_of_meeting(bot_obj)) is str

    def test_name_registration(self):
        """регистрация имени"""
        bot_obj.text = "User"
        assert type(name_registration(bot_obj)) is str

    def test_registration_email(self):
        """регистрация емейла"""
        bot_obj.text = "User@user.com"
        assert type(registration_email(bot_obj)) is str


if __name__ == "__main__":
    unittest.main()

# python -m unittest
