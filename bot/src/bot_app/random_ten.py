from aiogram import types
from . app import dp


@dp.message_handler(commands='train_ten')
async def train_ten(message: types.Message):
    await message.reply("train_ten")