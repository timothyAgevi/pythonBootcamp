from flask import Flask, render_template, url_for, request,redirect
from flaskext.mysql import MySQL
app = Flask(__name__)

@app.route("/")
def home():
    
    return render_template('index.html') 









if __name__ == "__app__":
    app.run(debug=True)