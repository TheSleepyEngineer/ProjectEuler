x=2**1000
number=str(x)
result=0

for i in range (0, len(number)):
    result+= int(number[i])

print(result)