import datetime


def readfile(filename):
    with open(filename, 'r') as file:
        return file.read()


directory = "/Users/kazu/GitHub/python/"
mfilename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt"
files = ["file1.txt", "file2.txt", "file3.txt"]

with open(directory + mfilename, 'w+') as mfile:
    for file in files:
        mfile.write(readfile(directory + file) + "\n")