from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_keyboard(
        *btns: str,
        placeholder: str=None,
        sizes: tuple[int] = (2,),
        page: int=1,
        total_pages: int=1
):
    keyboard = ReplyKeyboardBuilder()
    for index, text in enumerate(btns, start=0):
        keyboard.add(KeyboardButton(text=text))

    if page > 1:
        keyboard.row(KeyboardButton(text='<<'), KeyboardButton(text='>>'))
    elif page < total_pages:
        keyboard.row(KeyboardButton(text='Меню'), KeyboardButton(text='>>'))
    return keyboard.adjust(*sizes).as_markup(
        resize_keyboard = True, input_field_placeholder=placeholder)

back_kb = get_keyboard(
    'Назад',
    'Меню'
)