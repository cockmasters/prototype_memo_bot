from aiogram import Router, F
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

from notes.idea import Idea
from notes.ideas import Ideas
from telegram_app.callback_factory.idea import IdeaCallback
from telegram_app.keyboards.idea import idea_keyboard, menu_idea_keyboard, new_idea_keyboard

router = Router()


class IdeaState(StatesGroup):
    writing_new_text = State()
    writing_category = State()


@router.message(F.text)
async def idea(mess: Message, state: FSMContext):
    st = await state.get_state()
    if st == IdeaState.writing_new_text:
        await mess.answer(
            text=f"Ваша новая запись:\n"
                 f"{mess.text}",
            reply_markup=new_idea_keyboard()
        )
    else:
        await mess.answer(
            text=f"Ваша запись:\n"
                 f"{mess.text}",
            reply_markup=idea_keyboard()
        )


@router.callback_query(IdeaCallback.filter(F.text == "add_idea"))
async def add_idea(callback: CallbackQuery, callback_data: CallbackData, state: FSMContext):
    text = callback.message.text.split("\n")[1]
    idea = Idea(
        id=Ideas.get_new_id(),
        text=text
    )
    Ideas.add_idea(idea)
    await state.update_data(
        idea=idea
    )
    await callback.message.edit_text(
        text=f"Вы успешно добавили запись:\n{text}",
        reply_markup=menu_idea_keyboard()
    )
    await callback.answer()


@router.callback_query(IdeaCallback.filter(F.text == "edit_idea"))
async def edit_idea(callback: CallbackQuery, callback_data: CallbackQuery, state: FSMContext):
    await state.set_state(IdeaState.writing_new_text)
    await callback.message.answer(
        text="Напишите новый текст:"
    )
    await callback.answer()


@router.callback_query(IdeaCallback.filter(F.text == "complete_edit_idea"))
async def complete_edit(callback: CallbackQuery, state: FSMContext):
    text = callback.message.text.split("\n")[1]
    idea = (await state.get_data())["idea"]
    Ideas.edit_idea(idea.id, text)
    await state.clear()
    await callback.message.edit_text(
        text="Изменения сохранены:",
        #   reply_markup=menu_idea_keyboard()
    )
    await callback.answer()


@router.callback_query(IdeaCallback.filter(F.text == "cancel_edit_idea"))
async def cancel_edit(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text(
        text="Изменения отменены"
    )
    await callback.answer()
