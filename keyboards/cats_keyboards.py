from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Возможные хэндлеры
CATS_HANDLERS = {
    "add_cleaning": "🧹Записать себе кошку",
    "cancel_cleaning": "🗑 Отменить последнюю запись",
    "back": "◀️ Назад",
    "users": ["Гриша", "Вика"]
}

# Клавиатура первого уровня
main_cats_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=CATS_HANDLERS["add_cleaning"]),
        ],
        [
            KeyboardButton(text=CATS_HANDLERS["cancel_cleaning"]),
        ],
        [
            KeyboardButton(text=CATS_HANDLERS["back"]),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)
