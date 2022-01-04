from sqlite3 import connect
from data.random_contact import randomContact
import os
import random
import hashlib
import string
if os.path.exists('data.db'):
    os.remove("data.db")
data = connect("data.db", isolation_level=None, check_same_thread=False)

c = data.cursor()

#importing random contacts into the list
c.execute("""CREATE TABLE contacts (
    name TEXT PRIMARY KEY,
    ducker_id TEXT,
    ducker_tag TEXT
    );
    """)

mass_query = """INSERT INTO contacts (name,ducker_id,ducker_tag)
                VALUES"""

loop = 25
for x in range(loop):
    contact = randomContact()
    ducker_age = contact[1]
    letters = string.ascii_letters
    
    ducker_tag = contact[2]
    contact_string = f'''("{contact[0]}",
                            "{ducker_age}",
                            "{ducker_tag}")'''
    if not x==loop-1:
        contact_string += ","
    else:
        contact_string += ";"
    mass_query+=contact_string
c.execute(mass_query)

c.execute("""CREATE TABLE users (
    user TEXT PRIMARY KEY,
    hash TEXT,
    salt TEXT
    );
    """)
hashed_password = open("data/hashedpw.txt").read().split("\n")
salts = open("data/salts.txt").read().split("\n")

accounts = 3
mass_query = """INSERT INTO users (user,hash,salt)
                VALUES"""

for account in range(accounts):
    randomNumber = random.randint(0, len(salts))
    randomSalt = salts[randomNumber]
    randomHash = hashed_password[randomNumber]

    profile_string = f"""("bobby{account}","{randomHash}","{randomSalt}")"""

    if not account==accounts-1:
        profile_string += ","
    else:
        profile_string += ";"
    mass_query += profile_string

c.execute(mass_query)

c.execute("""CREATE TABLE no_no(
    word TEXT PRIMARY KEY
)
""")

c.execute("""INSERT INTO no_no (word)
             VALUES
             ("swan"),
             ("goose"),
             ("geese"),
             ("alligators"),
             ("killer_whales"),
             ("snakes"),
             ("dolphines"),
             ("water_hose"),
             ("coyote"),
             ("garlic"),
             ("essential_oils"),
             ("cayenne pepper"),
             ("spikes"),
             ("nets"),
             ("hunting"),
             ("hunters")
""")

c.execute("""CREATE TABLE breadcrumbs(
             active_status INTEGER,
             super_secret_0 TEXT,
             super_secret_1 TEXT,
             super_secret_2 TEXT
)
""")

mass_query = """INSERT INTO breadcrumbs (
                                     active_status,
                                     super_secret_0,
                                     super_secret_1,
                                     super_secret_2)
"""
mass_query += """ VALUES
             (1,"ZbKHN1QezB8K7aqXK9Fg","UUsp3w5PknpRu6MK","5Mqikg9398SCzx1eEuzn"),"""
def rand_pass(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(20))

fake_leads = 25
for fake_lead in range(fake_leads):

    breadcrumb_string = f'(0,"{rand_pass(20)}","{rand_pass(20)}","{rand_pass(20)}")'
    if not fake_lead == fake_leads-1:
        breadcrumb_string += ","
    else:
        breadcrumb_string += ";"
    mass_query += breadcrumb_string

c.execute(mass_query)

c.execute("""CREATE TABLE operation_pigeon(
             organization_name TEXT PRIMARY KEY,
             mission_statement TEXT,
             objective TEXT,
             visit TEXT
)""")

organization_name = "Evil Duckies United Corp."
mission_statement = "Here at EDUC, we aim to make a better world. We aim to create a glorious future. For the betterment of duckies worldwide, we aim to make duckies great again."
objective = "We will not stop until all our enemies bow underneath our feet."
visit = "Login to 167.71.250.167 with your ducky credentials, and await further instructions"
c.execute(f"""INSERT INTO operation_pigeon(organization_name,mission_statement,objective,visit)
             VALUES
             ("{organization_name}","{mission_statement}","{objective}","{visit}");
""")
