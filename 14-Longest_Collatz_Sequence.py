def collatz(x):
    k=0
    while (x != 1):
        if x%2==0:
            x=x/2
        else:
            x= 3*x + 1
        k+=1
    return k

i=13
length=0
maximum = 0
n=0

while (i<1000000):
    length=collatz(i)
    if length > maximum :
        maximum = length
        n = i
    i+=1
    print(i)

print(n)
