#
#
# Testing reading file from Dir

# Open up files
#fob = open('/Users/kazu/python/apple.txt', 'r')
with open('/Users/kazunorif/GitHub/python/apple.txt', 'r') as fob:
# Read All files into xyz
    xyz = fob.read()

# Output line
print xyz

# Close function
fob.close()


# Open up file with read mode
fob = open('/Users/kazunorif/GitHub/python/apple.txt', 'r')

# Put them into listme
listme = fob.readlines()
# fob.close()

# Repalce Orange with banana with \n
listme[3] = "Orange\n"

# Open up again and re-write line and close
fob = open('/Users/kazunorif/GitHub/python/apple.txt', 'w')
fob.writelines(listme)
fob.close()

# Read All files
# for abc in iter(fob):
#    print abc
# fob.close()

zoo = ["\nlion\n", "monky\n", "elephant\n"]
if __name__ == '__main__':
    f = open('/Users/kazunorif/GitHub/python/a.txt', 'a')
    f.writelines(zoo)
    f.close()
