from aiogram.types import Message, CallbackQuery, BotCommand
from aiogram.dispatcher.filters import IDFilter, Command, Text
from aiogram.dispatcher import Dispatcher

from inline_keyboard import create_main_keyboard, create_buttons
from demo_parser import parse_list

async def start(message: Message):
    await message.answer(text="Привет! Я - бот для парсинга.")

async def help(message: Message):
    await message.answer(text="Бла бла. То-то то-то!")

async def parse_main(message: Message):
    await message.answer(text="<b>Новости Санкт-Петербурга.</b>\nВыберите раздел!", parse_mode="HTML", reply_markup=create_main_keyboard())

async def parse_lists(call: CallbackQuery):
    name = call.data.split("#@#")[1]
    url = call.data.split("#@#")[2]
    await call.message.edit_reply_markup(reply_markup=None)
    lst = dict(parse_list(url=url))
    await call.message.edit_text(text=name)
    for name, link in lst.items():
        await call.message.answer(text=name, reply_markup=create_buttons(url = link))
        
    

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(parse_main, commands=['parse'])
    dp.register_callback_query_handler(parse_lists, Text(startswith="main"))