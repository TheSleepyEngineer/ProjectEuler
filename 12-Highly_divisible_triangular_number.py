import my_functions


count=0
n=0
i=0
factors=[]
while(count <500):
    i+=1
    n+=i
#    if n%2!=0:
#        continue
    factors=my_functions.all_factors(n)
    count=len(factors)


print(n)

