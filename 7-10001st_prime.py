import my_functions

i = 0
n=1
while i < 10001:
    n+= 1
    if my_functions.is_prime(n):
        i+=1

print n



