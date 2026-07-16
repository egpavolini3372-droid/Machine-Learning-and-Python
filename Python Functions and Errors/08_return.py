
def summation(a,b):
    sum = 0
    for i in range(a, b+1):
        sum = sum + i
    print(sum)

summation(1, 2)
summation(1, 100)

sum2 = 0
for x in range(1, 101):
    sum2 += x
print(sum2)
