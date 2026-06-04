import os
from dotenv import load_dotenv
import asyncio
import telegram

load_dotenv()

async def main():
    bot_token = os.getenv("BOT_TOKEN")
    if (not bot_token):
        raise RuntimeError("Missing Bot Token.")
    bot = telegram.Bot(bot_token)
    async with bot:
        print(await bot.get_me())
    print("Hello from py-bot!")


if __name__ == "__main__":
    asyncio.run(main())
