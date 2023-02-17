from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, CommandHandler, Filters
import os

from main import ( 
    send_dog, 
    start
)

app = Flask(__name__)


TOKEN = os.environ['TOKEN']
bot = Bot(TOKEN)

@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return 'Hi, from Python-2022I'
    elif request.method == 'POST':
        data = request.get_json(force=True)
        update = Update.de_json(data, bot)
        print(update)

        dp = Dispatcher(bot, None, workers=0)

        dp.add_handler(CommandHandler('start', start))
        dp.add_handler(MessageHandler(Filters.text('dog'), send_dog))


        dp.process_update(update)
        return 'Ok'

if __name__ == "__main__":
    main()

 