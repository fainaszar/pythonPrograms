#Coroutines in Python


def print_name(prefix):
	print("Searching for prefix: {}".format(prefix))
	try:
		while True:
			name = (yield)
			if prefix in name:
				print(name)
	except GeneratorExit:
		print("Closing Coroutine")


cr = print_name("Dear")

cr.__next__()

cr.send("Faizan")
cr.send("Dear Faizan")
cr.send("Muneer")
cr.send("Muneer Dear")
cr.close()