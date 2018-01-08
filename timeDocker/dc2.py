import time




months = {
	1 : ["JANUARY","January","january","jan","JAN","Jan"],
	2 : ["FEBRUARY","February","february","feb","FEB","Feb"],
	3 : ["MARCH","March","march","mar","MAR","Mar"],
	4 : ["APRIL","April","april","apr","APR","Apr"],
	5 : ["MAY","May","may"],
	6 : ["JUNE","June","june","jun","JUN","Jun"],
	7 : ["JULY","July","july","jul","JUL","Jul"],
	8 : ["AUGUST","August","august","aug","AUG","Aug"],
	9 : ["SEPTEMBER","September","september","sep","SEP","Sep"],
	10 : ["OCTOBER","October","october","oct","OCT","Oct"],
	11 : ["NOVEMBER","November","november","nov","NOV","Nov"],
	12 : ["DECEMBER","December","december","dec","DEC","Dec"]
}
def parseDate(date):

	if "/" in date:
		date = date.split("/")

	elif "-" in date:
		date = date.split("-")

	elif "," in date:
		date , year = date.split(",")
		date = date.split(" ") + [year]
	else:
		date = date.split()


	print("Parsed Date is  {} ".format(date))
	try:
		m,d,y=convertDate(date)

		printDate(m,d,y)
	except Exception:
		pass



def printDate(m,d,y):

	print("Press 1 to print the converted date in DD/MM/YYYY format else press any key for default format(YYYY/MM/DD")
	choice = input()

	if choice == '1':
		print("Converted Date: {} / {} / {}".format(d,m,y))
	else:
		print("Converted Date: {} / {} / {}".format(y,m,d))


def convertDate(date):

	month = 0
	day = 0
	year = 0		 
	
	for item in date:
		if item.isdigit():

			if int(item) in range(0,100):
				if len(date) < 3 :
					pass
				else:
					year =  "19" + item
					year = int(year)


			if int(item) in range(1000,4000):
				year = int(item)
		
			if int(item) in range(1,13):
				if month==0:
					month = int(item)
				if day == 0:
					day = int(item)

				month=int(item)
			

			if int(item) in range(13,32):
				day= int(item)

			 



		for key in months.keys():
			if item in months[key]:
				month = key
				

	if not year:
		year = 2017


	
	if not day or not month:
		print ("Invalid Date! Cannot Convert")
	else:
		
		return month,day,year
			









if __name__ == '__main__':
	
	date = input("Enter a date in any valid format (dd/mm/yy , mm/dd/yy, mm dd,yy) ")

	parseDate(date)