from flask import Flask, render_template, url_for, request,redirect;

app = Flask(__name__)

@app.route("/")
def home():
    
    return "hello world" 









if __name__ == "__app__":
    app.run(debug=True)