from data.recipe_data import getGroupInfo

getGroupInfo("Blackpink")
print(getGroupInfo(
    "Blackpink' UNION SELECT description FROM kpop WHERE band = 'Twice' ;--"))
