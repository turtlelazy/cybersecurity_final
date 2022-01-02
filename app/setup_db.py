from sqlite3 import connect
from data.random_contact import randomContact
import os
import random
if os.path.exists('data.db'):
    os.remove("data.db")
data = connect("data.db", isolation_level=None, check_same_thread=False)

c = data.cursor()

# #importing random contacts into the list
# c.execute("""CREATE TABLE contacts (
#     name TEXT KEY,
#     bd TEXT KEY,
#     number TEXT KEY
#     );
#     """)

# mass_query = """INSERT INTO contacts (name,bd,number)
#                 VALUES"""

# loop = 3
# for x in range(loop):
#     contact = randomContact()
#     contact_string = f'''("{contact[0]}",
#                             "{contact[1]}",
#                             "{contact[2]}")'''
#     if not x==loop-1:
#         contact_string += ","
#     else:
#         contact_string += ";"
#     mass_query+=contact_string
# print(mass_query)
# c.execute(mass_query)

# c.execute("""CREATE TABLE users (
#     user TEXT KEY,
#     hash TEXT KEY,
#     salt TEXT KEY
#     );
#     """)
# hashed_password = open("data/hashedpw.txt").read().split("\n")
# salts = open("data/salts.txt").read().split("\n")

# accounts = 3
# mass_query = """INSERT INTO users (user,hash,salt)
#                 VALUES"""

# for account in range(accounts):
#     randomNumber = random.randint(0, len(salts))
#     randomSalt = salts[randomNumber]
#     randomHash = hashed_password[randomNumber]

#     profile_string = f"""("bobby{account}","{randomHash}","{randomSalt}")"""

#     if not account==accounts-1:
#         profile_string += ","
#     else:
#         profile_string += ";"
#     mass_query += profile_string

# c.execute(mass_query)
