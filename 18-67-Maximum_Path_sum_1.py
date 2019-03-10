#Fill Values into Matrix M

M=[]

file=open("/tmp/MaximumPathSum_2","r")
lines=file.readlines()

for line in lines:
    table=[]
    for integers in line.split():
        table.append(int(integers))
    M.append(table)

number_of_rows= len(M)
last_row=number_of_rows -1



# Main program :


for i in range(last_row-1, -1, -1):
    number_of_columns= len(M[i])


    for j in range(0,number_of_columns):
        M[i][j]= M[i][j] + max(M[i+1][j], M[i+1][j+1])

print(M[0][0])
