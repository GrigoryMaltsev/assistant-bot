from aiogram.dispatcher.filters import Text
from aiogram.types import Message, User

from keyboards.cats_keyboards import main_cats_keyboard, CATS_HANDLERS
from keyboards.catan_keyboard import main_catan_keyboard, winner_catan_choose, CATAN_HANDLERS
from keyboards.main_keyboards import main_admin_keyboard, MAIN_ADMIN_HANDLERS
from keyboards.not_admin_keyboards import main_keyboard, MAIN_HANDLERS, CATAN_PLAYERS
from loader import dp
from utils.db_api.db_commands import DBCommands
from data.config import ADMINS_DICT, ADMINS_ID_LIST


db = DBCommands()


# Пробуем показать другую клавиатуру после выбора категории
@dp.message_handler(Text(equals=[MAIN_ADMIN_HANDLERS["cats"], MAIN_ADMIN_HANDLERS["catan"]]))
async def show_categories_keyboard(message: Message):
    if message.text == MAIN_ADMIN_HANDLERS["cats"]:
        full_info = await db.get_info_cats()
        await message.answer(
            "<b>Текущая статиктика: \n</b>"
            f"{full_info[1].get('user_name')}: {full_info[1].get('amount_cleaning')} ({full_info[1].get('last_date_cleaning').strftime('%H:%M:%S %d.%m')}) \n"
            f"{full_info[0].get('user_name')}: {full_info[0].get('amount_cleaning')} ({full_info[0].get('last_date_cleaning').strftime('%H:%M:%S %d.%m')})",
            reply_markup=main_cats_keyboard
        )
    elif message.text == MAIN_ADMIN_HANDLERS["catan"]:
        player_0_info = await db.get_winners_catan(year=2021, winner_game=CATAN_HANDLERS['players'][0])
        player_1_info = await db.get_winners_catan(year=2021, winner_game=CATAN_HANDLERS['players'][1])
        player_2_info = await db.get_winners_catan(year=2021, winner_game=CATAN_HANDLERS['players'][2])
        player_3_info = await db.get_winners_catan(year=2021, winner_game=CATAN_HANDLERS['players'][3])
        await message.answer(
            "<b>Результаты за 2021 год: \n</b>"
            f"{CATAN_HANDLERS['players'][0]}: {player_0_info} \n"
            f"{CATAN_HANDLERS['players'][1]}: {player_1_info} \n"
            f"{CATAN_HANDLERS['players'][2]}: {player_2_info} \n"
            f"{CATAN_HANDLERS['players'][3]}: {player_3_info}",
            reply_markup=main_catan_keyboard
        )
    else:
        await message.answer(
            "Кажется, меня пытаются сломать. Пожалуйста, не надо!"
        )


# Меню не для админов
@dp.message_handler(Text(equals=[MAIN_HANDLERS["stats2021"], MAIN_HANDLERS["statsAll"]]))
async def not_admin_actions(message: Message):
    player_0_info = await db.get_winners_catan(year=2021, winner_game=CATAN_PLAYERS[0])
    player_1_info = await db.get_winners_catan(year=2021, winner_game=CATAN_PLAYERS[1])
    player_2_info = await db.get_winners_catan(year=2021, winner_game=CATAN_PLAYERS[2])
    player_3_info = await db.get_winners_catan(year=2021, winner_game=CATAN_PLAYERS[3])

    if message.text == MAIN_HANDLERS["stats2021"]:
        await message.answer(
            "<b>Результаты за 2021 год: \n</b>"
            f"{CATAN_PLAYERS[0]}: {player_0_info} \n"
            f"{CATAN_PLAYERS[1]}: {player_1_info} \n"
            f"{CATAN_PLAYERS[2]}: {player_2_info} \n"
            f"{CATAN_PLAYERS[3]}: {player_3_info}",
            reply_markup=main_keyboard
        )

    elif message.text == MAIN_HANDLERS["statsAll"]:
        await message.answer(
            "<b>Статистика за всё время: \n</b>"
            f"{CATAN_PLAYERS[0]}: {17+10+player_0_info} \n"
            f"{CATAN_PLAYERS[1]}: {11+9+player_1_info} \n"
            f"{CATAN_PLAYERS[2]}: {9+2+player_2_info} \n"
            f"{CATAN_PLAYERS[3]}: {13+15+player_3_info} \n\n"
            "<b>Статистика за 2021 год: \n</b>"
            f"{CATAN_PLAYERS[0]}: {player_0_info} \n"
            f"{CATAN_PLAYERS[1]}: {player_1_info} \n"
            f"{CATAN_PLAYERS[2]}: {player_2_info} \n"
            f"{CATAN_PLAYERS[3]}: {player_3_info} \n\n"
            "<b>Статистика за 2020 год: \n</b>"
            f"{CATAN_PLAYERS[0]}: 17 \n"
            f"{CATAN_PLAYERS[1]}: 11 \n"
            f"{CATAN_PLAYERS[2]}: 9 \n"
            f"{CATAN_PLAYERS[3]}: 13 \n\n"
            "<b>Статистика за 2019 год: \n</b>"
            f"{CATAN_PLAYERS[0]}: 10 \n"
            f"{CATAN_PLAYERS[1]}: 9 \n"
            f"{CATAN_PLAYERS[2]}: 2 \n"
            f"{CATAN_PLAYERS[3]}: 15",
            reply_markup=main_keyboard
        )

    else:
        await message.answer(
            "Кажется, меня пытаются сломать. Пожалуйста, не надо!",
            reply_markup=main_keyboard
        )


