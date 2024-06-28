from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon import LEXICON
from keyboards import menu_kb, yes_no_kb
from parsing import get_bludo
from aiogram.types import FSInputFile

router = Router()

# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'], reply_markup=yes_no_kb)


# Этот хэндлер срабатывает на согласие пользователя показать ему рецепт
@router.message(F.text == LEXICON['yes_button'])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON['yes'], reply_markup=menu_kb)


# Этот хэндлер срабатывает на отказ пользователя
@router.message(F.text == LEXICON['no_button'])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON['no'])
    
    
@router.message(F.text.in_(LEXICON['topics']))
async def process_game_button(message: Message):
    receipt =get_bludo(LEXICON['topics'][message.text])
    photo = FSInputFile('pici.jpg')
    await message.answer_photo(photo) 
    await message.answer(text=receipt)
    await message.answer(text=LEXICON['add_answer'], reply_markup=yes_no_kb)
    
# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON['other_answer'])