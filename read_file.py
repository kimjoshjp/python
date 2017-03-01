#
#
# Testing reading file from Dir

# Open up files
fob = open('/Users/kazu/python/apple.txt', 'r')

# Read All files into xyz
xyz = fob.read()

# Output line
print xyz

# Close function
fob.close()


############ Open up file with read mode
fob = open('/Users/kazu/python/apple.txt', 'r')

# Read All files
for abc in iter(fob):
    print abc
fob.close()

