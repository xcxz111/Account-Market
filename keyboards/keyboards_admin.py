from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from const_strings import STATISTIC, ADD_ACCOUNT, EDIT_BILLING, BACK_HOME, ADD_ACCOUNT_TDATA, ADD_ACCOUNT_SESSION, HOME, \
    ADD_ACCOUNT_TDATA_USA, ADD_ACCOUNT_TDATA_GHANA, ADD_ACCOUNT_SESSION_RU, SETTINGS

ADMIN_KBD = [
    [InlineKeyboardButton("статистика", callback_data=STATISTIC)],
    [InlineKeyboardButton("добавить товар", callback_data=ADD_ACCOUNT)],
    [InlineKeyboardButton("настройки", callback_data=SETTINGS)],
    [InlineKeyboardButton("настройки платежей", callback_data=EDIT_BILLING)],
    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_HOME),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME)]

]

ADD_ACCOUNT_KBD = [
    [InlineKeyboardButton("tdata", callback_data=ADD_ACCOUNT_TDATA)],
    [InlineKeyboardButton("Session+Json", callback_data=ADD_ACCOUNT_SESSION)],

    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_HOME),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME)]

]

ADD_ACCOUNT_TDATA_KBD = [
    [InlineKeyboardButton("USA", callback_data=ADD_ACCOUNT_TDATA_USA)],
    [InlineKeyboardButton("GHANA", callback_data=ADD_ACCOUNT_TDATA_GHANA)],

    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_HOME),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME)]

]


ADD_ACCOUNT_SESSION_KBD = [
    [InlineKeyboardButton("RU", callback_data=ADD_ACCOUNT_SESSION_RU)],

    [
        InlineKeyboardButton("🔸 Назад", callback_data=BACK_HOME),
        InlineKeyboardButton("🔹 Главная", callback_data=HOME)]

]