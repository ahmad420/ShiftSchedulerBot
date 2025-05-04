"""
Keyboard layouts for the Shift Scheduler Bot.
"""
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton
)

from utils.translations import Language, get_translation


def get_main_menu_keyboard(is_supervisor: bool, language: Language = Language.ENGLISH) -> ReplyKeyboardMarkup:
    """
    Get the main menu keyboard based on user role.
    """
    keyboard = [
        [
            get_translation("my_shifts", language),
            get_translation("shift_schedule", language),
        ],
        [get_translation("request_swap", language)],
    ]
    
    if is_supervisor:
        keyboard.append([
            get_translation("create_shift", language),
            get_translation("manage_users", language),
        ])
    
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def get_shift_types_keyboard(language: Language = Language.ENGLISH) -> InlineKeyboardMarkup:
    """
    Get keyboard for shift types selection.
    """
    keyboard = [
        [
            InlineKeyboardButton(
                get_translation("morning_shift", language),
                callback_data="shift_type_morning"
            ),
            InlineKeyboardButton(
                get_translation("evening_shift", language),
                callback_data="shift_type_evening"
            ),
        ],
        [
            InlineKeyboardButton(
                get_translation("night_shift", language),
                callback_data="shift_type_night"
            ),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_swap_request_keyboard(shift_id: int, language: Language = Language.ENGLISH) -> InlineKeyboardMarkup:
    """
    Get keyboard for swap request actions.
    """
    keyboard = [
        [
            InlineKeyboardButton(
                get_translation("accept", language),
                callback_data=f"swap_accept_{shift_id}"
            ),
            InlineKeyboardButton(
                get_translation("reject", language),
                callback_data=f"swap_reject_{shift_id}"
            ),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_user_management_keyboard(language: Language = Language.ENGLISH) -> InlineKeyboardMarkup:
    """
    Get keyboard for user management actions.
    """
    keyboard = [
        [
            InlineKeyboardButton(
                get_translation("add_user", language),
                callback_data="user_add"
            ),
            InlineKeyboardButton(
                get_translation("edit_permissions", language),
                callback_data="user_edit"
            ),
        ],
        [
            InlineKeyboardButton(
                get_translation("delete_user", language),
                callback_data="user_delete"
            ),
        ],
    ]
    return InlineKeyboardMarkup(keyboard) 