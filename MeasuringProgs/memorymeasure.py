from tracemalloc import *

start()

l = []

for i in range (0, 100000):

    l.append(i)

print(get_traced_memory())

stop()