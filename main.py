from aiogram import types
from aiogram.filters import CommandStart

from PIL import Image, ImageDraw, ImageFont

import logging
import asyncio
import sys
import os

from loader import bot, dp


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    image = Image.open("your_signa.jpg")
    draw = ImageDraw.Draw(image)

    x = 350
    y = 430
    text = message.from_user.first_name
    if len(text) > 16:
        text = text[:16] + '...'
    draw.text((x, y), text, fill="white", font=ImageFont.truetype("arial.ttf", size=64))
    image.save(f"{message.from_user.id}.jpg")

    await message.answer_photo(photo=types.FSInputFile(path=f'{message.from_user.id}.jpg'),
                               caption='сигначлен бот')
    os.remove(f'{message.from_user.id}.jpg')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
