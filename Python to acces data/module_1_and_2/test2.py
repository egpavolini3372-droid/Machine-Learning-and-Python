import re

hand = open("Python to acces data/text_test1.txt")
x = list()
for line in hand:
    y = re.findall("[0-9]+", line)
    x = x + y
    print(x)

sum = 0
for z in x:
    sum = sum + int(z)

print(sum)
