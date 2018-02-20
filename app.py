import threading
import Queue
import time
import sys
import os
import subprocess
import glob
import logging
from subprocess import PIPE

logging.basicConfig(level="DEBUG",format="[%(levelname)s] -- [%(asctime)s] -- %(message)s" )

class FileReaderThread(threading.Thread):

	_file_count =0
	def __init__(self,file_queue):
		super(FileReaderThread,self).__init__()
		self.file_queue = file_queue
		self.stoprequest = threading.Event()
		logging.info("FileReaderThread Initialized")


	def run(self):
		logging.info("Starting FileReaderThread")
		while not self.stoprequest.isSet():
			try:
				filename =self.file_queue.get()
				logging.info("Getting file from the Queue")
				print("Reading file: {}".format(filename))
				
				res = subprocess.Popen(["wc",os.path.realpath(filename)],stdout=PIPE)
				results = res.stdout.read().strip().split(" ")
				results = [value for value in results if value !='']
				lines,words,chars = int(results[0]),int(results[1]),int(results[2])
				print("File {} has {} lines , {} words and {} characters".format(filename,lines,words,chars))
				logging.info("1 file processed")

				if file_queue.empty():
					logging.info("Queue got empty")
					self.stoprequest.set()
			except Queue.Empty:
				logging.error("Queue got empty")
				continue

		self.file_queue.task_done()

	
		

class FileGrabberThread(threading.Thread):

	_file_count =0
	def __init__(self,file_queue,dirname):
		super(FileGrabberThread,self).__init__()
		self.file_queue = file_queue
		self.stoprequest = threading.Event()
		self.dirname = dirname
		logging.info("FileGrabberThread Initialized")

		


	def run(self):
		logging.info("FileGrabberThread started")
		while not self.stoprequest.isSet():
			try:
				
				filenames =list(self._files_in_dir(self.dirname))
				logging.info("Grabbed files from the directory")
				for filename in filenames:
					self.file_queue.put(filename)
					logging.info("File {} pushed to queue".format(filename))

				self.stoprequest.set()
			except Queue.Empty:
				logging.error("Queue got Empty")
				continue

		self.file_queue.task_done()
		logging.info("Processed {} files".format(self._file_count))



	


	def _files_in_dir(self,dirname):
		logging.info("Processing files in directory")
		for path,dirs,files in os.walk(dirname):
			for file in files:
				if file.endswith(".py"):
					self._file_count += 1
					#self.file_queue.put(os.path.join(path,file))

					logging.info("yielding file")
					yield os.path.join(path,file)






if __name__ == '__main__':
	file_queue = Queue.Queue()
	logging.info("File Queue Created")
	dirname = os.getcwd()
	file_thread = FileGrabberThread(file_queue=file_queue,dirname=dirname)
	other_thread = FileReaderThread(file_queue=file_queue)
	logging.info("Starting Threads")
	file_thread.start()
	other_thread.start()
	
	
	





