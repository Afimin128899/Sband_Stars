from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.db import get_user, add_withdraw

async def withdraw_menu_cb(call):
    user = get_user(call.from_user.id)
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("15 ⭐", callback_data="withdraw_15")],
        [InlineKeyboardButton("25 ⭐", callback_data="withdraw_25")],
        [InlineKeyboardButton("50 ⭐", callback_data="withdraw_50")],
        [InlineKeyboardButton("100 ⭐", callback_data="withdraw_100")],
        [InlineKeyboardButton("🔙 Назад", callback_data="back_main")]
    ])
    await call.message.answer(f"💸 Ваш баланс: {user[1]} ⭐\nВыберите сумму для вывода:", reply_markup=kb)

async def withdraw_request_cb(call):
    amount = int(call.data.split("_")[1])
    user = get_user(call.from_user.id)
    if user[1] >= amount:
        add_withdraw(call.from_user.id, amount)
        await call.answer(f"✅ Заявка на вывод {amount} ⭐ отправлена!")
    else:
        await call.answer("❌ Недостаточно звёзд для вывода")