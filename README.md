# Курсовой проект Skillbox 'Профессия Python-разработчик'

### 🎯 Цель проекта:

1. создаие простого эхо-бота
2. написать тесты
3. /start запуск бота и приветствие
4. /help бот должен выводить справку
5. бот должен регистрировать человека на конференцию
6. бот должен отвечать на произвольные вопросы, например: где, когда
7. бот должен сгенерировать билет на конференцию с данными пользователя и отправить билет пользователю


![билет](https://github.com/Sergei-bit/telebot/blob/master/tickets/tickets.png)


### 📂

> ➡️ bot_screenshot - скриншоты работы бота

> ➡️ font - шрифт

> ➡️ tests - тесты

> ➡️ ticket_template - заготовки для генерации билета

> ➡️ tickets - сохранение готового билета

> ➡️ generate_ticket.py -> create_ticket - создает и сохраняет билет

> ➡️ handlers.py -> handler_name - проверяет на корректность имя, handler_email - проверяет на корректность email

> ➡️ intents.py - ответы на вопросы

> ➡️ models.py - модели

> ➡️ settings.py.default - название бота, токкен, конфиг базы psql - вам нужно создать файл settings.py и добавить в    него все содержимое.
> если база не нужна закоментируйте функцию create_table() -> telebot_bot.py

> ➡️ telebot_bot.py - запуск бота.

![PyPI](https://img.shields.io/pypi/v/pyTelegramBotAPI?label=pyTelegramBotAPI)  ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django)
