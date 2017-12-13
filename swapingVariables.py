x = int(raw_input("Enter Value for x"))
y = int(raw_input("Enter Value for y"))

print "Before Swaping:\n x= %d y= %d" % (x,y)

(x,y) = (y,x)

print "After Swaping:\n x= %d y= %d" % (x,y)
