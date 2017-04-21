#
#
#
#
# Output file name within Directory

import os, sys, datetime

filenames  = ["/Users/kazu/GitHub/python/file1.txt", "/Users/kazu/GitHub/python/file2.txt", "/Users/kazu/GitHub/python/file3.txt"]

new_filename = datetime.datetime.now()

with open("/Users/kazu/GitHub/python/file4.txt", 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)


print(new_filename,'.txt')