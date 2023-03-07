#Write a Python program with builtin function
# to multiply all the numbers in a list

numbers = [int(i) for i in input().split()]

p = iter(numbers)
mult=1
for i in range(len(numbers)):
    mult*=next(p)

print(mult)

