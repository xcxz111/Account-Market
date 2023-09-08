from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import ContextTypes

from config import BOT_USERNAME
from const_strings import ADMIN
from keyboards import HOME_KBD, CABINET_KBD, BILLING_KBD, ADMIN_KBD, TELEGRAM_KBD, PARTNERSHIP_KBD, SHOPPING_CART_KBD, \
    TELEGRAM_TDATA_KBD, TELEGRAM_SESSION_KBD, COMPLETE_ORDER_KBD, TELEGRAM_QUANTITY_KBD
from users.common import is_admin


async def home_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    admin = is_admin(user)

    if admin:
        admin_btn_exists = False
        for i in HOME_KBD[0]:
            if i.callback_data == ADMIN:
                admin_btn_exists = True
                break

        if not admin_btn_exists:
            HOME_KBD[0].append(InlineKeyboardButton("Admin", callback_data=ADMIN))
    reply_markup = InlineKeyboardMarkup(HOME_KBD)

    query = update.callback_query
    if query is not None:
        await query.edit_message_text(f"«Welcome to {BOT_USERNAME} 24/7»\n"\
            f"🆔Telegram ID: {user.id}\n"         
            f"💰Ваш баланс: 0 PLN.\n"  # TODO добавить баланс
            f"🔰Количество покупок: 0\n", reply_markup=reply_markup)
    else:
        await update.effective_user.send_message(f"«Welcome to {BOT_USERNAME} 24/7»\n"\
            f"🆔Telegram ID: {user.id}\n"         
            f"💰Ваш баланс: 0 PLN.\n"  # TODO добавить баланс
            f"🔰Количество покупок: 0\n", reply_markup=reply_markup)


async def cabinet_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(CABINET_KBD)
    await query.edit_message_text(f"«Welcome to {BOT_USERNAME} 24/7»\n"\
            f"🆔Telegram ID: {user.id}\n"         
            f"💰Ваш баланс: 0 PLN.\n"  # TODO добавить баланс
            f"🔰Количество покупок: 0\n", reply_markup=reply_markup)


async def billing_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(BILLING_KBD)
    await query.edit_message_text(f"выберите метод оплаты", reply_markup=reply_markup)


async def my_purchases_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.edit_message_text(f"тут будет список ваших покупок")


async def shopping_cart_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(SHOPPING_CART_KBD)
    await query.edit_message_text(f"в вашей корзине *** товаров на сумму *** ", reply_markup=reply_markup)


async def add_product_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await telegram_reply(update, context)


async def back_home_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await home_reply(update, context)


async def complete_order_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(COMPLETE_ORDER_KBD)
    await query.edit_message_text(f"сумма к оплате *** \n"
                                  f"выберите платежный метод", reply_markup=reply_markup)


async def back_cabinet_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await cabinet_reply(update, context)



async def telegram_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(TELEGRAM_KBD)
    await query.edit_message_text(f"Выберите формат", reply_markup=reply_markup)


async def telegram_tdata_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(TELEGRAM_TDATA_KBD)
    await query.edit_message_text(f"Выберите страну аккаунта", reply_markup=reply_markup)


async def telegram_session_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(TELEGRAM_SESSION_KBD)
    await query.edit_message_text(f"Выберите страну аккаунта", reply_markup=reply_markup)


async def telegram_tdata_usa_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(TELEGRAM_QUANTITY_KBD)
    await query.edit_message_text(f"Telegram аккаунт GHANNA (+233) с отлежкой \n" 
                                    f"формат: tdata \n"
                                    f"в наличии есть *** \n"
                                    f"введите нужное количество", reply_markup=reply_markup)


async def telegram_tdata_ghana_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(TELEGRAM_QUANTITY_KBD)
    await query.edit_message_text(f"Telegram аккаунт GHANNA (+233) с отлежкой \n" 
                                    f"формат: tdata \n"
                                    f"в наличии есть *** \n"
                                    f"введите нужное количество", reply_markup=reply_markup)


async def telegram_session_ru_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(TELEGRAM_QUANTITY_KBD)
    await query.edit_message_text(f"Telegram аккаунт GHANNA (+233) с отлежкой \n" 
                                    f"формат: tdata \n"
                                    f"в наличии есть *** \n"
                                    f"введите нужное количество", reply_markup=reply_markup)


async def back_telegram_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await telegram_reply(update, context)


async def admin_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(ADMIN_KBD)
    await query.edit_message_text(f"Приветствую в Панели Администратора", reply_markup=reply_markup)


async def partnership_replay(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(PARTNERSHIP_KBD)
    await query.edit_message_text(f"по любым вопросам сотрудничества писать админу: @real2021money", reply_markup=reply_markup)


