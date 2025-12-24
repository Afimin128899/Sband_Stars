from aiogram.types import Message
from utils.db import add_user
from keyboards.main import main_menu

async def start_command(message: Message):
    add_user(message.from_user.id)
    await message.answer(f"Привет, {message.from_user.full_name}! 👋\nДобро пожаловать в Sband_Stars.", reply_markup=main_menu())