import logging
import threading
import time
import random

logging.basicConfig(level=logging.DEBUG,
					format='(%(threadName)-10s) %(message)s'
					)


class ActivePool(object):
	def __init__(self):
		super(ActivePool,self).__init__()
		self.active=[]
		self.lock = threading.Lock()

	def makeActive(self,name):
		with self.lock:
			self.active.append(name)
			logging.debug('Running %s' , self.active)

	def makeInactive(self,name):
		with self.lock:
			self.active.remove(name)
			logging.debug('Running %s', self.active)



def worker(s,pool):
	logging.debug('Waiting to join pool')
	with s:
		name= threading.currentThread().getName()
		pool.makeActive(name)
		time.sleep(0.1)
		pool.makeInactive(name)
	


pool = ActivePool()
s = threading.Semaphore(2)
for i in range(4):
	t = threading.Thread(target=worker,name=str(i),args=(s,pool))
	t.start()