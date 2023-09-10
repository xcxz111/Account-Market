from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from const_strings import CABINET, BILLING, MY_PURCHASES, HOME, BILLING_USDT, BACK_HOME, PARTNERSHIP, SHOPPING_CART, \
    BACK_CABINET, TELEGRAM

HOME_KBD = [
    [InlineKeyboardButton("👤 Личный кабинет ", callback_data=CABINET)],
    [InlineKeyboardButton("💰 Пополнить счет", callback_data=BILLING)],
    [InlineKeyboardButton("купить TELEGRAM аккаунт", callback_data=TELEGRAM)],
    [InlineKeyboardButton("Инструкция", url="https://telegra.ph/Pravila-pokupok-v-magazine-LINCOLN-MARKET-11-25")],
    [InlineKeyboardButton("Сотрудничество", callback_data=PARTNERSHIP)],
    [InlineKeyboardButton("наш канал", url="https://t.me/tg_selling_market")]
    ]


CABINET_KBD = [
    [InlineKeyboardButton("мои покупки", callback_data=MY_PURCHASES)],
    [InlineKeyboardButton("💰 Пополнить счет", callback_data=BILLING)],
    [InlineKeyboardButton("моя корзина", callback_data=SHOPPING_CART)],
    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_HOME),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME)]

]


BILLING_KBD = [
    [InlineKeyboardButton("пополнить USDT", callback_data=BILLING_USDT)],
    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_CABINET),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME)]

]



PARTNERSHIP_KBD = [
    [InlineKeyboardButton("написать админу", url="https://t.me/real2021money")],
    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_HOME),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME)]

]




