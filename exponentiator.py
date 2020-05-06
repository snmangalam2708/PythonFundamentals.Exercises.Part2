def exponentiate(a,b):
    print("\n",int(a), "raised to",int(b),"is:",int(pow(a,b)), "\n")


def raise_to_fourth_power(a):
    print(a,"raised to 4 is:",exponentiate(a,4),"\n")

square = lambda x: exponentiate(x,2)
cube = lambda y: exponentiate(y,3)
raise_to_fourth = lambda z: exponentiate(z,4)

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))  
exponentiate(n1,n2)
n = int(input("Enter a number: "))
square(n)
cube(n)
raise_to_fourth(n)