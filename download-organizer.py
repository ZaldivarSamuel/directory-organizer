from os import listdir
from os.path import isfile, join

path = "/Users/samuel/Documents/test"

for f in listdir(path):
    if isfile(join(path, f)):
        print("File: " + f)
