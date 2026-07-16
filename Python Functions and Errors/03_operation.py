
setA = {'Colombia', 'Mexico', 'Bolivia'}
setB = {'Bolivia', 'Peru'}

# Union and Intersection
setC= setA.union(setB)
print(setC)

print(setA | setB) # Union operator |

setD= setA.intersection(setB) 
print(setD)

print(setA & setB) # Intersection operator &

# Difference
setE= setA.difference(setB)
print(setE)
print(setA - setB) # Difference operator 

# Symmetric Difference
setF= setA.symmetric_difference(setB)
print(setF)
print(setA ^ setB) # Symmetric Difference operator ^