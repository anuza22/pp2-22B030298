heads =int(input("numheads : "))
legs = int(input("numlegs : "))

def solve(numheads, numlegs):
    rabbits = numlegs//2 - numheads
    chickens = numheads - rabbits
    print( "rabbits : ", rabbits )
    print("chickens : ", chickens)

solve(heads, legs)

