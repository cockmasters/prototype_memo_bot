from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from telegram_app.callback_factory.idea import IdeaCallback


def idea_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Добавить идею",
        callback_data=IdeaCallback(
            text="add_idea"
        )
    )
    return builder.as_markup()


def menu_idea_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Отредактировать",
        callback_data=IdeaCallback(
            text="edit_idea"
        )
    )
    builder.button(
        text="Добавить категорию",
        callback_data=IdeaCallback(
            text="categorise_idea"
                                   )
    )
    builder.adjust(1)
    return builder.as_markup()


def new_idea_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Подтвердить",
        callback_data=IdeaCallback(
            text="complete_edit_idea"
        )
    )
    builder.button(
        text="Отменить",
        callback_data=IdeaCallback(
            text="cancel_edit_idea"
        )
    )
    return builder.as_markup()
