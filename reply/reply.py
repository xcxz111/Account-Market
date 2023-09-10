from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import ContextTypes

from config import BOT_USERNAME
from const_strings import ADMIN
from keyboards.keyboards import HOME_KBD, CABINET_KBD, BILLING_KBD, PARTNERSHIP_KBD

from reply.reply_telegram import telegram_reply
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
    context.user_data['state'] = 'home'


async def cabinet_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(CABINET_KBD)
    await query.edit_message_text(f"«Welcome to {BOT_USERNAME} 24/7»\n"\
            f"🆔Telegram ID: {user.id}\n"         
            f"💰Ваш баланс: 0 PLN.\n"  # TODO добавить баланс
            f"🔰Количество покупок: 0\n", reply_markup=reply_markup)
    context.user_data['state'] = 'cabinet'


async def billing_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(BILLING_KBD)
    await query.edit_message_text(f"выберите метод оплаты", reply_markup=reply_markup)
    context.user_data['state'] = 'billing'


async def back_home_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await home_reply(update, context)
    context.user_data['state'] = 'back_home'


async def back_cabinet_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await cabinet_reply(update, context)
    context.user_data['state'] = 'back_cabinet'


async def back_telegram_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await telegram_reply(update, context)
    context.user_data['state'] = 'back_telegram'


async def partnership_replay(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(PARTNERSHIP_KBD)
    await query.edit_message_text(f"по любым вопросам сотрудничества писать админу: @real2021money", reply_markup=reply_markup)
    context.user_data['state'] = 'partnership'


