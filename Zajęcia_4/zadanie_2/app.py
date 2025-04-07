from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("main.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/tasks")
def tasks_page():
    return render_template("tasks.html")