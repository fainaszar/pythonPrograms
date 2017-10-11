
filename = raw_input("Enter the name of the file to open: ")
try:
	file_content  = open(filename)
except IOError:
	print "File %r not found" % filename
	exit()


print "The file %r has following content :\n" % filename

print file_content.read()

print "Keep the file or overwrite it ? Press Ctrl+C to keep the file"
try:
	 raw_input("Ok ?")
except Exception:
	print "Error Occured"
	exit()

file_content.close()
print "Preparing to overwrite the file"

file_content = open (filename,"w")

file_content.truncate()
print "content flushed"

print "Enter new content: to save press Ctrl+D"
content = []

while True:
	try:
		line = raw_input(">>")
	except EOFError:
		break
	content.append(line)


for text in content:
	file_content.write(text + "\n")

file_content.close()

print "Cool! here are the new  file contents:"

file_content = open(filename)

print file_content.read()








