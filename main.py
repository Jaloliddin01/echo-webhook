from flask import Flask

echo_app = Flask(__name__)

@echo_app.route('/')
def echo():
    return 'OK'

if __name__ == '__main__':
    echo_app.run()