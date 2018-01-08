import grpc
import message_pb2_grpc 
import message_pb2
from concurrent import futures
import time


_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Messenger(message_pb2_grpc.MessengerServicer):

	def Welcome(self,request,context):
		print("%s requsted a reply" % request.user)
		return message_pb2.WelcomeReply(message="Welcome , %s" % request.user)

	def AddNumbers(self,request_iterator,context):
		previous = None

		sum=0

		for no in request_iterator:
			num = no.data
			
			if previous is None:
				
				sum = sum+num
				previous = sum
				print(sum)
			else:
				sum= previous + num
				previous=sum
				print(sum)



		return message_pb2.DataResponse(result=sum)

	def GetPrimes(self,request,context):

		num = request.data
		

		for i in range(num):
			flag=0
			for j in range(2,num):

				if i % j == 0 and i!=j:
					print(i)
					flag=1
					break
				

			if flag== 0:

				yield message_pb2.DataResponse(result = i)
				time.sleep(0.4)
		


	def Chat(self,request_iterator,context):


		for message in request_iterator:
			print("Incomming Message: %s" % message.message)

			outmsg = raw_input("Reply:>> ")

			yield message_pb2.OutMessage(message = outmsg)
			time.sleep(0.2)
			
		
		


def serve():
	  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	  message_pb2_grpc.add_MessengerServicer_to_server(Messenger(), server)
	  server.add_insecure_port('[::]:50051')
	  server.start()
	  try:
	    while True:
	      time.sleep(_ONE_DAY_IN_SECONDS)
	  except KeyboardInterrupt:
	    server.stop(0)	



if __name__ == '__main__':
  serve()