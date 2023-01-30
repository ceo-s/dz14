from aiogram import Dispatcher, Bot, asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token="5720374898:AAF_Xt9OMLwURvg6Na9jLWimdvP4bsterfc")
dp = Dispatcher(bot=bot, loop=asyncio.new_event_loop(), storage=MemoryStorage())