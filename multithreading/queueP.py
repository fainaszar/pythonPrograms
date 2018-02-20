import logging
import threading
import time
import random
import Queue

logging.basicConfig(level=logging.DEBUG,
					format='(%(threadName)-10s) %(message)s'
					)

BUFFER_SIZE=10
q = Queue.Queue(BUFFER_SIZE)


class ProducerThread(threading.Thread):
	def __init__(self,group=None,target=None,name=None,args=(),kwargs=None,verbose=None):
		super(ProducerThread,self).__init__()
		self.target = target
		self.name= name


	def run(self):
		while True:
			if not q.full():
				item = random.randint(1,10)
				q.put(item)
				logging.debug('Putting %s to the Queue :: Queue Size: %s' , str(item),str(q.qsize()) )
				time.sleep(random.random())



class ConsumerThread(threading.Thread):

	def __init__(self,group=None,target=None,name=None,args=(),kwargs=None,verbose=None):
		super(ConsumerThread,self).__init__()
		self.target = target
		self.name = name
		return


	def run(self):

		while True:
			if not q.empty():
				item = q.get()
				logging.debug('Getting Item %s from Queue :: Queue has %s items left', str(item),str(q.qsize()))
				time.sleep(random.random())

		return




if __name__ == '__main__':
	p = ProducerThread(name='Producer')
	c = ConsumerThread(name='Consumer')


	p.start()
	time.sleep(2)
	c.start()
	time.sleep(2)


