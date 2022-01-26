from aiogram import types
from . app import dp, bot
from . keyboards import inline_kb
from . states import GameStates
from . data_fetcher import get_random
from aiogram.dispatcher import FSMContext
from . import messages


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(messages.WELCOME_MESSAGE)


@dp.message_handler(commands='train_ten', state="*")
async def train_ten(message: types.Message, state: FSMContext):
    await GameStates.random_ten.set()
    res = await get_random()
    async with state.proxy() as data:
        data['step'] = 1
        data['answer'] = res.get('part_of_word')
        data['word'] = res.get('word')

        await message.reply(f"{ data['step']} of 10, English words list ❄️{data['word']}❄️", reply_markup=inline_kb)


@dp.callback_query_handler(lambda c: c.data in ['noun', 'verb', 'adjective', 'pronoun', 'adverb', 'numeral'], state=GameStates.random_ten)
async def button_click_call_back(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    answer = callback_query.data
    async with state.proxy() as data:
        if answer == data.get('answer'):
            await bot.send_message(callback_query.from_user.id, 'Correct\n' + f"{data['word']} is {data['answer']}")
            res = await get_random()
            data['step'] += 1
            data['answer'] = res.get('part_of_word')
            data['word'] = res.get('word')
            if data['step'] > 10:
                await bot.send_message(callback_query.from_user.id, "The game is over!!!")
                await GameStates.start.set()
            else:
                await bot.send_message(callback_query.from_user.id, f"{ data['step']} of 10, English words list ❄️{data['word']}❄️", reply_markup=inline_kb)

        else:
            await bot.send_message(callback_query.from_user.id, f'No\n', reply_markup=inline_kb)