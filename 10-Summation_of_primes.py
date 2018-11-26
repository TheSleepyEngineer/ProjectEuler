import my_functions

total = 2 + 3
below=2000000
step=2
for i in range (5,below,step):
    if my_functions.is_prime(i):
        total += i
        print(i)

print(total)