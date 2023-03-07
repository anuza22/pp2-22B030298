# #Write a Python program to list only directories, files and all directories, files in a specified path.

import os

path = r'C:\Users\Lenovo\pp2'

files = os.listdir(path)

files = [filenames for filenames in files if os.path.isfile(path+'/'+filenames)]

direc = os.listdir(path)

direc = [dirname for dirname in files if os.path.isdir(path+'/'+dirname)]

print('List of directories:\n',direc)

print('List of files:\n',files)

print('List of directories and files:\n',os.listdir(path))


# for dirname in os.walk(r'C:\Users\Lenovo\pp2\w3schools 1\TSIS5'):
#     print(dirname)
#     # list_of_files.append(filename)




