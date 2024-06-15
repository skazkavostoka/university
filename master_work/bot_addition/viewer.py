from aiogram import Router, types, F
from aiogram.filters import or_f, StateFilter
from aiogram.filters.command import CommandStart
from aiogram import html
from aiogram.types import FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
import os

from bot_addition.keyboards import get_keyboard
from bot_addition.filters import ViewerFilter
from bot_addition import texts


viewer_router = Router()
viewer_router.message.filter(ViewerFilter(['private']))

class DataState(StatesGroup):
    choosing_data = State()
    selected_data = State()

@viewer_router.message(or_f(CommandStart(), (F.text == 'Запустить бота'), (F.text == 'Главное меню')))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(f'{html.bold(html.quote(message.from_user.full_name))},здесь Вы можете ознакомиться с интересующей'
                         f'Вас графической и статистической информацией, относящейся к защите ВКР Сааковым А.Б.',
                         reply_markup=get_keyboard(
                             'Конфигурации РНС(RNN)',
                             'Конфигурации ГНС(HNN)',
                             'Данные', sizes=(2,1)
                                ))


@viewer_router.message(F.text.casefold() == 'данные')
async def view_data(message: types.Message, state: FSMContext):
    await state.set_state(DataState.choosing_data)
    await message.answer(f'Выберите данные, с описанием, моделями прогнозирования которых хотите ознакомиться:',
                         reply_markup=get_keyboard(
                             'Nasdaq-BANK',
                             'Nasdaq-100',
                             'BTC-USD',
                             'Главное меню',
                             sizes=(2, 1, 1)
                         ))

@viewer_router.message(F.text.casefold() == 'nasdaq-bank')
async def xndx(message: types.Message, state: FSMContext):
    await state.update_data(selected_data='nasdaq-bank')
    await state.set_state(DataState.selected_data)
    await message.answer('Выберите интересующий Вас раздел: ',
                         reply_markup=get_keyboard(
                             'Описание текстом',
                             'MA100, MA250',
                             'Диаграмма рассеяния',
                             'Межквартильный размах',
                             'Назад',
                             'Главное меню',
                             sizes=(2, 2, 2)
                         ))


@viewer_router.message(F.text.casefold() == 'nasdaq-100')
async def xndx(message: types.Message, state: FSMContext):
    await state.update_data(selected_data='nasdaq-100')
    await state.set_state(DataState.selected_data)
    await message.answer('Выберите интересующий Вас раздел: ',
                         reply_markup=get_keyboard(
                             'Описание текстом',
                             'MA100, MA250',
                             'Диаграмма рассеяния',
                             'Межквартильный размах',
                             'Назад',
                             'Главное меню',
                             sizes=(2, 2, 2)
                         ))


@viewer_router.message(F.text.casefold() == 'btc-usd')
async def xndx(message: types.Message, state: FSMContext):
    await state.update_data(selected_data='btc-usd')
    await state.set_state(DataState.selected_data)
    await message.answer('Выберите интересующий Вас раздел: ',
                         reply_markup=get_keyboard(
                             'Описание текстом',
                             'MA100, MA250',
                             'Диаграмма рассеяния',
                             'Межквартильный размах',
                             'Назад',
                             'Главное меню',
                             sizes=(2, 2, 2)
                         ))



@viewer_router.message(StateFilter(DataState.selected_data), F.text.casefold() == 'описание текстом')
async def nbank_about(message: types.Message, state: FSMContext):
    data = await state.get_data()
    selected_data = data.get('selected_data')
    if selected_data == 'nasdaq-bank':
        await message.answer(f'{texts.xndx}')
    elif selected_data == 'nasdaq-100':
        await message.answer(f'{texts.ndx}')
    elif selected_data == 'btc-usd':
        await message.answer(f'{texts.btc}')


@viewer_router.message(StateFilter(DataState.selected_data), F.text.casefold() == 'ma100, ma250')
async def xndx_ma(message: types.Message, state: FSMContext):
    data = await state.get_data()
    selected_data = data.get('selected_data')
    if selected_data == 'nasdaq-bank':
        file_path = texts.path_to_xndx_ma
    elif selected_data == 'nasdaq-100':
        file_path = texts.path_to_ndx_ma
    elif selected_data == 'btc-usd':
        file_path = texts.path_to_btc_ma
    else:
        file_path = texts.path_zero
    if os.path.exists(file_path):
        photo = FSInputFile(file_path)
        await message.answer_photo(photo,
                                   caption=f"MA модели {selected_data}")
    else:
        await message.answer('Не построено для данного набора данных')



