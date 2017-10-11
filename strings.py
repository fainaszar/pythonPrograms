from string import maketrans

string = "Welcome to the world of Python"
string2 = "This is a example string in Python"


print string[0]
print string2[8:len(string2)]
print string[8:]

print string[:len(string)-2] + " It is very powerful"
string = string + " ok done to work"
print string

print "a block of text \n in a text editor"
print r" a bock of text \n in a text editor"


print string.center(80,' ')
#Makes the string of the specified length.The orginal string is centered within the
#filler character supplied.

print string.count("box")

#print "Enter a string:"
#input = raw_input(">>")

#print "The encoded string is " + input.encode('base64','strict')
#input = input.encode('base64','strict')
#print "The decoded string is " + input.decode('base64','strict')


print string.isalnum()

string += " 23 People"
print string
print string.isalnum()

print string.isspace()



joiner =":"
timers = ("hh","mm","ss")

print joiner.join(timers)


print string.ljust(83,'x')


input = raw_input("-->")

output = maketrans("aeiou","uoiea")

print input.translate(output)

print input.title()

print input.startswith("This")


