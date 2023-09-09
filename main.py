from pathlib import Path

from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

from loguru import logger
from telegram.ext.filters import REPLY

from config import TOKEN
from const_strings import HOME, CABINET, BILLING, ADMIN, TELEGRAM, \
    BACK_HOME, BACK_TELEGRAM, PARTNERSHIP, SHOPPING_CART, TELEGRAM_TDATA, TELEGRAM_SESSION, \
    TELEGRAM_TDATA_USA, TELEGRAM_SESSION_RU, TELEGRAM_TDATA_GHANA, BACK_CABINET, ADD_PRODUCT, COMPLETE_ORDER
from reply import home_reply, cabinet_reply, billing_reply, admin_reply, telegram_reply, back_home_reply, \
    partnership_replay, shopping_cart_reply, telegram_tdata_reply, telegram_session_reply, telegram_tdata_usa_reply, \
    telegram_tdata_ghana_reply, telegram_session_ru_reply, back_cabinet_reply, back_telegram_reply, add_product_reply, \
    complete_order_reply
from users.common import is_admin

logger.add(Path(__file__).name + ".log", retention="10 days")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    admin = is_admin(user)

    logger.debug(f'start for user: {user.username} [{"ADMIN" if admin else "NOT ADMIN"}]')

    await home_reply(update, context)


REPLY = {
    HOME: home_reply,
    CABINET: cabinet_reply,
    BACK_CABINET: back_cabinet_reply,
    BILLING: billing_reply,
    ADMIN: admin_reply,
    TELEGRAM: telegram_reply,
    BACK_HOME: back_home_reply,
    BACK_TELEGRAM: back_telegram_reply,
    PARTNERSHIP: partnership_replay,
    SHOPPING_CART: shopping_cart_reply,
    TELEGRAM_TDATA: telegram_tdata_reply,
    TELEGRAM_SESSION: telegram_session_reply,
    TELEGRAM_TDATA_USA: telegram_tdata_usa_reply,
    TELEGRAM_TDATA_GHANA: telegram_tdata_ghana_reply,
    TELEGRAM_SESSION_RU: telegram_session_ru_reply,
    ADD_PRODUCT: add_product_reply,
    COMPLETE_ORDER: complete_order_reply,

}


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    await query.answer()
    if query.data in REPLY:
        await REPLY[query.data](update, context)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    logger.warning("In help handler")
    await update.message.reply_text("Help!")


async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    photo = update.message.photo[-1]
    photo_file = await photo.get_file()
    await photo_file.download_to_drive(Path('photos') / photo.file_unique_idfile_id)
    logger.debug(f'Recerved photo with TO: {photo.file_id}')


def main():
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(MessageHandler(filters.PHOTO, photo_handler))

    application.add_handler(CallbackQueryHandler(button))


    logger.info("Bot started")
    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)
    

if __name__ == '__main__':
    main()

