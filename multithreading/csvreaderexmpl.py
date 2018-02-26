from Queue import Empty
from ctypes import c_bool
from errno import EPIPE
from multiprocessing import (Process,Queue,Value)
from os import strerror
from random import randint
from time import sleep , time



def lagify():

	if randint(0,1):
		sleep(1)


class Pipe(object):

	def __init__(self):
		self.pipe =Queue()
		self._closed = Value(c_bool,False,lock=True)

	def write(self,data):

		if not self.closed:
			self.pipe.put(data)
		else:
			raise IOError("[Error No. {}] {}".format(EPIPE,strerror(EPIPE)))


	def read(self):

		return self.pipe.get(False)

	@property
	def closed(self):
		return self._closed.value 


	def close(self):
		self._closed.value = True


class Filter(object):

	def __init__(self,send=None,recv=None):
		self.send_pipe = send
		self.recv_pipe = recv


class WriteFilter(Filter):

	def send(self,fh):

		for line in fh:
			self.send_pipe.write(line)
			lagify()


	def __del__(self):
		self.send_pipe.close()


class CapsFilter(Filter):

	def listen(self):

		while True:
			try:
				print self.captalize(self.recv_pipe.read())
			except Empty:
				if self.recv_pipe.closed:
					print "Pipe is empty and closed "
					break

		lagify()


	def captalize(self,line):
		return str(line).upper()


	def send(self,line):

		if self.send_pipe:
			self.send_pipe.write(line)
		else:
			print line



if __name__ == '__main__':
	
	start = time()
	writer = WriteFilter(send=Pipe())
	capper  = CapsFilter(recv = writer.send_pipe)

	print "Sarting a CapsFilter listening to the WriteFilters Pipe"

	pc = Process(target=capper.listen)
	pc.start()

	print "Opening a filehande to test names.csv and passing it to Write Filter"

	test_data = open("names.csv")
	writer.send(test_data)
	print "FileWriter is done sending, closing pipe"
	writer  = None

	test_data.close()

	pc.join()
	print "Total Time Taken = {} seconds".format(start - time())