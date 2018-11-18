def is_palindrom(n):
    length= len(str(n))
    for i in range(0, int(length/2)+1):
        if n/10**(length -1 -i)%10 != int(n%10**(i+1)/10**i):
            return 0
    return 1


currentPal=1

for i in range(1,1000):
    for j in range(i,1000):
        if is_palindrom(i*j) and i*j > currentPal:
            currentPal=i*j


print(currentPal)
