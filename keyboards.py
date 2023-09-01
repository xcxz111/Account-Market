from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from const_strings import CABINET, BILLING, TELEGRAM, INSTAGRAM, GMAIL, MY_PURCHASES, HOME, BILLING_USDT, \
    STATISTIC, EDIT_BILLING, BUY_GMAIL_ACCOUNT, ADD_SUBSCRIBERS_INSTAGRAM, BUY_INSTAGRAM_ACCOUNT, \
    ADD_SUBSCRIBERS_TELEGRAM, BUY_TELEGRAM_ACCOUNT, BACK_TELEGRAM, BACK_HOME, TG_FORMAT, TG_USA, TG_GANA, TG_RU, \
    BACK_BUY_TELEGRAM_ACCOUNT, BACK_TG_FORMAT, PARTNERSHIP

services_dict = {}
services_telegram_dict = ["купить telegram аккаунт", "заказать накрутку", "заказать просмотры"]


HOME_KBD = [
    [
        InlineKeyboardButton("👤 Личный кабинет ", callback_data=CABINET),
        InlineKeyboardButton("💰 Пополнить счет", callback_data=BILLING),
    ],
    [InlineKeyboardButton("TELEGRAM", callback_data=TELEGRAM)],
    [InlineKeyboardButton("INSTAGRAM", callback_data=INSTAGRAM)],
    [InlineKeyboardButton("GMAIL", callback_data=GMAIL)],
    [InlineKeyboardButton("Инструкция", url="https://telegra.ph/Pravila-pokupok-v-magazine-LINCOLN-MARKET-11-25")],
    [InlineKeyboardButton("Сотрудничество", callback_data=PARTNERSHIP)],
    [InlineKeyboardButton("наш канал", url="https://t.me/tg_selling_market")]
    ]


CABINET_KBD = [
    [InlineKeyboardButton("мои покупки", callback_data=MY_PURCHASES)],
    [InlineKeyboardButton("💰 Пополнить счет", callback_data=BILLING)],
    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_HOME),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME)]

]


BILLING_KBD = [
    [InlineKeyboardButton("пополнить USDT", callback_data=BILLING_USDT)],
    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_HOME),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME)]

]

TELEGRAM_KBD = [
    [InlineKeyboardButton("купить telegram аккаунт", callback_data=BUY_TELEGRAM_ACCOUNT)],
    [InlineKeyboardButton("заказать накрутку", callback_data=ADD_SUBSCRIBERS_TELEGRAM)],
    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_HOME),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME)]
]

BUY_TELEGRAM_KBD = [
    [InlineKeyboardButton("tdata", callback_data=TG_FORMAT)],
    [
        InlineKeyboardButton("🔸Назад", callback_data=BACK_TELEGRAM),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME),
    ],
]

TG_FORMAT_KBD = [
    [InlineKeyboardButton("USA (+1)", callback_data=TG_USA)],
    [InlineKeyboardButton("GANA (+233)", callback_data=TG_GANA)],
    [InlineKeyboardButton("RU (+7)", callback_data=TG_RU)],

    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_TG_FORMAT),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME),
    ],
]

INSTAGRAM_KBD = [
    [InlineKeyboardButton("купить instagram аккаунт", callback_data=BUY_INSTAGRAM_ACCOUNT)],
    [InlineKeyboardButton("заказать накрутку", callback_data=ADD_SUBSCRIBERS_INSTAGRAM)],
    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_HOME),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME)]
]

GMAIL_KBD = [
    [InlineKeyboardButton("купить Gmail аккаунт", callback_data=BUY_GMAIL_ACCOUNT)],
    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_HOME),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME)]
]

ADMIN_KBD = [
    [InlineKeyboardButton("статистика", callback_data=STATISTIC)],
    [InlineKeyboardButton("настройки платежей", callback_data=EDIT_BILLING)],
    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_HOME),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME)]

]


PARTNERSHIP_KBD = [
    [InlineKeyboardButton("написать админу", url="https://t.me/real2021money")],
    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_HOME),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME)]

]




