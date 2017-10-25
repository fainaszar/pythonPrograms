import re
input = raw_input()
emails = re.findall(r'[a-zA-Z0-9-_\.]*@[a-zA-z]*\.[a-zA-z]{2,5}',input) #Match All emails
websites = re.findall(r'[^@A-Za-z]([a-zA-Z0-9-]+\.[a-zA-Z-.]+)',input) #match all websites
tags = re.findall(r'[^a-zA-Z]([@#][a-zA-Z0-9-_]*)',input) #matches all mentions startig like @uname and hashtags 

print "Extacted Emails:"
for email in emails:
	print email

print "Extracted Websites:"
for website in websites:
	print website


print "Extracted Tags:"
for tag in tags:
	print tag



# Other Regular Expressions:
'#\w*[^\n]*' - Matches all comments
#re.sub("(?<= )(&&)(?= )","and",string) Matches && and replaces it with and
#re.sub("(?<= )(\|\|)(?= )","or",string) Matches || and replaces it with or