import math
from functools import reduce

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
    r = math.sqrt(n)
    for i in range (1,int(r)+1):
        if n%i==0:
            fact.append(i)
            fact.append(n//i)
    return fact



def is_prime(a):
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            return 0
    return 1



#Fill a Matrix A with numbers (number by number) from a file:

def get_numbers_from_file(filePath):
    file=open(str(filePath),"r")
    lines=file.readlines()
    A=[]

    for line in lines:
        table=[]
        for integers in line.split():
            table.append(int(integers))
        A.append(table)
    return A

##Fill a Table T with line-long-numbers (line by line) from a file:

def get_lines_from_file(filePath):
    file=open(str(filePath),"r")
    lines=file.readlines()
    T=[]

    for line in lines:
        T.append(int(line))
    return T

