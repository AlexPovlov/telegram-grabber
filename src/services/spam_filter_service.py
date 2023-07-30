from fastapi import Depends, HTTPException
from telethon.tl.types import InputPeerEmpty, PeerUser, User

from src.repositories.spam_filter_repository import SpamFilterRepository
from src.libs.tele_sender import Sender
import datetime

class SpamFilterService:
    def __init__(self, repo: SpamFilterRepository = Depends(SpamFilterRepository)):
        self.repo = repo

    async def get_all(self):
        return await self.repo.get_all()

    async def get_from_id(self, id):
        filter = await self.repo.get(id)

        if not filter:
            raise HTTPException(status_code=404, detail="Filter not found")

        return filter

    async def create(self, text):
        await self.repo.create({"text": text})

    async def edit(self, filter_id, text):
        filter = await self.get_from_id(filter_id)
        return await self.repo.update(filter, {"text": text})

    async def delete(self, filter_id):
        filter = await self.get_from_id(filter_id)
        await self.repo.delete(filter)

    async def idi_nahui_spamer(self, phone):
        async with Sender(phone) as sender:
            chats = await sender.get_chats(offset_date=datetime.datetime.now()- datetime.timedelta(days=1), limit=500)
            filters = await self.get_all()
            for chat in chats:
                if chat.unread_count > 0 and isinstance(chat.entity, User):
                    messages = await sender.get_messages(chat)
                    for message in messages:
                        for filter in filters:
                            if filter.text in message.message.lower():
                                await sender.block(message.sender_id)
                                await sender.report(chat.entity, message.id)
                                await sender.clean(chat.entity)
                                print(f"От: {message.sender.first_name}")
                                print(f"Сообщение: {message.message}")
                                break
