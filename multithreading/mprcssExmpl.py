import os
import subprocess
import multiprocessing

def q_runner(nProcesses,list_item,function,*args):
	task_queue = multiprocessing.Queue()
	results_queue = multiprocessing.JoinableQueue()

	if args:
		arguments = (task_queue,results_queue,) + arg
	else:
		arguments = (task_queue,results_queue,)

	results = []

	if len(list_item) < nProcesses:
		nProcesses = len(list_item)


	for l in list_item:
		task_queue.put(l)

	for _ in range(nProcesses):
		p = multiprocessing.Process(target=function,args=arguments).start()

	for _ in range(len(list_item)):

		results.append(results_queue.get())
		results_queue.task_done()


	for _ in range(nProcesses):
		task_queue.put('STOP')

	results_queue.join()

	task_queue.close()
	results_queue.close()

	return results



def worker1(input,output):

	for c in iter(input.get,'STOP'):

		my_sub_call = subprocess.Popen('sleep 1',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate(None)
		output.put(str(c) + 'a')
		print output





nProcesses = 6
list_item = range(10)
r1 = q_runner(nProcesses,list_item,worker1)
print "First Process Completed"
r2 = q_runner(nProcesses,list_item,worker1)
print "Second Process Completed"