# ОБЩЕЕ
# Возврат в главное меню
@dp.message_handler(Text(equals=[CATS_HANDLERS["back"], CATAN_HANDLERS["back"]]))
async def back_to_main_menu(message: Message):
    await message.answer(
        "Чем могу помочь? \n"
        "Выбери нужную категорию",
        reply_markup=main_admin_keyboard
    )


# КОШКА
# Записать себе кошку
@dp.message_handler(Text(equals=[CATS_HANDLERS["add_cleaning"]]))
async def add_cleaning(message: Message):

    if str(User.get_current().id) not in ADMINS_ID_LIST:
        await message.answer(
            "Функция доступна только для админов",
            reply_markup=main_keyboard
        )

    else:
        await db.add_cleaning_cats(ADMINS_DICT[str(message.from_user.id)])
        full_info = await db.get_info_cats()
        await message.answer(
            f"Я записал кошку пользователю {message.from_user.first_name}. \n\n"
            f"<b>Текущая статистика: \n</b>"
            f"{full_info[1].get('user_name')}: {full_info[1].get('amount_cleaning')} ({full_info[1].get('last_date_cleaning').strftime('%H:%M:%S %d.%m')}) \n"
            f"{full_info[0].get('user_name')}: {full_info[0].get('amount_cleaning')} ({full_info[0].get('last_date_cleaning').strftime('%H:%M:%S %d.%m')})",
        )


# Отменить последнюю запись по кошке
@dp.message_handler(Text(equals=[CATS_HANDLERS["cancel_cleaning"]]))
async def cancel_cleaning(message: Message):

    if str(User.get_current().id) not in ADMINS_ID_LIST:
        await message.answer(
            "Функция доступна только для админов",
            reply_markup=main_keyboard
        )

    else:
        await db.remove_cleaning_cats(ADMINS_DICT[str(message.from_user.id)])
        full_info = await db.get_info_cats()
        await message.answer(
            "Я отменил последнюю запись. \n\n"
            "<b>Текущая статистика: \n</b>"
            f"{full_info[1].get('user_name')}: {full_info[1].get('amount_cleaning')} ({full_info[1].get('last_date_cleaning').strftime('%H:%M:%S %d.%m')}) \n"
            f"{full_info[0].get('user_name')}: {full_info[0].get('amount_cleaning')} ({full_info[0].get('last_date_cleaning').strftime('%H:%M:%S %d.%m')})",
        )


# КОЛОНИЗАТОРЫ
# Записать игру
@dp.message_handler(Text(equals=[CATAN_HANDLERS["add_winner"]]))
async def record_game(message: Message):
    await message.answer(
        "Кто победил?",
        reply_markup=winner_catan_choose
    )


