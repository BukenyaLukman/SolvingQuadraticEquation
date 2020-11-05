import math


def solve_quadratic(a,b,c):
    k = (b*b) - (4 * a * c)
    if k < 0:
       print("Complex root")
    else:
        x1 = (-b + math.sqrt(k))/(2*a) 
        x2 = (-b - math.sqrt(k))/(2*a)
        print(x1, x2)  

print("Enter Coefficients")
a = int(input())
b = int(input())
c = int(input())
solve_quadratic(a,b,c)

