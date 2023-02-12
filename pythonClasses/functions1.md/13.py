import random 
name = str(input("Hello! What is your name?\n"))

print(f"Well, {name}, I am thinking of a number between 1 and 20.")

num = random.randrange(1, 20)
print(num)

cnt =1

while True:
    print("Take a guess")
    guess=int(input())
    if num>guess:
        print("Your guess is too low.")
    elif num<guess:
        print("Your guess is too high.")
    else:
        print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
        break
    cnt+=1
    
    

