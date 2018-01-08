import grpc
import diamonds_pb2_grpc
import diamonds_pb2
from concurrent import futures
import time
import pymysql

import logging




_ONE_DAY_IN_SECONDS = 60 * 60 * 24



class Diamonds(diamonds_pb2_grpc.DiamondsServicer):

	def ConnectToDataBase(self):
		hostname = 'localhost'
		username = 'root'
		password = 'Password1'
		connection = pymysql.connect(host=hostname,user=username,password=password,db='gems')

		return connection

	def GetDiamondsByType(self,request,context):
		

		logging.info("SERVER:: GetDiamondsByType Requested")

		connection = self.ConnectToDataBase()
		cursor = connection.cursor()

		Query = "SELECT * from diamonds where cut='" + request.type + "'"
		print Query


		try:
			cursor.execute(Query)
			logging.info("Query %s executed" % Query)

			for item in cursor.fetchall():
				output = "{Carat: %f, Cut: %s, Color: %s, Clarity: %s,Depth: %f,Table: %d,Price: %d}" % (item[0],item[1],item[2],item[3],item[4],item[5],item[6])
		
				yield diamonds_pb2.TypeResponse(type=output)

		except Exception:
			logging.error("SERVER:: Error while Executing Query %s " % Query)
			

		


	def GetDiamondsByCarat(self,request,context):

		

		logging.info("SERVER:: GetDiamondsByCarat Requested")

		connection = self.ConnectToDataBase()
		cursor = connection.cursor()

		

		Query = "SELECT * from diamonds where carat=" + request.type
		print Query

		try:
			cursor.execute(Query)
			logging.info("Query %s executed" % Query)

			for item in cursor.fetchall():
				output = "{Carat: %f, Cut: %s, Color: %s, Clarity: %s,Depth: %f,Table: %d,Price: %d}" % (item[0],item[1],item[2],item[3],item[4],item[5],item[6])
		
				yield diamonds_pb2.TypeResponse(type=output)
		except Exception:
			logging.error("ServerError:: Unable to RUN query %s\nInvalid Parameters" % Query)

		



	def GetDiamondsByCaratRange(self,request,context):
		

		logging.info("SERVER:: GetDiamondsByCaratRange Requested")


		connection = self.ConnectToDataBase()
		cursor = connection.cursor()

		

		Query = "SELECT * from diamonds where carat between " + request.fromRange + " and " + request.toRange
		print Query

		try:
			cursor.execute(Query)
			logging.info("Query %s executed" % Query)

			for item in cursor.fetchall():
				output = "{Carat: %f, Cut: %s, Color: %s, Clarity: %s,Depth: %f,Table: %d,Price: %d}" % (item[0],item[1],item[2],item[3],item[4],item[5],item[6])
		
				yield diamonds_pb2.TypeResponse(type=output)
		except Exception:
			logging.error("ServerError:: Unable to RUN query %s\nInvalid Parameters" % Query)

		


	def GetDiamondsByPriceRange(self,request,context):
		

		logging.info("SERVER:: GetDiamondsByPriceRange Requested")

		connection = self.ConnectToDataBase()
		cursor = connection.cursor()

		

		Query = "SELECT * from diamonds where price between " + request.fromRange + " and " + request.toRange
		print Query

		try:
			cursor.execute(Query)
			logging.info("Query %s executed" % Query)
			for item in cursor.fetchall():
				output = "{Carat: %f, Cut: %s, Color: %s, Clarity: %s,Depth: %f,Table: %d,Price: %d}" % (item[0],item[1],item[2],item[3],item[4],item[5],item[6])
		
				yield diamonds_pb2.TypeResponse(type=output)
		except Exception:
			logging.error("ServerError:: Unable to RUN query %s\nInvalid Parameters" % Query)

		


	def GetDiamondsByColor(self,request,context):
		

		logging.info("SERVER:: GetDiamondsByColor Requested")

		connection = self.ConnectToDataBase()
		cursor = connection.cursor()

		

		Query = "SELECT * from diamonds where color='" + request.type + "'"
		print Query


		cursor.execute(Query)
		logging.info("Query %s executed" % Query)

		for item in cursor.fetchall():
			output = "{Carat: %f, Cut: %s, Color: %s, Clarity: %s,Depth: %f,Table: %d,Price: %d}" % (item[0],item[1],item[2],item[3],item[4],item[5],item[6])
		
			yield diamonds_pb2.TypeResponse(type=output)





def serve():
	logging.basicConfig(filename='diamonds.log',filemode='a',level=logging.DEBUG)
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	diamonds_pb2_grpc.add_DiamondsServicer_to_server(Diamonds(), server)
	server.add_insecure_port('[::]:50051')
	server.start()
	print "SERVER STARTED ! Listening for Incomming Requests"
	logging.info("SERVER:: Server Started")
	try:
	  while True:
	    time.sleep(_ONE_DAY_IN_SECONDS)
	except KeyboardInterrupt:
	  server.stop(0)	
	  logging.error("SERVER:: Server Closed")
	



if __name__ == '__main__':
  serve()


