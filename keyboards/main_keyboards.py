from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Возможные хэндлеры для админов
MAIN_ADMIN_HANDLERS = {
    "cats": "🐈 Кошки",
    "catan": "🎲 Колонизаторы",
}

# Главная клавиатура для админов
main_admin_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=MAIN_ADMIN_HANDLERS["cats"]),
        ],
        [
            KeyboardButton(text=MAIN_ADMIN_HANDLERS["catan"])
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)
