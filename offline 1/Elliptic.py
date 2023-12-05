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
    # print(f"Random number between (p+1)- 2root(p) and (p+1)+2 root(p): {e1}")
    
    e2=primeP+1+2*(math.sqrt(primeP))
    e2=int(e2)
    # print(f"Random number between (p+1)- 2root(p) and (p+1)+2 root(p): {e2}")
    
    # generate a random number between e1 and e2
    random_number = randprime(e1, e2)
    # print(f"Random number between e1 and e2: {random_number}")
    return random_number

def generate_a(E):
    # generate a random number between 1 and E-1
    random_number = randprime(1, E-1)
    # print(f"Random number between 1 and E-1: {random_number}")
    return random_number

def generate_b(E):
    # generate a random number between 1 and E-1
    random_number = randprime(1, E-1)
    # print(f"Random number between 1 and E-1: {random_number}")
    return random_number

def generate_point_G(primeP, a, b):

    x=.1
    y=.1
    while(True):
        x=random.randint(1,primeP-1)
        y=math.sqrt((x*x*x+a*x+b))
        if(y.is_integer()):
            break
    
    y=int(y)
    y=y%primeP
    return (x,y)

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
    
    primeP = 17
    a=2
    b=2
    x=5
    y=1
    return (a,b,primeP,x,y)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def get_a_b_p_x_y():
    primeP = randprime(1000000, 10000000)
    E = generate_E(primeP)
    a=generate_a(E)
    b=generate_b(E)
    while((4*a*a*a+27*b*b)%primeP==0):
        a=generate_a(E)
        b=generate_b(E)
    (x,y)=generate_point_G(primeP, a, b)
    print("a: ",a)
    print("b: ",b)
    print("p: ",primeP)
    print("E: ",E)
    print("x: ",x)
    print("y: ",y)
    
    return (a,b,primeP,E,x,y)
    
    
    
    