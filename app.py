from flask import Flask, request, render_template
from datetime import datetime
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('main.html')

@app.route("/Spring")
def spring():
    return render_template('Spring.html')

@app.route("/Summer")
def summer():
    return render_template('Summer.html')

@app.route("/Autumn")
def autumn():
    return render_template('Autumn.html')

@app.route("/Winter")
def winter():
    return render_template('Winter.html')

@app.route("/Picnic")
def picnic():
    return render_template('Picnic.html')

@app.route("/Spring/<booth>")
def SpringBooth(booth):
    return render_template(f'Spring{booth}.html')

@app.route("/Summer/<booth>")
def SummerBooth(booth):
    return render_template(f'Summer{booth}.html')

@app.route("/Autumn/<booth>")
def AutumnBooth(booth):
    return render_template(f'Autumn{booth}.html')

@app.route("/Winter/<booth>")
def WinterBooth(booth):
    return render_template(f'Winter{booth}.html')

@app.route("/Picnic/<booth>")
def PicnicBooth(booth):
    return render_template(f'Picnic{booth}.html')

if __name__ == '__main__':
    app.run()