import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
					format='(%(threadName)-10s) %(message)s'
					)


def WriteToFile(data,Lock):

	with Lock:


		logging.debug("Thread {} is Writing to the file".format(threading.currentThread().getName()))

		for i in range(1,5):
			logging.debug("Writing {}".format(data))

		logging.debug("{} : I am done writing to the file".format(threading.currentThread().getName()))


def ReadFromFile(data,Lock):

	with Lock:

		logging.debug("Thread {} is Reading from  the file".format(threading.currentThread().getName()))

		for i in range(1,5):
			logging.debug("Reading {}".format(data))

		logging.debug("{} : I am done reading to the file".format(threading.currentThread().getName()))


Lock = threading.Lock()
data = "Its good to read/write to the file"

for i in range(10):
	writeThread = threading.Thread(name="writeThread",target=WriteToFile,args=(data,Lock))
	readThread = threading.Thread(name="readThread",target=ReadFromFile,args=(data,Lock))

	writeThread.start()
	readThread.start()