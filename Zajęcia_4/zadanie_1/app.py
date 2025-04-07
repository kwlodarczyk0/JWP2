from flask import Flask, render_template

app = Flask(__name__)



users = {
    1: {"name": "Ala", "age": 22},
    2: {"name": "Bartek", "age": 25},
    3: {"name": "Celina", "age": 30}
}

@app.route("/")
def hello_world():
    return render_template("main.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/users")
def show_users():
    return render_template("users.html",users = users)


@app.route("/user/<id>")
def show_user(id):
    user = users.get(int(id))
    return render_template("user.html",user = user)


