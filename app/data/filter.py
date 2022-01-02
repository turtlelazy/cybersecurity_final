import re

f = open("storedsaltedpw.txt",'r').read()
output = open("salts.txt",'w')

y = re.sub("(.*) ", "", f)

output.write(y)
