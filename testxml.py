from xml.dom.minidom import parse
import xml.dom.minidom


DOMTree = xml.dom.minidom.parse("xmlTest.xml")
collection = DOMTree.documentElement

if collection.hasAttribute("shelf"):
	print "Root element is: %s" % collection.getAttribute("shelf")

	movies = collection.getElementsByTagName("movie")

	for movie in movies:
		print "----MOVIE----"

		if movie.hasAttribute("title"):
			print "Title: %s" % movie.getAttribute("title")


		type = movie.getElementsByTagName('type')[0]
		print "Type: %s" % type.childNodes[0].data
		description = movie.getElementsByTagName('description')[0]
		print "description: %s" % description.childNodes[0].data