@viewer_router.message(StateFilter(DataState.selected_data), F.text.casefold() == 'диаграмма рассеяния')
async def xndx_dr(message: types.Message, state: FSMContext):
    data = await state.get_data()
    selected_data = data.get('selected_data')
    if selected_data == 'nasdaq-bank':
        file_path = texts.path_to_xndx_dr
    elif selected_data == 'nasdaq-100':
        file_path = texts.path_to_ndx_dr
    elif selected_data == 'btc-usd':
        file_path = texts.path_to_btc_dr
    else:
        file_path = texts.path_zero
    if os.path.exists(file_path):
        photo = FSInputFile(file_path)
        await message.answer_photo(photo,
                                   caption=f"Диаграмма рассеяния значений Open и Close для {selected_data}")
    else:
        await message.answer('Не построено для данного набора данных')


@viewer_router.message(StateFilter(DataState.selected_data), F.text.casefold() == 'межквартильный размах')
async def xndx_mr(message: types.Message, state: FSMContext):
    data = await state.get_data()
    selected_data = data.get('selected_data')
    if selected_data == 'nasdaq-bank':
        await message.answer(f'Результат примения метода межквартильного размаха'
                             f' по данным индекса NASDAQ BANK (XNDX)\n{texts.xndx_mr}')
    elif selected_data == 'nasdaq-100':
        await message.answer(f'Результат примения метода межквартильного размаха'
                             f' по данным индекса NASDAQ-100 (NDX)\n{texts.ndx_mr}')
    elif selected_data == 'btc-usd':
        await message.answer(f'Криптовалюты на текущим этапе своего развития имеют большую волатильность'
                             f'курса на рынке, в связи с чем количество аномалий является чрезвычайно большим.')


@viewer_router.message(StateFilter(DataState.selected_data), F.text.casefold() == 'назад')
async def go_back(message: types.Message, state: FSMContext):
    await state.set_state(DataState.choosing_data)
    await message.answer(f'Выберите данные, с описанием, моделями прогнозирования которых хотите ознакомиться:',
                         reply_markup=get_keyboard(
                             'Nasdaq-BANK',
                             'Nasdaq-100',
                             'BTC-USD',
                             'Главное меню',
                             sizes=(2, 1, 1)
                         ))



@viewer_router.message(F.text.casefold() == 'конфигурации гнс(hnn)')
async def view_gnn(message: types.Message):
    await message.answer(f'Выберите данные, с описанием, моделями прогнозирования которых хотите ознакомиться:',
                         reply_markup=get_keyboard(
                             'ГНС-1',
                             'ГНС-2',
                             'ГНС-3',
                             'ГНС-4',
                             'ГНС-5',
                             'Главное меню',
                             sizes=(2, 2, 1, 1)
                         ))


@viewer_router.message(F.text.casefold() == 'конфигурации рнс(rnn)')
async def view_rnn(message: types.Message):
    await message.answer(f'Выберите данные, с описанием, моделями прогнозирования которых хотите ознакомиться:',
                         reply_markup=get_keyboard(
                             'РНС-1',
                             'РНС-2',
                             'РНС-3',
                             'РНС-4',
                             'РНС-5',
                             'Главное меню',
                             sizes=(2, 2, 1, 1)
                         ))


@viewer_router.message(F.text.casefold() == 'рнс-1')
async def rnn_1(message: types.Message):
    await message.answer(f'{texts.rns_1}')


@viewer_router.message(F.text.casefold() == 'рнс-2')
async def rnn_2(message: types.Message):
    await message.answer(f'{texts.rns_2}')


@viewer_router.message(F.text.casefold() == 'рнс-3')
async def rnn_3(message: types.Message):
    await message.answer(f'{texts.rns_3}')


@viewer_router.message(F.text.casefold() == 'рнс-4')
async def rnn_4(message: types.Message):
    await message.answer(f'{texts.rns_4}')


@viewer_router.message(F.text.casefold() == 'рнс-5')
async def rnn_5(message: types.Message):
    await message.answer(f'{texts.rns_5}')


@viewer_router.message(F.text.casefold() == 'гнс-1')
async def rnn_1(message: types.Message):
    await message.answer(f'{texts.hnn_1}')


@viewer_router.message(F.text.casefold() == 'гнс-2')
async def rnn_2(message: types.Message):
    await message.answer(f'{texts.hnn_2}')


@viewer_router.message(F.text.casefold() == 'гнс-3')
async def rnn_3(message: types.Message):
    await message.answer(f'{texts.hnn_3}')


@viewer_router.message(F.text.casefold() == 'гнс-4')
async def rnn_4(message: types.Message):
    await message.answer(f'{texts.hnn_4}')


@viewer_router.message(F.text.casefold() == 'гнс-5')
async def rnn_5(message: types.Message):
    await message.answer(f'{texts.hnn_5}')