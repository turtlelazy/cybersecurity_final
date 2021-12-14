from sqlite3 import connect
from data.table import Table

data = connect("data.db", isolation_level=None, check_same_thread=False)
users = Table(data, "users", "username")


def get_usernames():
    "retuns a list of usernames"
    return users.get_main_values()


def user_exists(username):
    "returns true if user exists"
    return users.value_exists(username)


def correct_password(username, password):
    "returns true if username matches password"
    real_password = users.get_value(username, "password")
    return password == real_password


def add_user(username, password):
    "adds a user with username and passsowrd"
    users.add_values([username, password])
    edited_stories = Table(data, username, "title")
    edited_stories.create(["title"])

def reset_data():
    "resets the database to empty user and story tables"
    open("data.db", "w").close()
    users.create(["username", "password"])