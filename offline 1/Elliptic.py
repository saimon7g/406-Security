from sympy import primerange, randprime
import math
import random

def point_double(x, y, a, b, p):
    if x == 0 and y == 0:
        return (0, 0)
    
    numerator = (3 * x * x + a)
    denominator = pow(2 * y, -1, p) % p
    slope = (numerator * denominator) % p
    
    x3 = (slope * slope - 2 * x) % p
    y3 = (slope * (x - x3) - y) % p
    
    return (x3, y3)
    
def point_addition(x1, y1, x2, y2, a, b, p):
    if x1 == 0 and y1 == 0:
        return (x2, y2)
    if x2 == 0 and y2 == 0:
        return (x1, y1)
    if x1 == x2 and y1 == y2:
        return point_double(x1, y1, a, b, p)
    slope = ((y2 - y1) * pow(x2 - x1, -1, p)) % p
    x3 = (slope * slope - x1 - x2) % p
    y3 = (slope * (x1 - x3) - y1) % p
    
    return (x3, y3)

def generate_E(primeP):
    # random number between (p+1)- 2root(p) and (p+1)+2 root(p)
    e1=primeP+1-2*(math.sqrt(primeP))
    e1=int(e1)
    e2=primeP+1+2*(math.sqrt(primeP))
    e2=int(e2)
    random_number = randprime(e1, e2)
    print(f"Random number: {random_number}")
    return random_number

def calculate_kG(a,b,p,x,y,k):
    result = (0, 0)
    binary = bin(k)[2:]
    # print(f"Binary: {binary}")
    for i in binary:
        result = point_double(result[0], result[1], a, b, p)
        if i == '1':
            result = point_addition(result[0], result[1], x, y, a, b, p)
    return result

def get_parameters():
    
    primeP=randprime(10000000000000, 99999999999999999999)
    print(f"Prime number: {primeP}")
    a=random.randint(1,10000000)
    x=random.randint(1,primeP-1)
    y=random.randint(1,primeP-1)
    b=(y*y-x*x*x-a*x)%primeP
    while(4*a*a*a+27*b*b==0):
        a=random.randint(1,10000000)
        x=random.randint(1,primeP-1)
        y=random.randint(1,primeP-1)
        b=(y*y-x*x*x-a*x)%primeP
    # primeP = 17
    # a=2
    # b=2
    # x=5
    # y=1
    print(f"a: {a}, b: {b}, x: {x}, y: {y}")
    return (a,b,primeP,x,y)