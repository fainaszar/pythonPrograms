# Program not working! ... cannot import Barrier
import threading
from random import randrange
from threading import  Thread 
from time import ctime , sleep
"""
	A barrier is a simple synchronization  primitive which can be used by different threads
	to wait for each other.
"""
num = 4

b = threading.Barrier(num)

names = ["Faizan","Faisal","Muneer","Burhan"]


def player():
	name = names.pop()
	sleep(randrange(2,5))
	print("{} reachd the barrier at: {}".format(name,ctime()))
	b.wait()


threads = []
print("Race Starts now...")


for i in range(num):
	threads.append(Thread(target=player))
	threads[-1].start()


for thread in threads:
	thread.join()

print()
print("Race over!")