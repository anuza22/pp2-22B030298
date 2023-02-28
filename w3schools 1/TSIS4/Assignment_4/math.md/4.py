# Write a Python program to calculate the area of a parallelogram.

# Length of base: 5
# Height of parallelogram: 6
# Expected Output: 30.0

def area(l, h):
    return h*l

l = int(input('Length of base: '))
h= int(input('Height of parallelogram: '))

print(area(l, h))
