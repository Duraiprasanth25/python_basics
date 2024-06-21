import threading
import time
def calc_square(numbers):
    print("calculate square of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("square:", n * n)
def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)#artificial daelay
        print("cube:", n * n * n)

arr = [2,5,7,9]

t = time.time()

t1 = threading.Thread(target = calc_square, args=(arr,))
t2 = threading.Thread(target = calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in :", time.time()-t)
print("Hah.. I am done with all my work now")

import time
import threading
from threading import Thread

def sleepMe(i):
    print("Thread %i will sleep." % i)
    time.sleep(5)
    print("Thread %i is awake." % i)

for i in range(10):
    th = threading.Thread(target=sleepMe, args=(i,))
    th.start()
    print('Current Threads: %i' % threading.activeCount())


