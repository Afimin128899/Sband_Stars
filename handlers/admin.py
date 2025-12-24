from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from utils.db import get_withdraws, set_withdraw_status, add_stars
ADMIN_ID = 548858090

async def admin_give_stars_cb(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    parts = message.text.split()
    if len(parts) < 4:
        await message.answer("Использование: /give <user_id> <stars> <reason>")
        return
    user_id, stars, reason = int(parts[1]), float(parts[2]), " ".join(parts[3:])
    add_stars(user_id, stars)
    await message.answer(f"✅ Выданы {stars} ⭐ пользователю {user_id}\nПричина: {reason}")

async def admin_withdraw_cb(call):
    if call.from_user.id != ADMIN_ID:
        return
    parts = call.data.split("_")
    withdraw_id = int(parts[1])
    action = parts[2]
    if action == "approve":
        set_withdraw_status(withdraw_id, "completed")
        await call.answer("✅ Вывод одобрен")
    elif action == "reject":
        reason = "Причина отклонения"
        set_withdraw_status(withdraw_id, "rejected", reason)
        await call.answer(f"❌ Вывод отклонён. {reason}")