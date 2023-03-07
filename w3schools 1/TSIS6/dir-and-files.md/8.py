import os

path = r'C:\Users\Lenovo\OneDrive\Рабочий стол\tsis3'

os.mkdir(path)

print(os.access(path, os.F_OK))

os.rmdir(path)



