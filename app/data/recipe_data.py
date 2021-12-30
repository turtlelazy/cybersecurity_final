from sqlite3 import connect

data = connect("data.db", isolation_level=None, check_same_thread=False)

def getGroupInfo(group):
    c = data.cursor()
    c.execute(f"SELECT description FROM kpop WHERE band = '{group}'")
    return c.fetchall()

def getInformation(attribute,table,search,condition):
    c = data.cursor()
    c.execute(f"SELECT {attribute} FROM {table} WHERE {search} = '{condition}'")
    return c.fetchall()

def getMatches(table,search,condition):
    c= data.cursor()
    c.execute(
        f"SELECT * FROM {table} WHERE {search} LIKE '%{condition}%'")
    return c.fetchall()
