
import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton
)

# 1. Bot tokeni
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN topilmadi! Tokenni sozlang.")

# 2. Bot va Dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()


# 3. Tugmalar yaratamiz
button1 = KeyboardButton(text="📚 Kurslar")
button2 = KeyboardButton(text="🕒 Dars jadvali")
button3 = KeyboardButton(text="👨‍💻 IT haqida")
button4 = KeyboardButton(text="📞 Aloqa")
button5 = KeyboardButton(text="🪙 Coinlar")


# 4. Klaviatura yaratamiz
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [button1, button2],
        [button3, button4],
        [button5]
    ],
    resize_keyboard=True
)


# 5. Start komandasi
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Assalomu alaykum! IT LIVE botiga xush kelibsiz! 🚀\n\n"
        "Kerakli bo'limni tanlang:",
        reply_markup=keyboard
    )


# 6. Help komandasi
@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "Botdan foydalanish uchun quyidagi tugmalardan foydalaning.",
        reply_markup=keyboard
    )


# 7. Kurslar tugmasi
@dp.message(F.text == "📚 Kurslar")
async def courses(message: Message):
    await message.answer(
        "📚 Bizning kurslarimiz:\n\n"
        "1. Python\n"
        "2. C++\n"
        "3. Frontend\n\n"
        "O'zingizga kerakli yo'nalishni tanlang!"
    )


# 8. Dars jadvali tugmasi
@dp.message(F.text == "🕒 Dars jadvali")
async def schedule(message: Message):
    await message.answer(
        "🕒 Dars jadvalimiz:\n\n"
        "Darslar haftaning dushanba-shanba kunlari o'tiladi."
    )


# 9. IT haqida tugmasi
@dp.message(F.text == "👨‍💻 IT haqida")
async def about_it(message: Message):
    await message.answer(
        "👨‍💻 IT — axborot texnologiyalari sohasi.\n\n"
        "Bu sohada:\n"
        "💻 Dasturlash\n"
        "🎨 Grafik dizayn\n"
        "🌐 Web dasturlash\n"
        "🤖 Sun'iy intellekt\n"
        "kabi yo'nalishlar mavjud."
    )


# 10. Aloqa tugmasi
@dp.message(F.text == "📞 Aloqa")
async def contact(message: Message):
    await message.answer(
        "📞 Biz bilan bog'lanish uchun:\n\n"
        "Administrator: IT LIVE\n"
        "Telefon: 88 713 06 36"
    )


# 11. Coinlar tugmasi
@dp.message(F.text == "🪙 Coinlar")
async def coins(message: Message):
    await message.answer(
        "🪙 Coinlaringiz haqida ma'lumot olish uchun "
        "administratorga murojaat qiling.\n\n"
        "Telefon: 88 713 06 36"
    )


# 12. Noma'lum xabarlar
@dp.message()
async def unknown(message: Message):
    await message.answer(
        "Kechirasiz, bu xabarni tushunmadim. 🤔\n\n"
        "Iltimos, menyudagi tugmalardan foydalaning.",
        reply_markup=keyboard
    )

print("1. Fayl ishga tushdi")

async def main():
    print("2. Main funksiyasi ishga tushdi")

    await dp.start_polling(bot)

if __name__ == "__main__":
    print("3. Asosiy blok ishga tushdi")
    asyncio.run(main())