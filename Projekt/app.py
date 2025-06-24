import eventlet
eventlet.monkey_patch()
from config.init_data import init_data
from models.models import db, User
from flask_cors import CORS
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_socketio import SocketIO
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from game.game_manager import GameManager
from hub.game_hub import GameHub
from typing import Optional, Any


app = Flask(__name__, template_folder="templates", static_folder="static")
app.config.from_object("config.db.Config")
db.init_app(app)
init_data(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id: str) -> Optional[User]:
    """
    Load a user from the database by user ID.

    Args:
        user_id (str): The user's ID.

    Returns:
        Optional[User]: The user instance or None if not found.
    """
    return db.session.get(User, int(user_id))


@app.route("/register", methods=["GET", "POST"])
def register() -> Any:
    """
    Handle user registration.

    Returns:
        Any: Redirect or rendered template.
    """
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        retypePassword = request.form["retypePassword"]
        if retypePassword != password:
            flash("Passwords do not match")
            return redirect(url_for("register"))

        if User.query.filter_by(username=username).first():
            flash("User already exists")
            return redirect(url_for("register"))

        hashed_password = generate_password_hash(password)

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful")
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login() -> Any:
    """
    Handle user login.

    Returns:
        Any: Redirect or rendered template.
    """
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("index"))
        flash("Wrong username or password")
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout() -> Any:
    """
    Log out the current user.

    Returns:
        Any: Redirect to login page.
    """
    logout_user()
    return redirect(url_for("login"))


socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)

game_manager = GameManager()
game_hub = GameHub(config={}, manager=game_manager)


@socketio.on("connect")
def handle_connect() -> None:
    """
    Handle a new socket connection and send available ships.
    """
    game_hub.get_ships()


@socketio.on("AddPlayer")
def on_add_player(data: Any) -> None:
    """
    Handle adding a player to a game.

    Args:
        data (Any): Player and board data.
    """
    game_hub.add_player(data)


@socketio.on("Shot")
def on_shot(data: Any) -> None:
    """
    Handle a shot event from a player.

    Args:
        data (Any): Shot data.
    """
    game_hub.shot(data)


@socketio.on("GetShips")
def on_get_ships() -> None:
    """
    Send available ships to the client.
    """
    game_hub.get_ships()


@socketio.on("SendMessageToGroupChat")
def on_group_message(data: Any) -> None:
    """
    Handle sending a chat message to the group.

    Args:
        data (Any): Message data.
    """
    game_hub.send_message_to_group_chat(data)


@socketio.on("Disconnect")
def on_disconnect(data: Any) -> None:
    """
    Handle a player disconnecting from the game.

    Args:
        data (Any): Disconnect data.
    """
    game_hub.disconnect(data)


@app.route("/")
@login_required
def index() -> Any:
    """
    Render the main game page for the logged-in user.

    Returns:
        Any: Rendered main page template.
    """
    return render_template("main.html", user=current_user)


if __name__ == "__main__":
    """
    Run the Flask application with SocketIO.
    """
    socketio.run(app, host="0.0.0.0", port=5000)
