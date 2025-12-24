from flyerapi import Flyer

async def get_flyer_tasks(user_id: int, api_key: str):
    flyer = Flyer(api_key)
    try:
        tasks = flyer.get_tasks(user_id=user_id, language_code="ru", limit=5)
        return tasks
    except Exception as e:
        print(f"[FlyerAPI Error] {e}")
        return []

async def check_task(api_key: str, user_id: int, signature: str):
    flyer = Flyer(api_key)
    try:
        result = flyer.check_task(user_id=user_id, signature=signature, language_code="ru")
        return result
    except Exception as e:
        print(f"[FlyerAPI Check Error] {e}")
        return {"completed": False}