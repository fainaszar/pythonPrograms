import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host,port))

s.listen(5)

while True:
	c , addr = s.accept()
	print "Got connection from : " , addr
	c.send("Hello Guest! Welcome")
	inp = c.recv(1024).strip("[,]").split()
	print "List Receaved for processing"
	sum =0
	for i in inp:
		sum += int(i.strip(","))

	result = "The result of the list is is %d" % sum
	print "Processing Completed"
	c.send(result)
	c.close()