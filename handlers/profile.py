from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.db import get_user

async def profile_cb(call):
    user_id = call.from_user.id
    user = get_user(user_id)
    text = (f"👤 Профиль\n\n"
            f"⭐ Баланс: {user[1]}\n"
            f"💸 Всего выведено: {user[2]}\n"
            f"👥 Приглашено людей: {user[3]}\n"
            f"🔗 Ваша реферальная ссылка: https://t.me/ВАШ_BOT_USERNAME?start={user_id}")
    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("🔙 Назад", callback_data="back_main")]])
    await call.message.answer(text, reply_markup=kb)