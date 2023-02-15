from telegram import Bot
import os

TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)

print(bot.get_webhook_info())
