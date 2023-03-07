#Write a Python program that invoke square root function after specific milliseconds.
import time

a = int(input())
b = int(input())

print(a)

time.sleep(b/1000)

print(f'Square root of {a} after {b} miliseconds is {pow(a, 0.5)}')



