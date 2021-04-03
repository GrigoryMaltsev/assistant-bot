from asyncpg import Connection, Record
from aiogram.types import User
from typing import List

from loader import bot, dp, db


class DBCommands:
    pool: Connection = db

    ADD_NEW_USER = "INSERT INTO users(adding_date, user_info) VALUES (NOW(), $1) RETURNING id_user"

    COUNT_CLEANINGS_CATS = "SELECT * FROM cats"
    ADD_CLEANING_CATS = "UPDATE cats SET amount_cleaning=amount_cleaning+1, last_date_cleaning=NOW() WHERE user_name=$1"
    REMOVE_CLEANING_CATS = "UPDATE cats SET amount_cleaning=amount_cleaning-1, last_date_cleaning=NOW() WHERE user_name=$1"

    GET_WINNERS_CATAN = "SELECT COUNT(*) FROM catan WHERE EXTRACT(YEAR FROM date_game) = $1 and winner_game = $2"
    ADD_NEW_WINNER_CATAN = "INSERT INTO catan(date_game, winner_game) VALUES (NOW(), $1)"
    DELETE_LAST_GAME_CATAN = "DELETE FROM catan WHERE id_game = (SELECT id_game FROM catan WHERE id_game=(SELECT max(id_game) FROM catan))"

    # Записываем в базу users нового пользователя бота
    async def add_new_user(self):
        full_info = User.get_current()

        user_info = f"id: {full_info.id}, username: {full_info.username}, first_name: {full_info.first_name}, last_name: {full_info.last_name}"

        command = self.ADD_NEW_USER
        id_user = await self.pool.fetchval(command, user_info)
        return id_user

    # Получаем статистику по кошкам
    async def get_info_cats(self):
        command = self.COUNT_CLEANINGS_CATS
        full_info: List[Record] = await self.pool.fetch(command)
        return full_info

    # Добавление записи по кошкам
    async def add_cleaning_cats(self, user_name):
        command = self.ADD_CLEANING_CATS
        return await self.pool.fetchval(command, user_name)

    # Отменяем последнюю запись по кошкам
    async def remove_cleaning_cats(self, user_name):
        command = self.REMOVE_CLEANING_CATS
        return await self.pool.fetchval(command, user_name)

    # Получение статистики по колониизаторам за 2021
    async def get_winners_catan(self, year, winner_game):
        command = self.GET_WINNERS_CATAN
        return await self.pool.fetchval(command, year, winner_game)

    # Добавляем победителя по колоннизаторам
    async def add_winner_catan(self, winner_game):
        command = self.ADD_NEW_WINNER_CATAN
        return await self.pool.fetchval(command, winner_game)

    # Отменяем последнюю запись по колонизаторам
    async def delete_last_game_catan(self):
        command = self.DELETE_LAST_GAME_CATAN
        return await self.pool.fetchval(command)
