import os
from os import environ
from pyrogram import Client, filters

API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
CHANNEL_ID = int(environ.get("CHANNEL_ID"))
ADMIN = int(environ.get("ADMIN"))

Client = Client("Copy bot", api_id = API_ID, api_hash = API_HASH, bot_token = BOT_TOKEN)

@Client.on_message(filters.text | filters.document | filters.photo | filters.audio)
async def copy(client: Client, message):
     if int(message.from_user.id) not in ADMIN:
          await message.reply_sticker("CAACAgUAAxkBAAIBT2J5_syo2NP8OB5oDyvXpAABPPZlDwACfwIAAhwWkFT5wl_pR2WTciQE")
     else:
          dd=await client.copy_message(
               chat_id = CHANNEL_ID,
               from_chat_id = message.chat.id,
               message_id = message.id
               )
          await message.reply(f"Successfully Copied your message to {dd.link}")
               
Client.run()
