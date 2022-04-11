import os
from os import listdir
from os.path import isfile, join
import shutil

# Get file extension for each file.
# Create a new folder for that extension if not already created
# Move file to that folder

path = "/Users/samuel/Documents/test"
folder_set = set()

for f in listdir(path):
    if isfile(join(path, f)):

        extension_index = f.rfind('.')
        extension = f[extension_index + 1:]

        if extension not in folder_set:
            folder_set.add(extension)
            folder_path = path + "/" + extension
            os.mkdir(folder_path)

        original_path = path + "/" + f
        new_path = path + "/" + extension + "/" + f

        shutil.move(original_path, new_path)
