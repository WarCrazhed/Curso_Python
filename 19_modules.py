import sys
print(sys.path)

import re
text = 'Mi número de telefono es 311 123 121, el codigo del país es 57, mi número de la suerte 3'

result = re.findall('[0-9]+', text)
print(result)

import time
timestamp = time.time()
print(timestamp)
local = time.localtime()
result = time.asctime(local)
print(local)
print(result)

import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter)