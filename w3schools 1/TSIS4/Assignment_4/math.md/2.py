# Write a Python program to calculate the area of a trapezoid.

# Height: 5
# Base, first value: 5
# Base, second value: 6
# Expected Output: 27.5

def area(h, a, b):
    return (a+b)*h/2

h = int(input('Height: '))
a = int(input('Base, first value: '))
b = int(input('Base, second value: '))

print(area(h, a, b))
