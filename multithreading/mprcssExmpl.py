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