#Write a Python program to write a list to a file.

list_of_words = [i for i in input().split()]

#1 method
with open('C:/Users/Lenovo/pp2/w3schools 1/TSIS6/dir-and-files.md/test.txt', 'w') as f:
    f.write('\n'.join(list_of_words))

# 2 method
# file = open('C:/Users/Lenovo/pp2/w3schools 1/TSIS6/dir-and-files.md/test.txt', 'w')
# for word in list_of_words:
# 	file.write(word+"\n")
# file.close()