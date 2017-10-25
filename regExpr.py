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
#'^[+-]?[0-9]*\.[0-9]+$' Matches floating point positve and negative numbers
#Print vowels of lenght 2 or more that lie between any 2 consonants
#v = "aeiou"
#c = "qwrtypsdfghjklzxcvbnm"
#m = re.findall(r'(?<=[%s])([%s]{2,})[%s]' % (c, v, c), raw_input(), flags = re.I)
#print('\n'.join(m or ['-1']))

#Find whether a given input is a valid roman number in range 1-3999
# = 'M{0,3}'
#hundred = '(C[MD]|D?C{0,3})'
#ten = '(X[CL]|L?X{0,3})'
#digit = '(I[VX]|V?I{0,3})'
#print (bool(re.match(thousand + hundred+ten+digit +'$', raw_input())))