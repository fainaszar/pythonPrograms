import logging
import threading
import time
import random

logging.basicConfig(level=logging.DEBUG,
					format='(%(threadName)-10s) %(message)s'
					)


def lock_holder(lock):
	logging.debug('Starting')
	while True:
		lock.acquire()
		try:
			logging.debug("Holding Lock")
			time.sleep(0.5)
		finally:
			logging.debug("Releasing Lock")
			lock.release()
		time.sleep(0.5)
	return


def worker(lock):
	logging.debug("Starting Worker")
	num_tries = 0
	num_acquires = 0

	while num_acquires < 3:
		time.sleep(0.5)
		logging.debug("Tring to acquire lock")
		have_it = lock.acquire(0)
		try:
			num_tries +=1
			if have_it:
				logging.debug('Iteration %d: Acquired', num_tries)
				num_acquires += 1
			else:
				logging.debug('Iteration %d: Not Acquired', num_tries)

		finally:
			if have_it:
				lock.release()
	logging.debug('Done after %d iterations' , num_tries)


lock = threading.Lock()


holder = threading.Thread(target=lock_holder,args=(lock,),name="LockHolder")
holder.setDaemon(True)
holder.start()


worker = threading.Thread(target=worker,args=(lock,),name='Worker')
worker.start()