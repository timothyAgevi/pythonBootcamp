from flask import Flask, render_template, url_for, request,redirect
from flaskext.mysql import MySQL
app = Flask(__name__)

@app.route("/")
def home():
    path = "homepage"
    return render_template('index.html', variable=path)