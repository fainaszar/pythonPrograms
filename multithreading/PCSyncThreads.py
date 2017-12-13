import logging
import threading
import time
import random
import Queue

logging.basicConfig(level=logging.DEBUG,
					format='(%(threadName)-10s) %(message)s'
					)

BUFFER_SIZE =10
q = Queue.Queue(BUFFER_SIZE)
lock = threading.Lock()

class Producer(threading.Thread):

	def __init__(self,group=None,target=None,name=None,args=(),kwargs=None,verbose=None):
		super(Producer,self).__init__()
		self.target = target
		self.name= name
		



	def run(self):

		while True:

			with lock:
				if not q.full():
					data = random.randint(1,50)
					q.put(data)
					logging.debug("Producer produced {} to the buffer".format(data))



class Consumer(threading.Thread):

	def __init__(self,group=None,target=None,name=None,args=(),kwargs=None,verbose=None):
		super(Consumer,self).__init__()
		self.target = target
		self.name= name
		


	def run(self):

		while True:
			with lock:
				if not q.empty():
					data = q.get()
					logging.debug("Consumer consumed {} from the buffer".format(data))






producer = Producer(name="ProducerThread")
consumer = Consumer(name="Consumer")




producer.start()
time.sleep(0.2)
consumer.start()


