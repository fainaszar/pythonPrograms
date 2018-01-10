from multiprocessing import Process,current_process

def func():
	for i in range(10):
		pname = current_process().name
		print("Process {} printed {}".format(pname,i))
	print "*"*30






for i in range(3):
	name = "Process " + str(i)
	p = Process(target=func)
	p.start()




