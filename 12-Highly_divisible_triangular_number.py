import my_functions

def triangle(n):
    value=0
    for i in range(1,n+1):
        value+=i
    return value

count=0
n=0
i=0
factors=[]
while(count <500):
    i+=1
    n+=i
    if n < 50000:
        continue
    if n%2!=0:
        continue
    factors=my_functions.all_factors(triangle(n))
    count=len(factors)

    print(count)


print(n)

