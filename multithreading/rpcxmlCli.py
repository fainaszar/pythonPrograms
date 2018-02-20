import xmlrpclib


def discover_methods(proxy):
	method_names = proxy.listMethods()

	for method_name in method_names:
		sig = proxy.methodSignature(method_name)
		help = proxy.methodHelp(method_name)
		print help
		print "Method -- '{}'".format(method_name)
		print "  Signature: {} ".format(sig)
		print "   Help    : {} ".format(help)



def request(proxy,ival):
	ret_ival = str(proxy.is_even(ival))
	print " {} is even : {}".format(ival,ret_ival)


def main():
	node = 'localhost'
	port = 8000
	url = "http://{}:{}".format(node,port)
	proxy = xmlrpclib.ServerProxy(url)
	print "REQUEST sent to  {} at port {} ... ".format(node,port)
	discover_methods(proxy)

	for ival in range(10):
		request(proxy,ival)

	answer = proxy.multiply(5,3)
	print " multiply answer : {}".format(answer)



if __name__ == '__main__':
	main()