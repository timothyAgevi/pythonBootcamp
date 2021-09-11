from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'


if __name__=='__main__':
    app.run(debug = True)











if __name__ == "__app__":
    app.run(debug=True)