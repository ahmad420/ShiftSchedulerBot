"""
Main entry point for the Shift Scheduler Bot.
"""
import logging
import os
from typing import Dict, Any

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)

from bot.commands.basic_commands import my_shifts, schedule, swap_request
from bot.commands.admin_commands import create_shift, assign_shift, approve_swap, manage_users
from bot.handlers.handlers import handle_message, handle_callback, handle_error
from bot.keyboards.keyboards import get_main_menu_keyboard
from db.models.user import User
from utils.translations import Language, get_translation

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot states
START, MAIN_MENU = range(2)

# Bot token
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start command handler."""
    user = update.effective_user
    language = Language.ENGLISH  # Default language
    
    # TODO: Get user's preferred language from database
    # user = await get_user_by_telegram_id(user.id)
    # if user:
    #     language = user.language
    
    await update.message.reply_text(
        get_translation("welcome_message", language).format(
            first_name=user.first_name
        ),
        reply_markup=get_main_menu_keyboard(False)
    )
    return MAIN_MENU


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Help command handler."""
    user = update.effective_user
    language = Language.ENGLISH  # Default language
    
    # TODO: Get user's preferred language from database
    # user = await get_user_by_telegram_id(user.id)
    # if user:
    #     language = user.language
    
    help_text = get_translation("help_text", language)
    await update.message.reply_text(help_text)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log errors caused by updates."""
    logger.error(f"Update {update} caused error {context.error}")


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token
    application = Application.builder().token(TOKEN).build()

    # Add conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START: [MessageHandler(filters.TEXT & ~filters.COMMAND, start)],
            MAIN_MENU: [
                CommandHandler("help", help_command),
                CommandHandler("myshift", my_shifts),
                CommandHandler("schedule", schedule),
                CommandHandler("swap", swap_request),
                CommandHandler("create_shift", create_shift),
                CommandHandler("assign_shift", assign_shift),
                CommandHandler("approve_swap", approve_swap),
                CommandHandler("manage_users", manage_users),
                MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message),
                CallbackQueryHandler(handle_callback),
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    application.add_handler(conv_handler)
    application.add_error_handler(error_handler)

    # Start the Bot
    application.run_polling()


if __name__ == "__main__":
    main() 