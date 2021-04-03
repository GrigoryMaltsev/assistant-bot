import asyncio
from utils.db_api.database import create_db_users, create_db_catan, create_db_cats


async def on_startup(dp):
    await asyncio.sleep(10)

    await create_db_users()
    await create_db_cats()
    await create_db_catan()

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
