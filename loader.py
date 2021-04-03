import logging

from aiogram import Bot, Dispatcher, types

from data import config
from utils.db_api.database import create_pool


logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.INFO,
)

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

db = dp.loop.run_until_complete(create_pool())
