import math

#prime factors:
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

#all factors:

def all_factors(n):
    fact=[]
    r = n/2
    for i in range (1,int(r)+1):
        if n%i==0:
            fact.append(i)
    fact.append(n)
    return fact


def is_prime(a):
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            return 0
    return 1