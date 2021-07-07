from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)

import os
from flask import send_from_directory

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.root_path,
                               'favicon.ico', mimetype='favicon.ico')

@app.route("/testing_page")
def testing_page():
    return render_template('testing.html')


@app.route("/")
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run() 
