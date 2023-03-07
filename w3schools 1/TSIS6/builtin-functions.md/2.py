#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
words = input()

low = 0
upp = 0

for i in range(len(words)):
    if words[i]>'Z' and words[i]<='z':
        low+=1
    elif words[i]>='A' and words[i]<='Z':
        upp+=1
    
print(low, upp)
