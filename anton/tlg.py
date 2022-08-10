import asyncio
import os
from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv()

api_id = os.getenv("TG_API_ID")
api_hash = os.getenv("TG_API_HASH")
bot_token = os.getenv("TG_BOT_TOKEN")

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


@bot.on(events.NewMessage)
async def my_event_handler(event):
    if "Привет" in event.raw_text:
        await event.reply('Привет и тебе!')


@bot.on(events.NewMessage(pattern=r'\.save'))
async def handler(event):
    if event.is_reply:
        replied = await event.get_reply_message()
        sender = replied.sender
        await bot.download_profile_photo(sender)
        await event.respond(f"Фотография пользователя «{sender.username}» сохранена!")

        await bot.delete_messages(replied.peer_id, [event.id, replied.id])


@bot.on(events.NewMessage(pattern='ping'))
async def handler_ping(event):
    answer = await event.respond('pong')
    await asyncio.sleep(5)
    await bot.delete_messages(event.chat_id, [event.id, answer.id])


bot.run_until_disconnected()
