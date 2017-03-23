#
#
#
#
#    Loop

a = 13
if a > 10:
    print("This should't happen")  # if a is larget than 10 then print this ones.
else:
    print("This should happen")

f = open('/Users/kazunorif/GitHub/python/apple.txt', 'r')

# Read each line
xyz = f.readline()   #Real all line and then put into xyz

# Keep reading line one at a time
# till the file is empty
while xyz:
    print (xyz)
    xyz = f.readline()

# Close function
f.close()
