from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Возможные хэндлеры не для админов
MAIN_HANDLERS = {
    "stats2021": "📊 Статистика за 2021 год",
    "statsAll": "📈 Статистика за всё время",
}

# Список игроков
CATAN_PLAYERS = ["Гриша", "Вика", "Слава", "Лена"]

# Главная клавиатура не для админов
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=MAIN_HANDLERS["stats2021"]),
        ],
        [
            KeyboardButton(text=MAIN_HANDLERS["statsAll"])
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)
