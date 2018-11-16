import fractions

def lcm(a, b):
    gc = fractions.gcd(a,b)
    return a*b/gc

result = 1
for i in range (1,21):
    result = lcm(result, i)

print(result)

