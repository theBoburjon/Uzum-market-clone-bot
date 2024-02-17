import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery
from aiogram.types import Message, BotCommand
from root import TOKEN
from button import buttons
from btnin import catalog, catalog1, catalog2, catalog3, catalog4, catalog5

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer_photo(photo="https://daryo.uz/static/2023/06/6489641736aff.png",
                               caption=f"Assalomu Alaykum {message.from_user.full_name} Uzum Market 🏰 Botimizga xush kelibsiz 🖐!,",
                               reply_markup=buttons)


@dp.message()
async def echo(message: Message):
    await message.answer(message.text)


@dp.message(F.text == "Telefonlar")
async def cmd_phones(message: Message):
    await message.answer_photo(photo="https://images.uzum.uz/cmru4uh25ku8ad8j8e0g/original.jpg",
                               caption="Смартфон TECNO Spark Go 2024", reply_markup=catalog),

    await message.answer_photo(photo="https://images.uzum.uz/cmrienps99ouqbfsbeig/original.jpg",
                               caption="Смартфон Samsung Galaxy A24, 6/128 ГБ, 6.5 50 mp, \n 90hz, sAMOLED, 2SIM, Android 13",
                               reply_markup=catalog1),
    await message.answer_photo(photo="https://images.uzum.uz/cmrih8p25ku8ad8j4iv0/original.jpg",
                               caption="Смартфон Samsung Galaxy A54 5G 6/128, 8/256, 6.4 50mp, 120hz, sAMOLED, IP67, 2SIM",
                               reply_markup=catalog2),
    await message.answer_photo(photo="https://images.uzum.uz/clouns7n7c6gg9ie7020/original.jpg",
                               caption="Смартфон iPhone 15 pro, \n 128 ГБ SIM ACTIVE IMEI",
                               reply_markup=catalog3)


@dp.message(F.text == "Aksessuarlar")
async def cmd_aksessuarlar(message: Message):
    await message.answer_photo(photo="https://images.uzum.uz/ckme514jvf2tgsrpdlj0/original.jpg",
                               caption="Зарядное устройство, адаптер, \n блок питания USB-C для iPhone Type-C, 25W, PD",
                               reply_markup=catalog4)

    await message.answer_photo(photo="https://images.uzum.uz/cio1rdf5d7kom1tjr1i0/original.jpg",
                               caption="Штатив-монопод Jmary MT-39 для телефона,\n камеры и кольцевой подсветки Go Pro",
                               reply_markup=catalog5)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    bot = Bot(token=TOKEN)
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
