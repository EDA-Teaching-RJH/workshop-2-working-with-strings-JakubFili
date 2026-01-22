import math  

def main():
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))

    c = pythag(a, b)
    print("The hypotenuse is:", c)


def pythag(A, B):
    c = math.sqrt(A**2 + B**2)
    return c




main()