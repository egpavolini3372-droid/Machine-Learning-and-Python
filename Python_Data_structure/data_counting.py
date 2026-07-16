
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name, "r")

counts = dict()
for line in handle:
    if line.startswith('From: '):
        email = line[5:]
        counts[email] = counts.get(email, 0) + 1
bigcount = None
bigemail = None
for email,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigemail = email
print(bigemail,bigcount)