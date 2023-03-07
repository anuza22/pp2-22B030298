#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os

path = r'C:\Users\Lenovo\pp2\pythonClasses1'

test_existence = os.access(path, os.F_OK)
if test_existence:
    print(os.listdir(path))
else:
    print('given path not exists')