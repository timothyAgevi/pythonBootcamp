from flask import Flask

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username][1] == password:
            session["username"] = username
            return redirect(url_for("home"))
    return render_template("login.jinja2")


@app.route('/')
def index():
    return 'Hello World'


if __name__=='__main__':
    app.run(debug = True)











if __name__ == "__app__":
    app.run(debug=True)