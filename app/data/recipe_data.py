from sqlite3 import connect

data = connect("data.db", isolation_level=None, check_same_thread=False)

def getGroupInfo(group):
    c = data.cursor()
    c.execute(f"SELECT description FROM kpop WHERE band = '{group}'")
    string = c.fetchmany()[0]
    return string
