# -*- coding: utf-8 -*-
from pony.orm import *
from settings import DB_CONFIG

db = Database()
db.bind(**DB_CONFIG)


class UserData(db.Entity):
    """Состояние пользователя"""
    id_user = Required(str, unique=True)
    name_user = Required(str)
    email_user = Required(str)
    user_state = Required(str)

    

db.generate_mapping(create_tables=True)