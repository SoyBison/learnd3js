from flask import Flask, current_app
from flask_restful import Resource, Api

app = Flask(__name__)


@app.route("/")
def hello_world():
    return current_app.send_static_file('home.html')


if __name__ == '__main__':
    app.run()
