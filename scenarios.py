# -*- coding: utf-8 -*-

SCENARIOS = {
    "registration": {
        "first_step": "step1",
        "steps": {
            "step1": {
                "text": "Чтобы зарегистрироваться, введите ваше имя. Оно будет написанно на вашем бейджике.",
                "failure_text": "Имя должно состоять из 3-30 букв и дефиса. Попробуйте еще раз",
                "handler": "handle_email",
                "next_step": "step2",
            },
            "step2": {
                "text": "Введите email . Мы отправим на него все данные.",
                "failure_text": "Имя должно состоять из 3-30 букв и дефиса. Попробуйте еще раз",
                "handler": "handle_email",
                "next_step": "step3",
            },
            "step3": {
                "text": "Спасибо за регестрацию, {name}! Мы отправили на {email} билет, распечатайте его.",
                "failure_text": None,
                "handler": None,
                "next_step": None,
            },
        }
    }
}

DEFAULT_ANSWER = """
Не знаю как ответить. 
Могу сказать когда и где пройдет конференция, а также зарегистрировать вас. 
Просто спросите.
"""
