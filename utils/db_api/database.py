import asyncio
import asyncpg
import logging
import os


from data.config import PGHOST, PGPASSWORD, PGUSER


logging_config = logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.INFO,
)


async def create_db_cats():
    current_path = os.getcwd() + "/utils/db_api"
    create_db_command = open(f"{current_path}/create_db_cats.sql", "r").read()

    logging.info("Connecting to database...")
    conn: asyncpg.Connection = await asyncpg.connect(
        user=PGUSER,
        password=PGPASSWORD,
        host=PGHOST
    )

    await conn.execute(create_db_command)
    await conn.close()
    logging.info("Table cats created")


async def create_db_catan():
    current_path = os.getcwd() + "/utils/db_api"
    create_db_command = open(f"{current_path}/create_db_catan.sql", "r").read()

    logging.info("Connecting to database...")
    conn: asyncpg.Connection = await asyncpg.connect(
        user=PGUSER,
        password=PGPASSWORD,
        host=PGHOST
    )

    await conn.execute(create_db_command)
    await conn.close()
    logging.info("Table catan created")


async def create_db_users():
    current_path = os.getcwd() + "/utils/db_api"
    create_db_command = open(f"{current_path}/create_db_users.sql", "r").read()

    logging.info("Connecting to database...")
    conn: asyncpg.Connection = await asyncpg.connect(
        user=PGUSER,
        password=PGPASSWORD,
        host=PGHOST
    )

    await conn.execute(create_db_command)
    await conn.close()
    logging.info("Table users created")


async def create_pool():
    return await asyncpg.create_pool(
        user=PGUSER,
        password=PGPASSWORD,
        host=PGHOST
    )


if __name__ == '__main__':
    loop_cats = asyncio.get_event_loop()
    loop_cats.run_until_complete(create_db_cats())

    loop_catan = asyncio.get_event_loop()
    loop_catan.run_until_complete(create_db_catan())

    loop_users = asyncio.get_event_loop()
    loop_users.run_until_complete(create_db_users())
