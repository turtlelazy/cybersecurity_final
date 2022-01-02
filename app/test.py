from data.recipe_data import *

# getGroupInfo("Blackpink")
# print(getGroupInfo(
#     "Blackpink' UNION SELECT description FROM kpop WHERE band = 'Twice' ;--"))

#print(execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"))
print(execute("SELECT * FROM operation_pigeon")[0][0])