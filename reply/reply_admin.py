from telegram import InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from keyboards.keyboards_admin import ADMIN_KBD, ADD_ACCOUNT_KBD, ADD_ACCOUNT_TDATA_KBD


async def admin_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(ADMIN_KBD)
    await query.edit_message_text(f"Приветствую в Панели Администратора", reply_markup=reply_markup)
    context.user_data['state'] = 'admin'


async def add_account_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(ADD_ACCOUNT_KBD)
    await query.edit_message_text(f"выберите формат", reply_markup=reply_markup)
    context.user_data['state'] = 'add_account'


async def add_account_tdata_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(ADD_ACCOUNT_TDATA_KBD)
    await query.edit_message_text(f"выберите страну", reply_markup=reply_markup)
    context.user_data['state'] = 'add_account_tdata'


async def add_account_tdata_usa_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.edit_message_text(f"Отправьте файл")
    context.user_data['state'] = 'add_account_tdata_usa'