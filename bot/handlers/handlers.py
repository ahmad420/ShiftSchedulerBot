"""
Message and callback handlers for the Shift Scheduler Bot.
"""
from typing import Dict, Any

from telegram import Update
from telegram.ext import ContextTypes

from bot.keyboards.keyboards import (
    get_main_menu_keyboard,
    get_shift_types_keyboard,
    get_swap_request_keyboard,
    get_user_management_keyboard,
)
from utils.translations import Language, get_translation


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming messages."""
    user = update.effective_user
    language = Language.ENGLISH  # Default language
    
    # TODO: Get user's preferred language from database
    # user = await get_user_by_telegram_id(user.id)
    # if user:
    #     language = user.language
    
    text = update.message.text
    
    if text == get_translation("my_shifts", language):
        # TODO: Get user's shifts from database
        await update.message.reply_text(
            get_translation("no_shifts_found", language)
        )
    
    elif text == get_translation("shift_schedule", language):
        # TODO: Get department schedule from database
        await update.message.reply_text(
            get_translation("no_schedule_found", language)
        )
    
    elif text == get_translation("request_swap", language):
        # TODO: Get available shifts for swap
        await update.message.reply_text(
            get_translation("no_shifts_available", language),
            reply_markup=get_shift_types_keyboard(language)
        )
    
    elif text == get_translation("create_shift", language):
        # TODO: Check if user is supervisor
        await update.message.reply_text(
            get_translation("create_shift_prompt", language)
        )
    
    elif text == get_translation("manage_users", language):
        # TODO: Check if user is supervisor
        await update.message.reply_text(
            get_translation("manage_users_prompt", language),
            reply_markup=get_user_management_keyboard(language)
        )
    
    else:
        await update.message.reply_text(
            get_translation("unknown_command", language)
        )


async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle callback queries."""
    query = update.callback_query
    user = update.effective_user
    language = Language.ENGLISH  # Default language
    
    # TODO: Get user's preferred language from database
    # user = await get_user_by_telegram_id(user.id)
    # if user:
    #     language = user.language
    
    await query.answer()
    
    if query.data.startswith("shift_type_"):
        shift_type = query.data.split("_")[2]
        # TODO: Process shift type selection
        await query.edit_message_text(
            get_translation("shift_selected", language).format(
                shift_type=get_translation(f"{shift_type}_shift", language)
            )
        )
    
    elif query.data.startswith("swap_"):
        action, shift_id = query.data.split("_")[1:]
        # TODO: Process swap request
        if action == "accept":
            await query.edit_message_text(
                get_translation("swap_accepted", language)
            )
        else:
            await query.edit_message_text(
                get_translation("swap_rejected", language)
            )
    
    elif query.data.startswith("user_"):
        action = query.data.split("_")[1]
        # TODO: Process user management action
        if action == "add":
            await query.edit_message_text(
                get_translation("add_user_prompt", language)
            )
        elif action == "edit":
            await query.edit_message_text(
                get_translation("edit_permissions_prompt", language)
            )
        else:
            await query.edit_message_text(
                get_translation("delete_user_prompt", language)
            )


async def handle_error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle errors."""
    language = Language.ENGLISH  # Default language
    
    # TODO: Get user's preferred language from database
    # if update.effective_user:
    #     user = await get_user_by_telegram_id(update.effective_user.id)
    #     if user:
    #         language = user.language
    
    error_message = get_translation("error_occurred", language)
    if update.effective_message:
        await update.effective_message.reply_text(error_message) 