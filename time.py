
import time


date = raw_input()

if "/" in date:
	date = date.split("/")

elif "-" in date:
	date = date.split("-")
else:
	date = date.split()


month=0
day=0
year=2017

for item in date:
	if item.isdigit():

		if int(item) in range(40,99):
			year =  "19" + item
			year = int(year) 


		if int(item) in range(1700,4000):
			year = int(item)
		
		if int(item) in range(1,13):
			month = int(item)
			if day == 0:
				day = int(item)
			

		if int(item) in range(13,32):
			day= int(item)





if "January" in date or "JANUARY" in date  or "january" in date or "JAN" in date or "jan" in date or "Jan" in date:
	month = 1



if "February" in date or "FEBRUARY" in date  or "february" in date or "FEB" in date or "feb" in date or "Feb" in date:
	month = 2


if "March" in date or "MARCH" in date  or "march" in date or "MAR" in date or "mar" in date or "Mar" in date:
	month = 3


if "April" in date or "APRIL" in date  or "april" in date or "APR" in date or "apr" in date or "Apr" in date:
	month = 4

if "May" in date or "MAY" in date  or "may" in date  or "May" in date:
	month = 5

if "June" in date or "JUNE" in date  or "june" in date or "JUN" in date or "jun" in date or "Jun" in date:
	month = 6

if "July" in date or "JULY" in date  or "july" in date or "JUL" in date or "jul" in date or "Jul" in date:
	month = 7


if "August" in date or "AUGUST" in date  or "august" in date or "AUG" in date or "aug" in date or "Aug" in date:
	month = 8

if "September" in date or "SEPTEMBER" in date  or "september" in date or "SEP" in date or "sep" in date or "Sep" in date:
	month = 9

if "October" in date or "OCTOBER" in date  or "october" in date or "OCT" in date or "oct" in date or "Oct" in date:
	month = 10

if "November" in date or "NOVEMBER" in date  or "november" in date or "NOV" in date or "nov" in date or "Nov" in date:
	month = 11

if "December" in date or "DECEMBER" in date  or "december" in date or "DEC" in date or "dec" in date or "Dec" in date:
	month = 12




if year == 0:
	year = 2017

if day==0:
	print "Invalid Date!"


print "{} / {} / {} ".format(year,month,day)

