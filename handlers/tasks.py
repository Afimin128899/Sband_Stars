from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.flyer import get_flyer_tasks, check_task
from utils.db import add_stars

async def tasks_handler_cb(call):
    user_id = call.from_user.id
    tasks = await get_flyer_tasks(user_id, api_key="ВАШ_FLYER_API_KEY")
    if not tasks:
        await call.message.answer("❌ Нет доступных заданий")
        return
    kb = InlineKeyboardMarkup(inline_keyboard=[])
    text = "📋 Доступные задания:\n\n"
    for t in tasks:
        sig = t.get("signature") or t.get("id")
        text += f"🔹 {t.get('title','Задание')}\n💰 0.25 ⭐\n\n"
        kb.inline_keyboard.append([InlineKeyboardButton("▶️ Выполнить", callback_data=f"task_open:{sig}")])
    kb.inline_keyboard.append([InlineKeyboardButton("🔙 Назад", callback_data="back_main")])
    await call.message.answer(text, reply_markup=kb)

async def task_open_cb(call):
    sig = call.data.split(":")[1]
    user_id = call.from_user.id
    result = await check_task(api_key="ВАШ_FLYER_API_KEY", user_id=user_id, signature=sig)
    if result.get("completed"):
        add_stars(user_id, 0.25)
        await call.answer("🎉 Задание выполнено! +0.25 ⭐")
    else:
        await call.answer("❌ Задание ещё не выполнено")