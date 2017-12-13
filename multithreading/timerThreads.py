import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
					format='(%(threadName)-10s) %(message)s'
					)


def delayed():
	logging.debug('Worker Running')
	return


t1 = threading.Timer(3,delayed)
t1.setName('t1')
t2= threading.Timer(3,delayed)
t2.setName('t2')

logging.debug('Starting Timers')
t1.start()
t2.start()


logging.debug('Waiting before cancelling %s',t2.getName())
time.sleep(2)
logging.debug('cancelling %s',t1.getName())
t1.cancel()
logging.debug('done')