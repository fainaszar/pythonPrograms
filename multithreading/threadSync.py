import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
					format='(%(threadName)-10s) %(message)s'
					)

def consumer(condition):

	logging.debug('Consumer Thread Started')
	t = threading.currentThread()
	with condition:
		condition.wait()
		logging.debug("Resourse is available to consumer")


def producer(condition):

	logging.debug('Producer Thread Started')
	with condition:
		logging.debug('Making Resources Avalialble')
		condition.notifyAll()


condition = threading.Condition()

c1 = threading.Thread(name='c1',target=consumer,args=(condition,))
c2 = threading.Thread(name='c2',target=consumer,args=(condition,))
p = threading.Thread(name='p1', target=producer,args=(condition,))



c2.start()

c1.start()

p.start()