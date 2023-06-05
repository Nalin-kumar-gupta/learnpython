from sys import argv

script, filename = argv

txt = open(filename)

print "here is your file %r " %filename
print txt.read()