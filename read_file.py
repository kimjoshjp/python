#
#
# Testing reading file from Dir

# Open up files
f = open('/Users/kazu/python/apple.txt', 'r')

# Read All files
xyz = f.read()

# Output line
print xyz

# Close function
f.close()
############
f = open('/Users/kazu/python/apple.txt', 'r')

# Read All files
for abc in iter(f):
    print abc
f.close()

