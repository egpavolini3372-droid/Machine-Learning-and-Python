fname = input("Enter file name: ")

fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    words =line.split()
    for l in words:
         if l in lst:
             continue
         else:
             lst.append(l)

lst.sort()
print(lst)      




