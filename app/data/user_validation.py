from sqlite3 import connect
import hashlib

data = connect("data.db", isolation_level=None, check_same_thread=False)
c = data.cursor()

def user_exists(username):
    "returns true if user exists"
    return bool(c.execute(f'SELECT user FROM users WHERE user="{username}"').fetchone())

def get_salt(username):
    return c.execute(f'SELECT salt FROM users WHERE user="{username}"').fetchone()[0]


def get_hash(username):
    return c.execute(f'SELECT hash FROM users WHERE user="{username}"').fetchone()[0]

def correct_password(username, password):
    "returns true if username matches password"
    if not user_exists(username):
        return False
    
    given_hash = hashlib.md5((password + get_salt(username)).encode()).hexdigest()
    return given_hash == get_hash(username)
