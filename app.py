from flask import Flask, request, render_template
from datetime import datetime
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('main.html')

@app.route("/<season>")
def section(season):
    return render_template(f'{season}.html')

@app.route("/Spring/<booth>")
def Spring(booth):
    return render_template(f'Spring{booth}.html')

@app.route("/Summer/<booth>")
def Summer(booth):
    return render_template(f'Summer{booth}.html')

@app.route("/Autumn/<booth>")
def Autumn(booth):
    return render_template(f'Autumn{booth}.html')

@app.route("/Winter/<booth>")
def Winter(booth):
    return render_template(f'Winter{booth}.html')

@app.route("/Picnic/<booth>")
def booth(booth):
    return render_template(f'{booth}.html')

if __name__ == '__main__':
    app.run()