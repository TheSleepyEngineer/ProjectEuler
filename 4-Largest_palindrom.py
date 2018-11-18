def is_palindrom(n):
    length= len(str(n))
    for i in range(0, int(length/2)+1):
        if n/10**(length -1 -i)%10 != int(n%10**(i+1)/10**i):
            return 0
    return 1



i = 999
j = 999

while (is_palindrom(i*j)==0):
    if i<=j:
        j-=1
    else:
        i-=1

print(i*j)