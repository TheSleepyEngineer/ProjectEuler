

#Variables:
dict_pathes={2020:1}
n=0
path_number=0
K=[] # Temporary list
G=[] #Matrix


#Fill the Grid G:
for i in range(0,21):
    for j in range(0,21):
        if j < 10 :
            K.append(i*10 + j)
        else:
            K.append(i*100 + j)
    G.append(K)
    K=[]

def path(i,j,k=20,l=20):
    global path_number
    if i < k:
        path(i+1,j,k,l)
    if j < l:
        path(i,j+1,k,l)
    if i==k and j==l:
        path_number+=1
    return 0



def backward_path(i,j):
    print(i)
    print(j)
    if i==20 and j==20:
        return 0

    elif i<20 and j<20:
        dict_pathes[G[i][j]]= dict_pathes[G[i+1][j]] + dict_pathes[G[i][j+1]]
    elif i < 20:
        dict_pathes[G[i][j]] = dict_pathes[G[i+1][j]]
    else:
        dict_pathes[G[i][j]] = dict_pathes[G[i][j+1]]
    return 0






#main function:

for i in range (20,0, -1):
    for j in range (20,0,-1):
        backward_path(i,j)

print(dict_pathes.get(11))
