import thread

def doSomething(threadName,delay):
	count = 0
	while(count < 100):
		print "%s : I am doing some wor %d pc" % (threadName,count)
		count+=1


try:
	thread.start_new_thread(doSomething ,("Thread 1", 2))
	thread.start_new_thread(doSomething ,("Thread 2", 3))

except:
	print "Error: Unable to start Thread"


finally:
	print "Threads Executed"

while 1:
	pass



