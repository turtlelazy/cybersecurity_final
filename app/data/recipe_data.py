from sqlite3 import connect

data = connect("data.db", isolation_level=None, check_same_thread=False)
