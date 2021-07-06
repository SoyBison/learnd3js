from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)


@app.route("/testing_page")
def testing_page():
    return render_template('testing.html')


@app.route("/")
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run() 
