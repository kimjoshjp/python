#
#
#
#
# Read file and input word and output

# Create File OBJ and sepecify path with write mode

fob = open('/Users/kazu/GitHub/python/python/a.txt', 'w')
fob.write('Welocme to Python world')
fob.close()

fob = open('/Users/kazu/GitHub/python/python/a.txt', 'r')
print fob.read()

# Read a.txt with read mode
fob = open('/Users/kazu/GitHub/python/python/server.txt', 'r')
# print fob.read(3)

# Read one line
print fob.readline()

# Read all lines
print fob.readlines()
# read them into xyz
#xyz = fob.read()
#print xyz
#fob.close()
