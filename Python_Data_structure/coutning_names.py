
counts = {"erwin":1, "Natalia":2, "carlo":10}
for key in counts:
    print(key, counts[key])

print(list(counts.keys()))
print(list(counts.values()))
print(list(counts.items()))

for aaa, bbb in counts.items():
    print(aaa,bbb)

bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount is None or count >bigcount:
         bigword = word
         bigcount = count

print(bigword, bigcount)

stuff = dict()
print(stuff.get('candy',-1))