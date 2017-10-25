import xml.etree.ElementTree as xml

filename = raw_input("Enter FileName: ")

noOfBooks = int(raw_input("Enter no of books: "))

root = xml.Element("Books")

for i in range(noOfBooks):
	bookElement = xml.Element("book")
	root.append(bookElement)

	title = xml.SubElement(bookElement,"title")
	title.text = raw_input("Book Name: ")

	catagory = xml.SubElement(bookElement,"catagory")
	catagory.text = raw_input("Catagory: ")

	price = xml.SubElement(bookElement,"price")
	price.text = raw_input("Price: ")


tree = xml.ElementTree(root)

with open(filename,"w") as file:
	tree.write (file)


print  "File Written Successfully"

#Parsing Xml File:

tree = xml.parse('pyCreatedXml.xml')
root = tree.getroot()

print "<%s>" % root.tag

children = root.getchildren()

for child in children:
	print "<%s>" % child.tag
	sib = child.getchildren()
	for elem in sib:
		print "<%s>%s</%s>" %(elem.tag , elem.text , elem.tag)
	print "</%s>" % child.tag


print "</%s>" % root.tag