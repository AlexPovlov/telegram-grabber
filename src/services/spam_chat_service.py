import random
from fastapi import Depends, HTTPException

from src.repositories.spam_chat_repository import SpamChatRepository
from src.libs.tele_sender import Sender


class SpamChatService:
    def __init__(self, repo: SpamChatRepository = Depends(SpamChatRepository)):
        self.repo = repo

    async def set_spam_chats(self, chats: set, chat_id: int, time):
        spam_chat = await self.repo.create({"chat_id": chat_id, "time": time})
        for chat in chats:
            await spam_chat.to_chats.add(chat)

    async def delete(self, spam_id):
        spam = await self.repo.get(spam_id)

        if not spam:
            raise HTTPException(status_code=404, detail="Spam not found")

        await self.repo.delete(spam)

    async def spams(self):
        return await self.repo.get_all()

    async def mass_send(self):
        spams = await self.spams()

        for spam in spams:
            await self.send(spam.account.phone, spam.chat.chat_id, spam.to_chats)

    async def one_send(self, spam_id):
        spam = await self.repo.get(spam_id)
        chat = await spam.chat
        account = await chat.account
        to_chats = await spam.to_chats
        await self.send(account.phone, chat.chat_id, to_chats)

    async def send(self, name, from_chat, to_chats):
        async with Sender(name) as sender:
            chat_from = await sender.get_entity(int(from_chat))
            posts = await sender.get_messages(chat_from, 100)
            random_index = random.randint(0, len(posts) - 2)
            message = posts[random_index]

            for chat in to_chats:
                chat_to = await sender.get_entity(int(chat.chat_id))
                await sender.forward_messages(chat_to, message)
