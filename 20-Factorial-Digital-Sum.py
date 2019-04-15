from math import factorial

text_number = str(factorial(100))

total = 0

for number in text_number:
    total += int(number)


print(total)