import asyncio
from telethon import TelegramClient, events

api_id = 10953300
api_hash = "9c24426e5d6fa1d441913e3906627f87"
bot_token = 'bot tokeni'

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

async def text_animation(event, emoji, text):
    original_text = list(text)
    message = await event.respond("Animatsiya boshlanyapti...")

    for i in range(len(original_text)):
        animated_text = original_text.copy()
        animated_text[i] = emoji
        await message.edit(''.join(animated_text))
        await asyncio.sleep(0.3)

    final_text = emoji * len(text)
    await message.edit(final_text)

@client.on(events.NewMessage(pattern=r'/animation (.+?) (.+)'))
async def animation_handler(event):
    input_str = event.message.text.split(' ', 2)
    if len(input_str) < 3:
        await event.respond("To'g'ri format: /animation <emoji> <text>")
        return
    
    emoji = input_str[1]
    text = input_str[2]
    
    await text_animation(event, emoji, text)

client.run_until_disconnected()
