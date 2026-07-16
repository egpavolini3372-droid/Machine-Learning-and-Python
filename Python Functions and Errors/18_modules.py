import sys
import re
import time
import collections

# Modulo sys

print(sys.path)

# Modulo re

text = "mi mumero es 3204298763, el codigo del pais es 51, mi numero de la suerte es 7"
result = re.findall("[0-9]+", text)
print(result)

# Modulo time

timestamp = time.time()
local = time.localtime()
what_time = time.asctime(local)
print(timestamp)
print(what_time)

# Modulo Collections

numbers = [1,2,4,5,1,8,5,3,9,1,1,1,4,5,6,7,7,7,7,7,7,7]
counter = collections.Counter(numbers)
print(counter)


