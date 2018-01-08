import grpc
import message_pb2_grpc 
import message_pb2
import time


def sendMessages():
	while 1:
		msg = raw_input("Send Message: ")

		if msg=='q':
			break;


		yield message_pb2.InMessage(message=msg)
		time.sleep(0.2)
		

def getNum():
	while 1:
		print("entering function")
		i = raw_input("Enter a number or q to quit: ")

		if i=='q':
			print("Leaving Function")
			break;

		try:
			num = int(i)
		except ValueError:
			print("error")
			continue

		yield message_pb2.DataRequest(data = num)
		time.sleep(0.1)

def run():
	channel = grpc.insecure_channel('localhost:50051')
	stub = message_pb2_grpc.MessengerStub(channel)

	#Simple Request
	response = stub.Welcome(message_pb2.WelcomeRequest(user=raw_input("Enter your name: ")))
	print("Message Recieved From Server:\n " + response.message )

	

	#Streaming Request
	response = stub.AddNumbers(getNum())

	print(response)

	#Streaming Response
	response = stub.GetPrimes(message_pb2.DataRequest(data=(int(raw_input("Enter a number: ")))))
	print("The List of Prime nos Are:")
	for item in response:
		#print(type(item))
		#result = message_pb2.DataResponse(result=item.result)
		print(item.result)
	


	#Streaming Requests and Responses

	response = stub.Chat(sendMessages())

	for msg in response:
		print("Incomming Message: %s" % msg.message)


	





if __name__ == '__main__':
  run()