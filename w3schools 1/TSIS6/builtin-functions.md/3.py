#Write a Python program with builtin function that checks whether a passed string is palindrome or not.

word = input()
word = [i for a,i in enumerate(word)]
words1 = list(reversed(word))

if word==words1:
    print('Palindrome')
else:
    print('Not palindrome')