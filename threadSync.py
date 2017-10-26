import threading

exitFlag = 0

class myThread(threading.Thread):
	def __init__(self,threadID,threadName,counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.threadName = threadName
		self.counter = counter

	def run(self):
		print "Starting " + self.threadName
		threadLock.acquire()
		doSomething(self.threadName,self.counter,5)
		#print "Exiting " + self.threadName
		threadLock.release()

def doSomething(threadName,counter,delay):
	while counter:
		if exitFlag:
			threadName.exit()
		for i in range(100):
			print "%s printing %d" % (threadName,i)
		counter-=1


threadLock = threading.Lock()
threads=[]
try:
	thread1 = myThread (1,"Thread 1",1)
	thread2 = myThread (2 ,"Thread 2" , 2)

	thread1.start()
	thread2.start()

	threads.append(thread1)
	threads.append(thread2)
except:
	print "Error: Somthing bad happened"

finally:
	for t in threads:
		t.join()
	print "Exiting Main Thread"
