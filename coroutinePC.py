

def producer(sentence,next_coroutine):

	tokens = sentence.split(" ")
	for token in tokens:
		next_coroutine.send(token)
	next_coroutine.close()


def pattern_filler(pattern="ing",next_coroutine=None):

	print("Searching for {}".format(pattern))
	try:
		while True:
			token = (yield)
			if pattern in token:
				next_coroutine.send(token)
	except GeneratorExit:
		print("Done with filtering")


def print_tokens():

	print("I am sink , I will print tokens")

	try:
		while True:
			token = (yield)
			print(token)
	except GeneratorExit:
		print ("Done with printing")



pt = print_tokens()
pt.__next__()
pf = pattern_filler(next_coroutine=pt)
pf.__next__()


# sentences = [,,]
#producer("Bob is running behind a fast moving car",pf)
#producer("The boy was playing football in the playground",pf)
producer("While sleeping he was wandering in the corridor",pf)