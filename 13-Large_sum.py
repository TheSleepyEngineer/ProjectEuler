import my_functions

T=my_functions.get_lines_from_file("/tmp/problem13-input.txt")

sum=0
for i in T:
    sum += i
print(sum)

