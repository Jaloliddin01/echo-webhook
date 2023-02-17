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
    update.message.reply_text("Press one of the buttons", reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True))

def send_dog(update: Update, context: CallbackContext):
    
    pic = requests.get('https://random.dog/woof.json').json()

    update.message.reply_photo(pic['url'])

def send_cat(update: Update, context: CallbackContext):
    
    pic = requests.get('https://aws.random.cat/meow').json()

    update.message.reply_photo(pic['file'])