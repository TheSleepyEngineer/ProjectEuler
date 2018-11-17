import math

def factors(n):
    fact=[]
    r = math.sqrt(n)
    for i in range (2,int(r)+1):
        if n%i==0:
            fact.append(i)
            n=n/i
            while n%i==0:
                fact.append(i)
                n=n/i
    return fact

def is_prime(a):
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            return 0
    return 1