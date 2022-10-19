# Курсовой проект

bot_screenshot - скриншоты работы бота

font - шрифт

tests - тесты

ticket_template - заготовки для генерации билета

tickets - сохранение готового билета

generate_ticket.py -> create_ticket - создает и сохраняет билет

handlers.py -> handler_name - проверяет на корректность имя, handler_email - проверяет на корректность email

intents.py - ответы на вопросы

models.py - модели

settings.py.default - название бота, токкен, конфиг базы psql - вам нужно создать файл settings.py и добавить в него все содержимое.
если база не нужна закоментируйте функцию create_table() -> telebot_bot.py

telebot_bot.py - запуск бота.
