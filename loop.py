#
#
#
#
#    Loop

a = 13
if a > 10:
    print("This should't happen")
else:
    print("This should happen")

f = open('/Users/kazu/python/apple.txt', 'r')

# Read each line
xyz = f.readline()

# Keep reading line one at a time
# till the file is empty
while xyz:
    print xyz
    xyz = f.readline()

# Close function
f.close()
