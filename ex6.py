x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
print x
print y

print "i said %r" %x
print "i said %s" %y
hilarious = False
joke = "Isn't that joke funny?  %r"

print joke % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
