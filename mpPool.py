from multiprocessing import Process, Pool ,current_process
from threading import Thread
def doubler(number):
	name = current_process().name
	print ("Process {} is doubling the number {}".format(name,number))
	return number * 2



if __name__ == "__main__":
	numbers = [i for i in range(10) if i % 5 == 0]
	pool = Pool(processes=2)
	print (pool.map(doubler,numbers))



	
	# for i in numbers:
	# 	result = pool.apply_async(doubler,(i,))
	# 	print(result.get())