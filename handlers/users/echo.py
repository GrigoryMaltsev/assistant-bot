from aiogram.types import Message
from loader import dp


@dp.message_handler()
async def bot_echo(message: Message):
    if message.text[-1] == "?":
        await message.answer("Хороший вопрос. Но я могу только посоветовать воспользоваться командой /help")
    elif message.text == "/start":
        await message.answer("Нужно останоовить и запустить бота заного")
    elif message.text == "/help":
        await message.answer("Я бы мог написать инструкцию, но, мне кажется, что тут всё очевидно :)")
    else:
        await message.answer("Я бы поддержал беседу, но мне не разрешают :(")
