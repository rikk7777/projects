from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon import LEXICON

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

# Создаем кнопки с ответами согласия и отказа
button_yes = KeyboardButton(text=LEXICON['yes_button'])
button_no = KeyboardButton(text=LEXICON['no_button'])

# Инициализируем билдер для клавиатуры с кнопками "Давай" и "Не хочу!"
yes_no_kb_builder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с аргументом width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# ------- Создаем клавиатуру без использования билдера -------

# Создаем кнопки меню
button_1 = KeyboardButton(text='Супы')
button_2 = KeyboardButton(text='Десерты и выпечка')
button_3 = KeyboardButton(text='Салаты')
button_4 = KeyboardButton(text='Завтраки')
button_5 = KeyboardButton(text='Закуски')
button_6 = KeyboardButton(text='Напитки')
button_7 = KeyboardButton(text='Заготовки')
button_8 = KeyboardButton(text='Несладкая выпечка')
button_9 = KeyboardButton(text='Вторые блюда')

# Создаем клавиатуру с категориями блюд
menu_kb = ReplyKeyboardMarkup(
    keyboard=[[button_1, button_2, button_3],
              [button_4, button_5, button_6],
              [button_7, button_8, button_9]],
    resize_keyboard=True
)