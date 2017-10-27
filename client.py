import socket

s = socket.socket()
host = socket.gethostname()
port = 1234

s.connect((host,port))
print s.recv(1024)
s.send(str([2,3,4,5]))
print "List sent to server for processing"
print s.recv(1024)
s.close()