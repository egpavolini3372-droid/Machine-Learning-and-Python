import re

x = "From Using the : character"
y = re.findall("^F.+:", x)
print("^F.+: word with F until : sign", y)

v = "From eg.pavolini3372@gmail.com Sat 14/09/2021"
t = re.findall("\S+@\S+", v)
z = print("\S+@\S+ Letter between blank spaces", t)

words = v.split()
email = words[1]
pieces = email.split("@")
print(words)
print(pieces)
print(pieces[1])

x = "From: Using the : character"
y = re.findall("^F.+:", x)
print(y)
