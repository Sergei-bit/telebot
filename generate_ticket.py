# -*- coding: utf-8 -*-
import requests
from PIL import Image, ImageDraw, ImageFont
from intents import INTENTS
from io import BytesIO

TITLE = "Skillbox Conf"
TICKET = "Билет на конфиренцию"

SAMPLE = Image.open("ticket_template/skillbox_fon.jpg").convert("RGBA")
FNT = ImageFont.truetype("font/ofont.ru_Kitsch.ttf" ,20)

COLOR = (0, 0, 0, 255)
COLOR_AVATAR = (0, 255, 179, 100)

TITLE_OFFSET = (450, 260)
TICKET_OFFSET = (400, 290)
INTENTS_OFFSET_1 = (250, 360)
INTENTS_OFFSET_2 = (100, 390)
NAME_OFFSET = (690, 460)
EMAIL_OFFSET = (690, 690)

AVATAR_SIZE = 250
AVATAR_OFFSET = (680, 460)


def create_ticket(name, email):
    """создать билет"""

    draw_obj = ImageDraw.Draw(SAMPLE)
    draw_obj.text(TITLE_OFFSET, TITLE, font=FNT, fill=COLOR)
    draw_obj.text(TICKET_OFFSET, TICKET, font=FNT, fill=COLOR)
    draw_obj.text(INTENTS_OFFSET_1, INTENTS[1]["answer"], font=FNT, fill=COLOR)
    draw_obj.text(INTENTS_OFFSET_2, INTENTS[0]["answer"], font=FNT, fill=COLOR)

    response = requests.get(
        f"https://avatars.dicebear.com/api/micah/{email}.png?size={AVATAR_SIZE}")
    avatar_file_like = BytesIO(response.content)
    avatar = Image.open(avatar_file_like)
    SAMPLE.paste(avatar, AVATAR_OFFSET)

    draw_obj.text(NAME_OFFSET, name, font=FNT, fill=COLOR_AVATAR)
    draw_obj.text(EMAIL_OFFSET, email, font=FNT, fill=COLOR_AVATAR)

    with open("tickets/tickets.png", "wb") as f:
        SAMPLE.save(f, "png")

    temp_file = BytesIO()
    SAMPLE.save(temp_file, "png")
    temp_file.seek(0)

    return temp_file
