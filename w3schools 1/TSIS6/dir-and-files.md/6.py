#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import os, string

os.chdir(r'C:\Users\Lenovo\pp2\w3schools 1\TSIS6' )

alphabet = string.ascii_uppercase

for letter in alphabet:
    with open(letter+'.txt', 'w') as f:
        f.write(letter)



