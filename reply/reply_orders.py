from telegram import InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from keyboards.keyboards_orders import SHOPPING_CART_KBD, COMPLETE_ORDER_KBD
from reply.reply_telegram import telegram_reply


async def my_purchases_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.edit_message_text(f"тут будет список ваших покупок")
    context.user_data['state'] = 'my_purchases'


async def shopping_cart_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(SHOPPING_CART_KBD)
    await query.edit_message_text(f"в вашей корзине *** товаров на сумму *** ", reply_markup=reply_markup)
    context.user_data['state'] = 'shopping_cart'


async def add_product_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await telegram_reply(update, context)
    context.user_data['state'] = 'add_product'


async def complete_order_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(COMPLETE_ORDER_KBD)
    await query.edit_message_text(f"сумма к оплате *** \n"
                                  f"выберите платежный метод", reply_markup=reply_markup)
    context.user_data['state'] = 'complete_order'