@dp.message_handler(Text(equals=CATAN_HANDLERS["players"]))
async def add_winner(message: Message):

    if str(User.get_current().id) not in ADMINS_ID_LIST:
        await message.answer(
            "Функция доступна только для админов",
            reply_markup=main_keyboard
        )

    else:
        await db.add_winner_catan(message.text)
        player_0_info = await db.get_winners_catan(year=2021, winner_game=CATAN_HANDLERS['players'][0])
        player_1_info = await db.get_winners_catan(year=2021, winner_game=CATAN_HANDLERS['players'][1])
        player_2_info = await db.get_winners_catan(year=2021, winner_game=CATAN_HANDLERS['players'][2])
        player_3_info = await db.get_winners_catan(year=2021, winner_game=CATAN_HANDLERS['players'][3])
        await message.answer(
            f"{message.text}, поздравляю тебя с победой! Я зафиксировал это в таблице результатов. \n\n"
            f"<b>Текущая статистика за 2021 год: \n</b>"
            f"{CATAN_HANDLERS['players'][0]}: {player_0_info} \n"
            f"{CATAN_HANDLERS['players'][1]}: {player_1_info} \n"
            f"{CATAN_HANDLERS['players'][2]}: {player_2_info} \n"
            f"{CATAN_HANDLERS['players'][3]}: {player_3_info}",
            reply_markup=main_catan_keyboard
        )


@dp.message_handler(Text(equals=[CATAN_HANDLERS["dont_record"]]))
async def dont_record(message: Message):
    await message.answer(
        "Ок!",
        reply_markup=main_catan_keyboard
    )


# Отменить последнюю запись по колонизаторам
@dp.message_handler(Text(equals=[CATAN_HANDLERS["cancel_last_record"]]))
async def cancel_last_record(message: Message):

    if str(User.get_current().id) not in ADMINS_ID_LIST:
        await message.answer(
            "Функция доступна только для админов",
            reply_markup=main_keyboard
        )

    else:
        await db.delete_last_game_catan()
        player_0_info = await db.get_winners_catan(year=2021, winner_game=CATAN_HANDLERS['players'][0])
        player_1_info = await db.get_winners_catan(year=2021, winner_game=CATAN_HANDLERS['players'][1])
        player_2_info = await db.get_winners_catan(year=2021, winner_game=CATAN_HANDLERS['players'][2])
        player_3_info = await db.get_winners_catan(year=2021, winner_game=CATAN_HANDLERS['players'][3])
        await message.answer(
            "Я отменил последнюю запись. \n\n"
            "<b>Текущая статистика за 2021 год: \n</b>"
            f"{CATAN_HANDLERS['players'][0]}: {player_0_info} \n"
            f"{CATAN_HANDLERS['players'][1]}: {player_1_info} \n"
            f"{CATAN_HANDLERS['players'][2]}: {player_2_info} \n"
            f"{CATAN_HANDLERS['players'][3]}: {player_3_info}",
        )


# Подробная статистика по колонизаторам
@dp.message_handler(Text(equals=[CATAN_HANDLERS["stats"]]))
async def get_stats(message: Message):
    player_0_info = await db.get_winners_catan(year=2021, winner_game=CATAN_HANDLERS['players'][0])
    player_1_info = await db.get_winners_catan(year=2021, winner_game=CATAN_HANDLERS['players'][1])
    player_2_info = await db.get_winners_catan(year=2021, winner_game=CATAN_HANDLERS['players'][2])
    player_3_info = await db.get_winners_catan(year=2021, winner_game=CATAN_HANDLERS['players'][3])
    await message.answer(
        "<b>Статистика за всё время: \n</b>"
        f"{CATAN_HANDLERS['players'][0]}: {17+10+player_0_info} \n"
        f"{CATAN_HANDLERS['players'][1]}: {11+9+player_1_info} \n"
        f"{CATAN_HANDLERS['players'][2]}: {9+2+player_2_info} \n"
        f"{CATAN_HANDLERS['players'][3]}: {13+15+player_3_info} \n\n"
        "<b>Статистика за 2021 год: \n</b>"
        f"{CATAN_HANDLERS['players'][0]}: {player_0_info} \n"
        f"{CATAN_HANDLERS['players'][1]}: {player_1_info} \n"
        f"{CATAN_HANDLERS['players'][2]}: {player_2_info} \n"
        f"{CATAN_HANDLERS['players'][3]}: {player_3_info} \n\n"
        "<b>Статистика за 2020 год: \n</b>"
        f"{CATAN_HANDLERS['players'][0]}: 17 \n"
        f"{CATAN_HANDLERS['players'][1]}: 11 \n"
        f"{CATAN_HANDLERS['players'][2]}: 9 \n"
        f"{CATAN_HANDLERS['players'][3]}: 13 \n\n"
        "<b>Статистика за 2019 год: \n</b>"
        f"{CATAN_HANDLERS['players'][0]}: 10 \n"
        f"{CATAN_HANDLERS['players'][1]}: 9 \n"
        f"{CATAN_HANDLERS['players'][2]}: 2 \n"
        f"{CATAN_HANDLERS['players'][3]}: 15"
    )
