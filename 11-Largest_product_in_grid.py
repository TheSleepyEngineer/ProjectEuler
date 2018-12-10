A=[]

#Fill the Matrix A with numbers:

file=open("/tmp/Largest_product.txt","r")
lines=file.readlines()

for line in lines:
    table=[]
    for integers in line.split():
        table.append(int(integers))
    A.append(table)



#       Actual Program

#Product functions:

def right_product(i,j):
    return A[i][j]*A[i][j+1]*A[i][j+2]*A[i][j+3]

def down_product(i,j):
    return A[i][j]*A[i+1][j]*A[i+2][j]*A[i+3][j]

def diag_right_product(i,j):
    return A[i][j]*A[i+1][j+1]*A[i+2][j+2]*A[i+3][j+3]

def diag_left_product(i,j):
    return A[i][j]*A[i+1][j-1]*A[i+2][j-2]*A[i+3][j-3]

# main code :

biggest = 0
for i in range(0,16):
    for j in range(0,19):
        if j < 3:
            biggest = max(biggest, right_product(i, j))
            biggest = max(biggest, down_product(i, j))
            biggest = max(biggest, diag_right_product(i, j))
        elif j > 16:
            biggest = max(biggest, down_product(i, j))
            biggest = max(biggest, diag_left_product(i, j))
        else:
            biggest = max(biggest, right_product(i, j))
            biggest = max(biggest, down_product(i, j))
            biggest = max(biggest, diag_right_product(i, j))
            biggest = max(biggest, diag_left_product(i, j))


print(biggest)



