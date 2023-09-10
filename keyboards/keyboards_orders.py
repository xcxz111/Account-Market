from telegram import InlineKeyboardButton

from const_strings import COMPLETE_ORDER, ADD_PRODUCT, CLEAR_CART, BACK_CABINET, HOME, COMPLETE_USDT, COMPLETE_BLIK, \
    QUANTITY, MINUS, PLUS, ADD_TO_CART, BACK_TELEGRAM

SHOPPING_CART_KBD = [
    [InlineKeyboardButton("оплатить заказ", callback_data=COMPLETE_ORDER)],
    [InlineKeyboardButton("добавить товары", callback_data=ADD_PRODUCT)],
    [InlineKeyboardButton("очистить корзину", callback_data=CLEAR_CART)],
    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_CABINET),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME)]
]



COMPLETE_ORDER_KBD = [
    [InlineKeyboardButton("оплатить USDT", callback_data=COMPLETE_USDT)],
    [InlineKeyboardButton("оплатить Blik", callback_data=COMPLETE_BLIK)],

    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_CABINET),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME)]

]


TELEGRAM_QUANTITY_KBD = [
    [
        InlineKeyboardButton("-", callback_data=MINUS),
        InlineKeyboardButton("количество: 15", callback_data=QUANTITY),
        InlineKeyboardButton("+", callback_data=PLUS)],
    [
        InlineKeyboardButton("добавить в корзину", callback_data=ADD_TO_CART),
        InlineKeyboardButton("оплатить заказ", callback_data=COMPLETE_ORDER)],
    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_TELEGRAM),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME)]
]
