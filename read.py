#
#
#
#
# Read file and input word and output

# Create File OBJ and sepecify path with write mode

fob = open('/Users/kazu/python/a.txt', 'w')
fob.write('Welocme to Python world')
fob.close()

# Read a.txt with read mode
fob = open('/Users/kazu/python/server_name.txt', 'r')
# print fob.read(3)
print fob.readline()
# read them into xyz
#xyz = fob.read()
#print xyz
#fob.close()
