from aiogram import executor
from bot import dp
from aiogram.types import BotCommand
from handlers import register_handlers

async def set_comm(dp):
    await dp.bot.set_my_commands([BotCommand("start", "Старт"), BotCommand("help", "Помощь"), BotCommand("parse", "Парсинг новостей GAZETA SPb")])

if __name__ == "__main__":
  
    register_handlers(dp=dp)
    executor.start_polling(dp, on_startup=set_comm)