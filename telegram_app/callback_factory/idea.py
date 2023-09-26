from aiogram.filters.callback_data import CallbackData


class IdeaCallback(CallbackData, prefix="idea"):
    text: str
