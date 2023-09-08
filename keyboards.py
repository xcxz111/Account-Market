from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from const_strings import CABINET, BILLING, MY_PURCHASES, HOME, BILLING_USDT, STATISTIC, EDIT_BILLING, BACK_HOME, \
    PARTNERSHIP, SHOPPING_CART, COMPLETE_ORDER, ADD_PRODUCT, CLEAR_CART, TELEGRAM_TDATA_USA, \
    TELEGRAM_TDATA_GHANA, TELEGRAM_SESSION_RU, TELEGRAM_TDATA, TELEGRAM_SESSION, BACK_CABINET, TELEGRAM, \
    BACK_TELEGRAM, SETTINGS, COMPLETE_USDT, COMPLETE_BLIK

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

SHOPPING_CART_KBD = [
    [InlineKeyboardButton("оплатить заказ", callback_data=COMPLETE_ORDER)],
    [InlineKeyboardButton("добавить товары", callback_data=ADD_PRODUCT)],
    [InlineKeyboardButton("очистить корзину", callback_data=CLEAR_CART)],
    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_CABINET),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME)]
]



TELEGRAM_KBD = [
    [InlineKeyboardButton("Tdata", callback_data=TELEGRAM_TDATA)],
    [InlineKeyboardButton("Session+Json", callback_data=TELEGRAM_SESSION)],
    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_HOME),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME)]
]


TELEGRAM_TDATA_KBD = [
    [InlineKeyboardButton("USA (+1) - 1.5$", callback_data=TELEGRAM_TDATA_USA)],
    [InlineKeyboardButton("GHANA (+233) - 1.3$", callback_data=TELEGRAM_TDATA_GHANA)],

    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_TELEGRAM),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME),
    ],
]

TELEGRAM_SESSION_KBD = [
    [InlineKeyboardButton("RU (+7) - 2$", callback_data=TELEGRAM_SESSION_RU)],
    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_TELEGRAM),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME),
    ],
]




ADMIN_KBD = [
    [InlineKeyboardButton("статистика", callback_data=STATISTIC)],
    [InlineKeyboardButton("настройки", callback_data=SETTINGS)],
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


COMPLETE_ORDER_KBD = [
    [InlineKeyboardButton("оплатить USDT", callback_data=COMPLETE_USDT)],
    [InlineKeyboardButton("оплатить Blik", callback_data=COMPLETE_BLIK)],

    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_CABINET),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME)]

]


TELEGRAM_QUANTITY_KBD = [
    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_TELEGRAM),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME)]
]