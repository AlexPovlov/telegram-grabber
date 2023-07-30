from .deps import spam_service, filter_service, account_service
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

async def mass_send():
    try:
        service = spam_service()
        schedules = await service.spams()
        for schedule in schedules:
            print(schedule.time.strftime("%H:%M"))
            if schedule.time.strftime("%H:%M") == datetime.now().strftime("%H:%M"):
                chat = await schedule.chat
                account = await chat.account
                to_chats = await schedule.to_chats
                await service.send(account.phone, chat.chat_id, to_chats)
    except:
        pass

async def sosat_spamers():
    try:
        service = filter_service()
        a_service = account_service()
        accounts = await a_service.get_all()
        for account in accounts:
            await service.idi_nahui_spamer(account.phone)
    except:
        pass
    

async def tasks():
    scheduler = AsyncIOScheduler(timezone="Europe/Berlin")
    scheduler.add_job(sosat_spamers, 'interval', seconds=60)
    scheduler.add_job(mass_send, 'interval', seconds=60)
    scheduler.start()
