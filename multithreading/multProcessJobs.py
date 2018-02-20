from multiprocessing import Lock, Process,Queue,current_process
import time
import queue


def do_job(task_to_accomplish,tasks_that_are_done):
	while True:
		try:
			task = task_to_accomplish.get_nowait()
		except queue.Empty:
			break
		else:

			print(task)
			tasks_that_are_done.put("Task {} done by {}".format(task,current_process().name))
			time.sleep(.5)

		return True



def main():

	no_of_tasks = 30
	no_of_processes = 4
	task_to_accomplish = Queue()
	tasks_that_are_done = Queue()
	processes = []

	for i in range(no_of_tasks):
		task_to_accomplish.put("Task no {}".format(i))

	for w in range(no_of_processes):

		p = Process(target=do_job,args=(task_to_accomplish,tasks_that_are_done))
		processes.append(p)
		p.start()


	for p in processes:
		p.join()


	while not tasks_that_are_done.empty():
		print(tasks_that_are_done.get())

	return True



if __name__ == "__main__":
	main()