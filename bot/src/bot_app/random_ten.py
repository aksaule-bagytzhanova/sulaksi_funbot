from aiogram import types
from . app import dp
from . keyboards import inline_kb
from . states import GameStates
from . data_fetcher import get_random
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands='train_ten', state="*")
async def train_ten(message: types.Message, state: FSMContext):
    await GameStates.random_ten.set()
    res = await get_random()
    async with state.proxy() as data:
        data['step'] = 1
        data['answer'] = res.get('part_of_word')
        data['word'] = res.get(' word')

        await message.reply("train_ten", reply_markup=inline_kb)