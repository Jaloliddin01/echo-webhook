import requests
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    keyboard = [
        [
            KeyboardButton('cat'),
            KeyboardButton('dog'),
        ],
    ]
    update.message.reply_text("Press one of the buttons", reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, one_time_keyboard=True))

def send_dog(update: Update, context: CallbackContext):
    
    # pic = requests.get('https://random.dog/woof.json')
    # print(pic)

    update.message.reply_text("mamam")