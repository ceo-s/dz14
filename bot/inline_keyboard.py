from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from demo_parser import parse_exact, parse_list, parse_main

def create_main_keyboard():
    buttons = dict(parse_main())
    keyboard_main = InlineKeyboardMarkup(row_width=1)
    for name, link in buttons.items():
        button = InlineKeyboardButton(text=name, callback_data=f"main#@#{name}#@#{link}")
        keyboard_main.add(button)
    return keyboard_main

def create_buttons(url):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Подробнее↓", url=url)
    markup.add(button)
    return markup
