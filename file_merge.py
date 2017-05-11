#
#
#
#
#
import glob
import os


for f in glob.glob('/Users/kazu/GitHub/python/file*.txt'):
    os.system("cat "+f+" >> OutFile.txt")



#files = glob.glob('/Users/kazu/GitHub/python/*.txt',)   #Display all file lists.
#
#for a in files:
#    print(a)




