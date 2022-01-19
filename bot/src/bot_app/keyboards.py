from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

inline_button_1 = InlineKeyboardButton('Noun', callback_data='noun')
inline_button_2 = InlineKeyboardButton('Verb', callback_data='verb')
inline_button_3 = InlineKeyboardButton('Adjective', callback_data='adjective')
inline_button_4 = InlineKeyboardButton('Pronoun', callback_data='pronoun')
inline_button_5 = InlineKeyboardButton('Аdverb', callback_data='adverb')
inline_button_6 = InlineKeyboardButton('Numeral', callback_data='numeral')
inline_kb = InlineKeyboardMarkup()

inline_kb.add(inline_button_1)
inline_kb.add(inline_button_2)
inline_kb.add(inline_button_3)
inline_kb.add(inline_button_4)
inline_kb.add(inline_button_5)
inline_kb.add(inline_button_6)





