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