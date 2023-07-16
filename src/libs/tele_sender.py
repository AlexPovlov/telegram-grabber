from telethon import TelegramClient, errors

from src.conf import (
    TELEGRAM_API_HASH,
    TELEGRAM_API_ID,
    TELEGRAM_APP_VERSION,
    TELEGRAM_DEVICE,
)


class Sender:
    def __init__(self, name_account):
        self.name_account = name_account
        self.client = TelegramClient(
            name_account,
            api_id=TELEGRAM_API_ID,
            api_hash=TELEGRAM_API_HASH,
            system_version="4.16.30-vxCUSTOM",
            device_model=TELEGRAM_DEVICE,
            app_version=TELEGRAM_APP_VERSION,
        )

    async def connect(self):
        await self.client.connect()

    async def send_code(self, number):
        return await self.client.send_code_request(number)

    async def sign_in(self, number, phone_code_hash, code, tfa=None):
        try:
            await self.client.sign_in(
                number, code, password=tfa, phone_code_hash=phone_code_hash
            )
        except errors.SessionPasswordNeededError:
            await self.client.sign_in(password=tfa)
        except Exception as e:
            raise e

    async def get_chats(self, limit=10):
        # dialogs = await self.client.get_dialogs(limit=10)
        # # print(dialogs)
        return await self.client.get_dialogs(limit=limit)

    async def send(self):
        chat = await self.client.get_entity("")
        await self.client.send_message(chat, "hi")

    async def get_entity(self, chat_id):
        return await self.client.get_entity(int(chat_id))

    async def get_messages(self, chat_from, limit=10):
        return await self.client.get_messages(chat_from, limit=limit)

    async def forward_messages(self, chat_to, message):
        return await self.client.forward_messages(chat_to, message)

    # async def mass_send(self, chat_id_from, chat_ids_to):
    #     chat_from = await self.client.get_entity(int(chat_id_from))
    #     posts = await self.client.get_messages(chat_from, 100)
    #     random_index = random.randint(0, len(posts) - 2)
    #     message = posts[random_index]

    #     for chat_id_to in chat_ids_to:
    #         chat_to = await self.client.get_entity(int(chat_id_to))
    #         await self.client.forward_messages(chat_to, message)

    async def disconnect(self):
        await self.client.disconnect()

    async def log_out(self):
        await self.client.log_out()

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()
