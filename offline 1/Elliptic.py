from sympy import primerange, randprime
import math
import random


def double(x, y, a, p):
    if y == 0:
        return (0, 0)
    s = (3 * x * x + a)
    s = s/(2*y)
    s = s % p
    x_r = (s * s - 2 * x) % p
    y_r = (s * (x - x_r) - y) % p
    return (x_r, y_r)


def addition(x1, y1, x2, y2, a, p):
    if x1 == x2 and y1 == y2:
        return double(x1, y1, a, p)
    s=(y2-y1)/(x2-x1)
    x_r=(s*s-x1-x2)%p
    y_r=(s*(x1-x_r)-y1)%p
    return (x_r, y_r)


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

def calculate_kG(k, x, y, a, p):
    # k in binary
    k_binary = bin(k)[2:]
    print(f"k in binary: {k_binary}")
    # kG
    kG = (x,y)
    for i in range(len(k_binary)):
        if k_binary[i] == '1':
            kG = addition(kG[0], kG[1], x, y, a, p)
        kG = double(kG[0], kG[1], a, p)
    return kG

    
    
    
    
    
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
    
    
    
    