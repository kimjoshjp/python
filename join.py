#
#
#
#
# Output file name within Directory

import os, sys

filenames  = ["/Users/kazu/GitHub/python/file1.txt", "/Users/kazu/GitHub/python/file2.txt", "/Users/kazu/GitHub/python/file3.txt"]

with open("/Users/kazu/GitHub/python/file4.txt", 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line + "\n")

