import math

for b in range (2,501):
    for a in range (1,b):
        c = math.sqrt(a*a + b*b)
        if a + b + c == 1000 :
            print(a*b*c)
