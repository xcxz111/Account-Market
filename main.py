from pathlib import Path

from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

from loguru import logger
from telegram.ext.filters import REPLY

from config import TOKEN
from const_strings import HOME, CABINET, BILLING, ADMIN, TELEGRAM, INSTAGRAM, GMAIL, BUY_TELEGRAM_ACCOUNT, \
    BACK_HOME, BACK_TELEGRAM, TG_FORMAT, BACK_TG_FORMAT, PARTNERSHIP
from reply import home_reply, cabinet_reply, billing_reply, admin_reply, telegram_reply, instagram_reply, gmail_reply, \
    buy_telegram_account_reply, back_home_reply, back_buy_telegram_account_reply, tg_format_reply, back_tg_format_reply, \
    partnership_replay
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
    BILLING: billing_reply,
    ADMIN: admin_reply,
    TELEGRAM: telegram_reply,
    INSTAGRAM: instagram_reply,
    GMAIL: gmail_reply,
    BUY_TELEGRAM_ACCOUNT: buy_telegram_account_reply,
    BACK_HOME: back_home_reply,
    BACK_TELEGRAM: back_buy_telegram_account_reply,
    TG_FORMAT: tg_format_reply,
    BACK_TG_FORMAT: back_tg_format_reply,
    PARTNERSHIP: partnership_replay,



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

