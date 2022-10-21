from flask import Flask, request, render_template
from datetime import datetime
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('main.html')

@app.route("/<BoothName>")
def booth():
    return render_template(f'{booth}.html')


if __name__ == '__main__':
    app.run()