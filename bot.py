import asyncio
from aiogram import Bot, Dispatcher, F
from handlers import start, tasks, profile, withdraw, admin
from keyboards.main import main_menu

BOT_TOKEN = "ВАШ_BOT_TOKEN"
ADMIN_ID = 548858090
FLYER_API_KEY = "ВАШ_FLYER_API_KEY"

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

dp.message.register(start.start_command, F.text.startswith("/start"))
dp.callback_query.register(tasks.tasks_handler_cb, F.data == "tasks")
dp.callback_query.register(tasks.task_open_cb, F.data.startswith("task_open:"))
dp.callback_query.register(profile.profile_cb, F.data == "profile")
dp.callback_query.register(withdraw.withdraw_menu_cb, F.data == "withdraw")
dp.callback_query.register(withdraw.withdraw_request_cb, F.data.startswith("withdraw_"))
dp.message.register(admin.admin_give_stars_cb)
dp.callback_query.register(admin.admin_withdraw_cb)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())