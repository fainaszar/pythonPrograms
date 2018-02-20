from SimpleXMLRPCServer import SimpleXMLRPCServer
import inspect



class Methods(object):

	def multiply(self,x,y):
		return x*y



def is_even(n):
	return n % 2  == 0

def is_odd(n):
	return n % 2 == 1


def listMethods():
	return Supported_methods.keys()


def methodSignature(method_name):

	if method_name in Supported_methods:
		func = Supported_methods[method_name]
		return inspect.getargspec(func).args

	else:
		return "Error. Function '{}' not supported".format(method_name)


def methodHelp(method_name):
	print method_name
	if method_name in Supported_methods:
		func = Supported_methods[method_name]

		return func.__doc__
	else:
		return "Error. Function '{}' not supported".format(method_name)


Supported_methods = {
	'is_even':is_even,
	'is_odd':is_odd,
	'listMethods':listMethods,
	'methodSignature':methodSignature,
	'methodHelp':methodHelp,
}


def start():
	node = 'localhost'
	port = 8000
	server = SimpleXMLRPCServer((node,port),allow_none=True)
	print "Listening on {} at port {} ....".format(node,port)

	for name,func in Supported_methods.items():
		server.register_function(func,name)

	methods = Methods()
	multiply = methods.multiply
	server.register_function(multiply,'multiply')
	server.register_function(listMethods,"listMethods")
	server.serve_forever()


def main():
	start()


if __name__ == '__main__':
	main()