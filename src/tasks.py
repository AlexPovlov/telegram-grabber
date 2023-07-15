from fastapi_utils.tasks import repeat_every

from .deps import spam_service
from datetime import datetime


@repeat_every(seconds=60)
async def mass_send():
    service = spam_service()
    schedules = await service.spams()
    for schedule in schedules:
        print(schedule.time.strftime("%H:%M"))
        if schedule.time.strftime("%H:%M") == datetime.now().strftime("%H:%M"):
            chat = await schedule.chat
            account = await chat.account
            to_chats = await schedule.to_chats
            await service.send(account.phone, chat.chat_id, to_chats)


async def tasks():
    await mass_send()
