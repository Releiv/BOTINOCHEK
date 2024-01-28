from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

help_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Расписание"),
            KeyboardButton(text="Кто мы?")
        ],
        [
            KeyboardButton(text="Выход")
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True, selective=True
)

fraction = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Числитель"),
            KeyboardButton(text="Знаменатель")
        ],
        [
            KeyboardButton(text="Выход")
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True, selective=True
)

week = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Понедельник"),
            KeyboardButton(text="Вторник")
        ],
        [
            KeyboardButton(text="Среда"),
            KeyboardButton(text="Четверг")
        ],
        [
            KeyboardButton(text="Пятница")
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True, selective=True
)