import threading
import Queue

exitFlag = 0

class myThread(threading.Thread):
	def __init__(self,threadID,threadName,q):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.threadName = threadName
		self.q = q

	def run(self):
		print "Starting " + self.threadName
		doSomething(self.threadName,self.q)
		print "Exiting " + self.threadName

def doSomething(threadName,q):
	while not exitFlag:
		queueLock.acquire()
		if not workQueue.empty():
			data=q.get()
			queueLock.release()
			print "%s processing %s" % (threadName,data)
		else:
			queueLock.release()


threadList = ["Thread-1", "Thread-2" ,"Thread-3"]
nameList = ["One","Two","Three","Four","Five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads=[]
threadID=1



try:
	for t in threadList:
		thread = myThread(threadID,t,workQueue)
		thread.start()
		threads.append(thread)
		threadID += 1
	queueLock.acquire()
	for word in nameList:
		workQueue.put(word)
	queueLock.release()


	while not workQueue.empty():
		pass

	exitFlag=1



except:
	print "Error: Somthing bad happened"

finally:
	 for thread in threads:
	 	thread.join()
	 print "Exiting Main Thread"
