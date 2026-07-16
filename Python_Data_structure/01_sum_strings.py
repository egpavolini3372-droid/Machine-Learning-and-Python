
a = "hello"
b = a + " world"
print(b)

t_or_f = "l" in a
print(t_or_f)

if "x" in a:
    print("x is in a")
else:
    print("x is not in a")
print("Fin del programa")

c = "I AM HAPPY TODAY"
d = c.lower()
print(d)

e = c.find("HAPPY")
print(e)

f = c.replace("HAPPY", "SAD")
print(f)

g ="   spacious   "
print(g)
h = g.strip() # removes leading and trailing spaces (first and last)
print(h)

i = g.lstrip() # removes leading spaces (only first)
print(i)
j = g.rstrip() # removes trailing spaces (only last)
print(j)

k = c.startswith("I AM")
print(k)

l ="eg.pavolini3382@gmail.com ErwinPavolini"
m = l.find("@")
print(m)
n = l.find(" ", m)
print(n)
email = l[m:n]
print(email)

str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)

x = 'From marquard@uct.ac.za'
atpos = x.find('q')
print(atpos)
sppos = x.find("@")
print(sppos)
print(x[14:17])

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])