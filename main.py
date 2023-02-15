from flask import Flask, request
from telegram import Bot
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
        
        chat_id = data['message']['from']['id']
        text = data['message']['text']

        print(f"ID`si {chat_id} bo`lgan foydalanuvchi ``{text}`` xabarini yubordi")

        bot.send_message(chat_id, text)

        return 'Hello'

if __name__ == '__main__':
    echo_app.run()