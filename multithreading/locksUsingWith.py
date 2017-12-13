import logging
import threading

logging.basicConfig(level=logging.DEBUG,
					format='(%(threadName)-10s) %(message)s'
					)


def using_with(lock):
	with lock:
		logging.debug("Lock Acquired Using With")


def without_using_with(lock):
	lock.acquire()
	try:
		logging.debug('Lock acquired directly')
	finally:
		lock.release()


lock = threading.Lock()
w = threading.Thread(target=using_with,args=(lock,))
nw = threading.Thread(target=without_using_with,args=(lock,))

w.start()
nw.start()