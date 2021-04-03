import os

from dotenv import load_dotenv


load_dotenv()

# Заберем токен нашего бота
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

# Тут у нас будет список из админов
ADMINS_ID_LIST = os.getenv("ADMIN_ID").split(",")
ADMINS_DICT = {
    ADMINS_ID_LIST[0]: "Гриша",
    ADMINS_ID_LIST[1]: "Вика",
}

# Заберем данные для подключения к базе данных (юзер, пароль, название бд)
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
PGHOST = str(os.getenv("PGHOST"))
