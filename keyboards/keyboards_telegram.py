from telegram import InlineKeyboardButton

from const_strings import TELEGRAM_TDATA, TELEGRAM_SESSION, BACK_HOME, HOME, TELEGRAM_TDATA_USA, TELEGRAM_TDATA_GHANA, \
    BACK_TELEGRAM, TELEGRAM_SESSION_RU

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