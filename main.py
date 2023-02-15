from flask import Flask, request
from telegram import Bot, Update
import os

echo_app = Flask(__name__)

TOKEN = os.environ['TOKEN']
bot = Bot(TOKEN)

@echo_app.route('/', methods=['GET', 'POST'])
def echo():
    if request.method == 'GET':
        return 'Hi there!'
    elif request.method == 'POST':
        data = request.get_json(force=True)

        update = Update.de_json(data, bot)
        
        chat_id = update.message.chat.id
        text = update.message.text

        if text != None:
            bot.send_message(chat_id, text)

        print(f"ID`si {chat_id} bo`lgan foydalanuvchi ``{text}`` xabarini yubordi")

        bot.send_message(chat_id, text)

        return 'Hello'

if __name__ == '__main__':
    echo_app.run()