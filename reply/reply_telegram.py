from telegram import InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from keyboards.keyboards_orders import TELEGRAM_QUANTITY_KBD
from keyboards.keyboards_telegram import TELEGRAM_KBD, TELEGRAM_TDATA_KBD, TELEGRAM_SESSION_KBD


async def telegram_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(TELEGRAM_KBD)
    await query.edit_message_text(f"Выберите формат", reply_markup=reply_markup)
    context.user_data['state'] = 'telegram'


async def telegram_tdata_reply(bot: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = bot.callback_query
    reply_markup = InlineKeyboardMarkup(TELEGRAM_TDATA_KBD)
    await query.edit_message_text(f"Выберите страну аккаунта", reply_markup=reply_markup)
    context.user_data['state'] = 'telegram_tdata'


async def telegram_session_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(TELEGRAM_SESSION_KBD)
    await query.edit_message_text(f"Выберите страну аккаунта", reply_markup=reply_markup)
    context.user_data['state'] = 'telegram_session'


async def telegram_tdata_usa_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(TELEGRAM_QUANTITY_KBD)
    await query.edit_message_text(f"Telegram аккаунт USA (+1) с отлежкой \n"
                                    f"формат: tdata \n"
                                    f"в наличии есть *** \n"
                                    f"введите нужное количество", reply_markup=reply_markup)
    context.user_data['state'] = 'telegram_tdata_usa'


async def telegram_tdata_ghana_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(TELEGRAM_QUANTITY_KBD)
    await query.edit_message_text(f"Telegram аккаунт GHANNA (+233) с отлежкой \n" 
                                    f"формат: tdata \n"
                                    f"в наличии есть *** \n"
                                    f"введите нужное количество", reply_markup=reply_markup)
    context.user_data['state'] = 'telegram_ghana'


async def telegram_session_ru_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(TELEGRAM_QUANTITY_KBD)
    await query.edit_message_text(f"Telegram аккаунт RU (+7) с отлежкой \n" 
                                    f"формат: session+Json \n"
                                    f"в наличии есть *** \n"
                                    f"введите нужное количество", reply_markup=reply_markup)
    context.user_data['state'] = 'telegram_ghana'



