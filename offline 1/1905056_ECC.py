from sympy import primerange, randprime
import math
import random
import time

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
    random_number = random.randint(e1, e2)
    # print(f"Random number: {random_number}")
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

def get_parameters(k):
    
    max=pow(2,int(k))
    primeP=randprime(max/2,max)
    # print(f"Prime number: {primeP}")
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
    # print(f"a: {a}, b: {b}, x: {x}, y: {y}")
    return (a,b,primeP,x,y)





def task2_by_bit(k):
    
    parameters=get_parameters(k)
    a=parameters[0]
    b=parameters[1]
    p=parameters[2]
    x=parameters[3]
    y=parameters[4]
    e=generate_E(p)
    start_time1=time.time()
    private_key_1=random.randint(1,e)
    public_key=calculate_kG(a,b,p,x,y,private_key_1)
    start_time2=time.time()
    private_key_2=random.randint(1,e)
    public_key_2=calculate_kG(a,b,p,x,y,private_key_2)
    
    encryption_key_1=calculate_kG(a,b,p,public_key_2[0],public_key_2[1],private_key_1)[0]
    end_time1=time.time()
    encryption_key_2=calculate_kG(a,b,p,public_key[0],public_key[1],private_key_2)[0]
    end_time2=time.time()
    return (end_time1-start_time1,end_time2-start_time2)

def task2():
    results1=[]
    results2=[]
    result3=[]
    results4=[]
    for j in range(1,4):
        k=input("input number of bits: ")
        total_time=0
        timeA=0
        timeB=0
        for i in range(1,10):
            start_time=time.time()
            res=task2_by_bit(k)
            end_time=time.time()
            total_time+=end_time-start_time
            timeA+=res[0]
            timeB+=res[1]
            
        results1.append(k)
        results2.append(timeA/10)
        result3.append(timeB/10)
        results4.append(total_time/10)
        
        
    for j in range(0,3):
        print(f"Average time to calculate A for {results1[j]} bits       : {1000*results2[j]}ms")
        print(f"Average time to calculate B for {results1[j]} bits       : {1000*result3[j]}ms")
        print(f"Average time to calculate total for {results1[j]} bits   : {1000*results4[j]}ms")
        
        
    
    
    

task2()