import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters.command import Command
from aiogram.types import FSInputFile

from core.keybord.reply import help_keyboard, fraction, week
from core.settings import settings
from core.keybord.inline import select_book


async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    @dp.message(Command("start"))
    async def get_start(message: types.Message):
        await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}. Рад тебя видеть')

    @dp.message(Command("help"))
    async def cmd_help(message: types.Message):
        await message.answer("Чем я могу тебе помочь?", reply_markup=help_keyboard)

    @dp.message(Command("cansel"))
    async def cmd_help(message: types.Message):
        await message.answer("Действие отменено")

    @dp.message(Command("shut_down"))
    async def cmd_stop(message: types.Message):
        await bot.send_message(message.from_user.id, f'До новых встреч {message.from_user.first_name}.')

    @dp.message(F.text == "Расписание")
    async def timetable(message: types.Message):
        await bot.send_message(message.from_user.id, f'Сейчас числитель или знаменатель?', reply_markup=fraction)

    @dp.message(F.text == "Числитель")
    async def chisl(message: types.Message):
        await bot.send_message(message.from_user.id, f'Какой сейчас день недели?', reply_markup=week)
       #global fraction_answer
       #fraction_answer = "Числитель"

    @dp.message(F.text == "Знаменатель")
    async def znam(message: types.Message):
        await bot.send_message(message.from_user.id, f'Какой сейчас день недели?', reply_markup=week)
        #global fraction_answer
        #fraction_answer = "Знаменатель"

    @dp.message(F.text == "Выход")
    async def cmd_help(message: types.Message):
        await message.answer("Был рад помочь. Обращайтесь еще☺️")

    @dp.message(F.text == "Понедельник")
    async def image(message: types.Message):
        photo = FSInputFile(r'core/IMAGE/Ponedilnic.png')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)

    @dp.message(F.text == "Вторник")
    async def image(message: types.Message):
        photo = FSInputFile(r'core/IMAGE/BTORNIC.png')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)

    @dp.message(F.text == "Среда")
    async def image(message: types.Message):
        photo = FSInputFile(r'core/IMAGE/925782388857435623_-498320278638945136.png')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)

    @dp.message(F.text == "Четверг")
    async def image(message: types.Message):
        photo = FSInputFile(r'core/IMAGE/chetwerg.png')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)

    @dp.message(F.text == "Пятница")
    async def image(message: types.Message):
        photo = FSInputFile(r'core/IMAGE/PATNICA.png')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)

    @dp.message(F.text == "Кто мы?")
    async def send_photo_with_text(message: types.Message):
        photo = FSInputFile(r'core/IMAGE/mi.jpg')
        await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'<tg-spoiler>Какие мы я тут '
                                                                           f'один</tg-spoiler>', reply_markup=select_book)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    # Запуск бота

    asyncio.run(start())
