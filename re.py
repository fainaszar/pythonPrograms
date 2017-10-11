import re

paragraph = """This is a sample paragraph used to search through for using
regular expresseions in when python with all the related functions. Height and Width of 
an element is set. Lets us see if and only if it can do it
it matches numbers such as 123456 and 989332 . Also lets see what what whole 
bunch of where stuff it can do."""

print paragraph + "\n"


match_result = re.findall(r'\d+',paragraph,re.M | re.I) #search all numbers in the paragraph

if match_result:
	print match_result
else:
	print "No Matches found"


match_result = re.findall(r'[a-z,0-9]+ and [a-z,0-9]+',paragraph,re.M | re.I) #search all words grouped with and

if match_result:
	print match_result
else:
	print "No Matches found"


match_result = re.findall(r'wh.{1,3}',paragraph,re.M | re.I) #search all words grouped with and

if match_result:
	print match_result
else:
	print "No Matches found"