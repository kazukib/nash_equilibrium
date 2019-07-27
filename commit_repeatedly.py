import time
import random

time.sleep(random.randint(1,10))
f = open('proliferate.py', 'a')
f.write('print("under experiment")\n')
f.close()