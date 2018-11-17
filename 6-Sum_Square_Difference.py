sum_square=0
square_sum=0

for i in range(1,101):
    sum_square+=i*i
    square_sum += i

print(square_sum*square_sum - sum_square)