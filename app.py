# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/events/new', methods = ['GET', 'POST'])
def zip10456():
    if request.method =='GET':
        return render_template("mapsTest.html")
    else:
        print ("else statement")
print ("Hello")

