from flask import Flask, request

echo_app = Flask(__name__)

@echo_app.route('/', methods=['GET', 'POST'])
def echo():
    if request.method == 'GET':
        return 'Hi there!'
    elif request.method == 'POST':
        data = request.get_json(force=True)
        
        chat_id = data['message']['from']['id']
        text = data['message']['text']

        print(chat_id, text)

        return 'Hello'

if __name__ == '__main__':
    echo_app.run()