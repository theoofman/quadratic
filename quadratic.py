import math
def quadratic(a,b,c):
    x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    return(x1, x2)

while True:
    print("What is A?")
    a = float(input())
    print("What is B?")
    b = float(input())
    print("What is C?")
    c = float(input())
    print(quadratic(a,b,c))
    print("Again?")
    exits = input()
    if exits == "Exit":
        break
