import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.filters import Command

# 🔐 Токен бота
TOKEN = "7337118484:AAGTyLOR9SBCOtolh1Skm4n7AIELSU7utZc"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# 🔹 Кнопки
btn_what_happened = KeyboardButton(text="Что же случилось?")
btn_who_is_she = KeyboardButton(text="Кто же она?")
btn_how_help = KeyboardButton(text="Чем я могу помочь?")

# 🔹 Клавиатуры
kb_what_happened = ReplyKeyboardMarkup(keyboard=[[btn_what_happened]], resize_keyboard=True)
kb_who_is_she = ReplyKeyboardMarkup(keyboard=[[btn_who_is_she]], resize_keyboard=True)
kb_how_help = ReplyKeyboardMarkup(keyboard=[[btn_how_help]], resize_keyboard=True)

# 🔹 Кнопка "Войти в портал"
portal_button = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Войти в портал", url="https://t.me/+SJW_MsOMcBkwM2Uy")]]
)

# 🔹 Тексты
story_part_1 = """💫 В самом сердце Великого Цикла, на пересечении прошлого и будущего, раскинулось Королевство Блаженство. Здесь люди пребывали в гармонии с Потоком, всё текло в ритме солнечного круга, и каждый знал свою истинную природу. Они жили в созерцании, творчестве и радости, ведь Генные Ключи сияли в их сердцах, открывая двери к новым возможностям.

Но раз в год происходило нечто особенное - открывались Врата Нового Цикла. Солнце входило в 41-е Врата, открывая перед человеком видение своей судьбы на грядущий год.

Шесть дней шло это Волшебное Погружение, и каждый из дней показывал новую часть карты судьбы, направляя странников на их истинный путь.

В этом году великий день пришелся на вечер 21 января, но  всё пошло не так... """

story_part_2 = """Мир Блаженства затянуло серым туманом Забвения. Люди перестали видеть мечты, забыли, кто они, зачем пришли и в чём их дар. Они бродили в тишине, словно их души окутал сон.

Скорбница Времени знала: если люди утратят связь со своими Генными Ключами, если перестанут мечтать, осознавать и следовать своей Истине, она получит власть над миром. Поэтому она вплела в их сознание сомнения, тревоги, усталость и страх, превратив их мечты в иллюзии. Люди блуждали в собственных фантазиях, создавая себе преграды, которых не существовало, и убеждая себя, что не могут начать, что не время, что не получится.

Теперь весь мир бродил во сне, не видя путей к пробуждению.

Врата Нового Цикла открылись, но никто не вошел в них.

Но одна малышка оказалась Скорбнице не по зубам...."""

story_part_3 = """👑 Царевна Блажена чувствовала: Королевство можно спасти! ✨

С ней была ее наставница Дари — Сказочница, Плетущая Нити Реальности. Она знала, как оживить забытые мечты и вернуть людям их предназначение. Её слова пробуждали, а истории вплетали в сердца огонь истинного пути.

— Нам нужно активировать Кристалл Пробуждения! — воскликнула юная Царевна.

— Да, но он действует только тогда, когда достаточно людей помнит себя... — задумчиво сказала Дари.

🔥 Ты нужен нам! 🔥"""

mission_text = """📜 Твоя первая миссия: ✨ передай Искру другому! ✨

🌞 Как это сделать?

1️⃣ Поделись этим свитком в соцсетях (Instagram, Telegram, чаты, блоги) — или пригласи хотя бы одного человека в путешествие лично.

Тот, кто спит, не сможет пробудить Королевство.

3️⃣ Пришли скрин в бота следующим сообщением — и врата Портала откроются перед тобой.

💡 Чем больше людей увидят свет Свитка, тем быстрее растает Туман Забвения!

⚡ Цикл уже запущен, Время уходит! ⏳
Ты готов создать своё будущее?"""

portal_text = "🔮 Портал открыт! Вот твоя ссылка"

# 🔹 Обработчики команд и сообщений
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer(story_part_1, reply_markup=kb_what_happened)

@dp.message()
async def handle_message(message: Message):
    if message.text == "Что же случилось?":
        await message.answer(story_part_2, reply_markup=kb_who_is_she)
    elif message.text == "Кто же она?":
        await message.answer(story_part_3, reply_markup=kb_how_help)
    elif message.text == "Чем я могу помочь?":
        # 🔹 Здесь удаляем кнопки после запроса фото
        await message.answer(mission_text, reply_markup=ReplyKeyboardRemove())
    elif message.photo:  # Человек отправил фото (скрин)
        await message.answer(portal_text, reply_markup=portal_button)

# Запуск бота
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
