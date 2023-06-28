import random
from pyrogram import Client
from pyrogram.errors import SessionPasswordNeeded
from .conf import TELEGRAM_API_ID, TELEGRAM_API_HASH

class Sender:
    def __init__(self, name_account):
        api_id = TELEGRAM_API_ID
        api_hash = TELEGRAM_API_HASH
        self.name_account = name_account
        self.client = Client(name_account, api_id, api_hash)

    async def connect(self):
        await self.client.connect()

    async def send_code(self, number):
        return await self.client.send_code(number)

    async def sign_in(self, number, phone_code_hash, code, tfa=None):
        try:
            await self.client.sign_in(phone_number=number, phone_code_hash=phone_code_hash, phone_code=code)
        except SessionPasswordNeeded as e:
            await self.client.check_password(tfa)

    async def get_chats(self):
        return await self.client.get_dialogs()

    async def send(self):
        await self.client.send_message('t.me/+NxynK3HfjK82NzYy', 'hi')

    async def mass_send(self, chat_id_from, chat_ids_to):
        posts = await self.client.get_chat_history(chat_id_from, limit=100)
        random_index = random.randint(0, len(posts) - 2)
        message = posts[random_index]

        for chat_id_to in chat_ids_to:
            await self.client.forward_messages(chat_id_to, chat_id_from, message.message_id)

    async def disconnect(self):
        await self.client.disconnect()

    async def log_out(self):
        await self.client.log_out()

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()
