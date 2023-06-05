from sys import argv

script, inp_file = argv

def print_file(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_line(line_no, f):
    print line_no, f.readline()

my_file = open(inp_file)

print "First let's print the whole file:\n"

print_file(my_file)

print "Now let's rewind, kind of like a tape."

rewind(my_file)

print "Let's print three lines:"
# for line  in [1, 4]:
#     print_line(line, my_file)
line = 1
print_line(line, my_file)
line += 1
print_line(line, my_file)
line+=1
print_line(line, my_file)

my_file.close()

