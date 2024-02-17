from aiogram import types

btn = [
    [types.KeyboardButton(text="Telefonlar"), types.KeyboardButton(text="Aksessuarlar")],
]

buttons = types.ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True)




