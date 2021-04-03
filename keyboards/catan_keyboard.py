from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Возможные хэндлеры
CATAN_HANDLERS = {
    "add_winner": "🏆 Добавить победителя",
    "cancel_last_record": "🗑 Удалить последнюю запись",
    "stats": "📈 Подробная статистика",
    "back": "◀️ Назад",
    "players": ["Гриша", "Вика", "Слава", "Лена"],
    "dont_record": "🚫 Не записывать"
}

# Клавиатура первого уровня
main_catan_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=CATAN_HANDLERS["add_winner"]),
        ],
        [
            KeyboardButton(text=CATAN_HANDLERS["cancel_last_record"]),
        ],
        [
            KeyboardButton(text=CATAN_HANDLERS["stats"]),
        ],
        [
            KeyboardButton(text=CATAN_HANDLERS["back"]),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)

# Выбор победителя
winner_catan_choose = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=CATAN_HANDLERS["players"][0]),
            KeyboardButton(text=CATAN_HANDLERS["players"][1]),
        ],
        [
            KeyboardButton(text=CATAN_HANDLERS["players"][2]),
            KeyboardButton(text=CATAN_HANDLERS["players"][3]),
        ],
        [
            KeyboardButton(text=CATAN_HANDLERS["dont_record"]),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)
