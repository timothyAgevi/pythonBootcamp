from flask import Flask,redirect,url_for,request,render_template,session

app = Flask(__name__)
app.secret_key = "agevi"

users = {"agevi": ("agevi", "1234")}

@app.route("/index")
def index():
    return render_template("index.html", name=session.get("username", "Unknown"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username][1] == password:
            session["username"] = username
            return redirect(url_for("index"))
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username not in users:
            users[username] = (username, password)
            return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))    

if __name__=='__main__':
    app.run(debug = True)











if __name__ == "__app__":
    app.run(debug=True)