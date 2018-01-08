import grpc
import diamonds_pb2_grpc
import diamonds_pb2
import time
import os

import logging




def DiamondsByCutType(stub):

	#Function to get Diamonds Based on thier Cut Type

	CutTypes = ["Premium","Very Good","Good","Fair","Ideal"]
	selectedType = raw_input("Please Enter Cut Type from following: %r \n>>>" % CutTypes)

	if selectedType not in CutTypes:
		print "Invalid Choice"
	else:
		return

	response = stub.GetDiamondsByType(diamonds_pb2.TypeRequest(type=selectedType))
	logging.info("DiamondsByCutType:: Method Called")


	count = 0
	for data in response:
		print data.type
		count+=1


	
	logging.info("DiamondsByCutValue:: %d records retreived" % (count))



	


def DiamondsByCaratValue(stub):

	Input = raw_input("Please Enter a value from 0.0 to 5.0 >> ")

	if Input.isalpha():
		print "Invalid Value"
		logging.error("DiamondsByCaratValue:: Invalid Data Entered")
		return
	
	response = stub.GetDiamondsByCarat(diamonds_pb2.TypeRequest(type=Input))
		
		
	
	logging.info("DiamondsByCaratValue:: Method Called")
	count=0
	for data in response:
		print data.type
		count+=1

	print "Total no of Diamonds Found: " , count
	logging.info("DiamondsByCaratValue:: %d records retreived" % (count))
	



def DiamondsByCaratRange(stub):

	logging.info("DiamondsByCaratRange:: Method Called")
	print "[Note]: Carat Range can be 0.0 to 5.0"
	From = raw_input("From Range: ")
	To = raw_input("To Range: ")

	if From.isalpha() or To.isalpha():
		logging.error("DiamondsByCaratRange:: Invalid Data Entered")
		print "Invalid Parameters"
		return

	response = stub.GetDiamondsByCaratRange(diamonds_pb2.RangeRequest(fromRange=From,toRange=To))
	count=0

	

	for data in response:
		print data.type
		count+=1


	print "Total No. of Diamonds Found: " , count
	logging.info("DiamondsByCaratRange:: %d records retreived" % (count))
	



def DiamondsByColor(stub):

	DiamondColors = ["D","E","F","G","H","I","J"]
	color = raw_input("Diamond colors start form D upto J , Enter a color >> ") 

	if color not in DiamondColors:
		logging.error("DiamondsByColor:: Invalid Data Entered")
		print "Invalid Parameters"
		return 

	response=stub.GetDiamondsByColor(diamonds_pb2.TypeRequest(type=color))
	count=0

	logging.info("DiamondsByColor:: Method Called")

	print "The Following Diamonds were Found"

	for data in response:
		print data.type
		count+=1


	print "Total No. of Diamonds Found: " , count
	logging.info("DiamondsByColor:: %d records retreived" % (count))


def DiamondsByPriceRange(stub):
	print "[Note] : Price Starts From 320"

	From=raw_input("From Range: >>")
	To =raw_input("To Range: >>")

	if From.isalpha() or To.isalpha():
		logging.error("DiamondsByCaratRange:: Error Retreiving Data")
		print "Invalid Paremeters"
		return

	response = stub.GetDiamondsByPriceRange(diamonds_pb2.RangeRequest(fromRange=From,toRange=To))
	count=0

	logging.info("DiamondsByPriceRange:: Method Called")

	

	for data in response:
		print data.type
		count+=1


	print "Total No. of Diamonds Found: " , count
	logging.info("DiamondsByPriceRange:: %d records retreived" % (count))

	
		
		




def run():
	channel = grpc.insecure_channel('localhost:50051')
	stub = diamonds_pb2_grpc.DiamondsStub(channel)

	logging.basicConfig(filename='diamonds.log',filemode='a',level=logging.DEBUG)



	print "*"*100

	print "Welcome to Diamonds gRPC Service"
	logging.info("MainProgram:: Client Service Started")

	while 1:
		os.system('clear')
		print "Enter your Choice of RPC to Call:\n"
		print '''
				 Press 1  to Get Diamonds By Cut type
				 Press 2  to Get Diamonds By Carat Value
				 Press 3  to Get Diamonds By Carat Range
				 Press 4  to Get Diamonds By Color
				 Press 5  to Get Diamonds By Price Range
				 Press q  to Quit'''

		choice = raw_input("Enter your choice:>> ")


		if choice == 'q':
			print "Thank you for using Diamonds gRPC"
			logging.info("MainProgram:: Client Disconnected")
			break


		if choice == '1':
			DiamondsByCutType(stub)
		elif choice == '2':
			DiamondsByCaratValue(stub)

		elif choice == '3':
			DiamondsByCaratRange(stub)

		elif choice == '4':
			DiamondsByColor(stub)

		elif choice == '5':
			DiamondsByPriceRange(stub)
		else:
			print "Invalid Request!"
			logging.error("MainProgram:: Invalid Choice")


		raw_input("<<Press a key to continue>>")





	



	



	



	




if __name__ == '__main__':
  run()