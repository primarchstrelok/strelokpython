#Strelok 021118
#Global library

#Math functions
#Calculates if a number is even and outputs as boolean
def ifEven(a):
    if a % 2 == 0 :
        even = True
    else:
        even = False
    return even
#Calculates an single input as a factorial
def factorial(a):
    c = a
    while a >= 2:
        b = a-1
        c = c*b
        a -= 1
    return c
#Contains 12 digits of pi
def pi():
    pi = 3.14159265359
    return pi
#Calculates the area of a circle from the radius
def circleArea(r):
    area = pi() * r * r
    return area
#Command Functions
#Prompts the user to press enter to continue
def pause():
    input("Press enter to continue")
def winner():
    print("A winner is you")