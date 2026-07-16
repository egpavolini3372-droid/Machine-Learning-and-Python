
total = 0
count = 0

while True:
    num = input("Enter a number ")
    if num == "done" : break
    value = int(num)
    total = total + value
    count = count + 1

average = total/count
print("Average is ", average) 


numList =[]

while True:
    num = input("Enter a number ")
    if num == "done" : break
    value = int(num)
    numList.append(value)

average2 = sum(numList)/len(numList)
print("Average 2 is ", average2) 


