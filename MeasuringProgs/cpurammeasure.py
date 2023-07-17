from psutil import *
from os import *

l1, l5, l15 = getloadavg()

# CPU

cusage = cpu_percent()

print(f"CPU Usage (%): {cusage}")

# RAM

rusage = virtual_memory()[2] # 3rd field of virtual_memory tuple is used. This is percentage usage.

rusedvalue = virtual_memory()[3]/1000000000 # 4th field of virtual_memory tuple is used and converted to GB. This is GB usage.

print(f"Ram Usage (%): {rusage}")

print(f"Ram Usage (GB): {rusedvalue}")