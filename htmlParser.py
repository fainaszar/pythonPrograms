# Enter your code here. Read input from STDIN. Print output to STDOUT
from HTMLParser import HTMLParser
import re
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start :", tag
        for (attr,value) in attrs:
            print "-> %s > %s" % (attr,value)
    def handle_endtag(self, tag):
        print "End   :", tag
    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        for (attr,value) in attrs:
            print "-> %s > %s" % (attr,value)

    #Handling Comments also

    def handle_comment(self, data):
        
        if "\n" in data:
            print ">>> Multi-line Comment\n" , data
        else:
            print ">>> Single-line Comment\n" , data
            
    def handle_data(self, data):
        if data != "\n":
            print ">>> Data\n", data


# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
N = int(raw_input())
inp=""
for i in range(N):
    x = raw_input()
    if re.match(r'^<!--[ a-zA-z=-_$<>]*-->$',x):
        pass
    else:
        inp+=x
parser.feed(inp)