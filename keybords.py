from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


ikb=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Продуке 1',callback_data="product_buying"),
    InlineKeyboardButton(text='Продуке 2',callback_data="product_buying"),
    InlineKeyboardButton(text='Продуке 3',callback_data="product_buying"),
    InlineKeyboardButton(text='Продуке 4',callback_data="product_buying")]])



kb=ReplyKeyboardMarkup(keyboard=[
                                 [KeyboardButton(text='Рассчитать',callback_data='calculate1'),
                                  KeyboardButton(text='Информация',callback_data='calculate'),],
                                 [KeyboardButton(text='Купить')]], resize_keyboard=True,)













