from multiprocessing import Process,Queue,current_process

sentinel = -1


def producer(data,q):

	print('Creating data and putting it on the que')
	for item in data:
		q.put(item)
		print("Producer {} produced {}".format(current_process().name,item))


def consumer(q):
	while True:
		data = q.get()
		print("Data found to be processed: {} by {}".format(data,current_process().name))
		processed = data*2
		print(processed)


		if data is sentinel:
			break



if __name__ == '__main__':
	q = Queue()
	data = [i for i in range(10) if i % 3 != 0]
	p1 = Process(target=producer,args=(data,q))
	p2 = Process(target=consumer,args=(q,))
	p1.start()
	p2.start()



	q.close()
	q.join_thread()


	p1.join()
	p2.join()