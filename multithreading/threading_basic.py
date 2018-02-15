import threading , multiprocessing

def worker(num):
	for i in range(100000):
		continue
	print "{}".format(num)
	return

threads=[]


for i in range(5):
	t = multiprocessing.Process(target=worker,args=(i,))
	#t =threading.Thread(target=worker,args=(i,))
	threads.append(t)
	t.start()

	