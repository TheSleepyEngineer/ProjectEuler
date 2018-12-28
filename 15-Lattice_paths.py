#Fill Grid:
def Fill_grid(G=[]):
	L=[]
	for i in range(1,21):
		for j in range(1,21):
			if j < 10:
				L.append(i*10+j)
			else:
				L.append (i*100+j)
		G.append(L)
		L=[]
	return 0


#Give each point in the grid a value:

def assign_values(G,path_value):
	path_value[G[19][19]]=1

	for i in range(19,-1, -1):
		for j in range(19,-1, -1):

			if i==19 and j==19:
				continue
			if i == 19 :
				path_value[G[i][j]] = path_value[G[i][j+1]]
			elif j == 19:
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


