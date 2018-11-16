import fractions

result = 1
for i in range (1,21):
    result = result*i/fractions.gcd(result,i)

print(result)

