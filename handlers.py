# -*- coding: utf-8 -*-

import re

RE_NAME = re.compile(r"[a-zA-Z0-9_]")

RE_EMAIL = re.compile(r"\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b")


def handler_name(text):
    """получает имя пользователя"""
    match = re.match(RE_NAME, text)
    if match:
        return True
    else:
        return False


def handler_email(text):
    """получает емейл пользователя"""
    mathes = re.findall(RE_EMAIL, text)
    if len(mathes) > 0:
        return True
    else:
        return False
