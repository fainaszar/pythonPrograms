
def checkNumber(num):

	
	if (num % 2 == 0):
		return "Even"
	else:
		return "Odd"



def break_words(sentence):
	word = sentence.split(' ')
	print word
	word = sort_words(word)
	print word



def sort_words(words):
	return sorted(words)


number = raw_input("Enter a number: ")
result = checkNumber(int(number))
print "The number %r is %r" % (number,result)


break_words("This Is A Book Of Magic")

