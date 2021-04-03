from aiogram.types import Message, User
from aiogram.dispatcher.filters import CommandStart

from data.config import ADMINS_ID_LIST
from keyboards.main_keyboards import main_admin_keyboard
from keyboards.not_admin_keyboards import main_keyboard
from loader import dp
from utils.db_api.db_commands import DBCommands


db = DBCommands()


@dp.message_handler(CommandStart())
async def welcome_message(message: Message):
    # Запишем пользователя в базу
    id_user = await db.add_new_user()

    # Выполним функцию, которая отправит пользователю кнопки с доступными категориями
    if str(User.get_current().id) in ADMINS_ID_LIST:
        await message.answer(
            "Привет! Я бот-ассистент. \nВсе возможные действия есть в меню управления.",
            reply_markup=main_admin_keyboard
        )

    else:
        await message.answer(
            "Привет! Я бот-ассистент. \nС помощью меня ты сможешь посмотреть статистику по играм в колонизаторы.",
            reply_markup=main_keyboard
        )
