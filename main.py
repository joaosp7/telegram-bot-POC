import os
from dotenv import load_dotenv
import asyncio
import telegram

load_dotenv()

async def main():
    chat_id = 1033053823
    bot_token = os.getenv("BOT_TOKEN")
    if (not bot_token):
        raise RuntimeError("Missing Bot Token.")
    bot = telegram.Bot(bot_token)
    async with bot:
        print(await bot.get_me())
        updates = (await bot.get_updates())[1]
        print(updates)
        await bot.send_message(chat_id, text='VAI CURINTIA')
        
    print("Hello from py-bot!")


if __name__ == "__main__":
    asyncio.run(main())
