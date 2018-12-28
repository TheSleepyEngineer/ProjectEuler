#Fill Grid:
def Fill_grid(G=[]):
	L=[]
	for i in range(1,22):
		for j in range(1,22):
			if j < 10:
				L.append(i*10+j)
			else:
				L.append (i*100+j)
		G.append(L)
		L=[]
	return 0


#Give each point in the grid a value:

def assign_values(G,path_value):
	path_value[G[20][20]]=1

	for i in range(20,-1, -1):
		for j in range(20,-1, -1):

			if i==20 and j==20:
				continue
			if i == 20 :
				path_value[G[i][j]] = path_value[G[i][j+1]]
			elif j == 20:
				path_value[G[i][j]] = path_value[G[i+1][j]]
			else :
				path_value[G[i][j]] = path_value[G[i][j+1]] + path_value[G[i+1][j]]

	return 0

# main function:

G=[]
path_value={}
Fill_grid(G)
assign_values(G,path_value)

print(path_value[G[0][0]])

