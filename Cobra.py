def display(h,key):
    global a2,a,count
    if key!=2:
    	print("-------------------------")
    for d in h:
        for i in range(0, 3, 1):
            if key==2:
            		for j in range(0, 3, 1):
            			for k in range(0,3):
            				
            				if (str(type(d[j][i][k])) == "<class 'list'>"):
            				   		if((len(d[j][i][k]))==1):
            				   			
            				   			a[h.index(d)][j][i][k]=d[j][i][k][0]
            				   			
            				   			count-=1
            				   		else:
            				   			continue
            				   
            
            			    			
            else:
                	try: 
                	    print("|", ' '.join(map(str, d[0][i])), "|", ' '.join(map(str, d[1][i])), "|", ' '.join(map(str, d[2][i])), "|")
                	except:
                		print("|", d[0][i], "|", d[1][i], "|", d[2][i], "|")
            	
            
        if key!=2:
        	print("-------------------------")
        

def update():
	global a2,count
	a2 = [[
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
],[
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
],[
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
]
]
	
	for di in a:
	   	for i in range(0,3):
	   		list =[1,2,3,4,5,6,7,8,9]
	   		for j in range(0,3):
	   		     			for k in range(0,3):
	   		     				if di[i][j][k] in list:
	   		     					list.remove(di[i][j][k])
	   		     			for k in range(0,3):
	   		     				if di[i][j][k]==0:
	   		     					a2[a.index(di)][i][j][k]=list
    	
print("Coordinates:")				
a = [[
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]],
    [[[28, 29, 30], [31, 32, 33], [34, 35, 36]],
    [[37, 38, 39], [40, 41, 42], [43, 44, 45]],
    [[46, 47, 48], [49, 50, 51], [52, 53, 54]]],
    [[[55, 56, 57], [58, 59, 60], [61, 62, 63]],
    [[64, 65, 66], [67, 68, 69], [70, 71, 72]],
    [[73, 74, 75], [76, 77, 78], [79, 80, 81]]
]]

display(a,1)
a = [[
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]],
    [
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
],[
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
]
]


def twist():
    global a,count
    transposed_a = []

    # Loop over each 3D group
    for group in a:
        new_group = []

        # Loop over each 2D matrix in the group
        for matrix in group:
            rows = len(matrix)
            cols = len(matrix[0])

            # Transpose the matrix
            transposed_matrix = []
            for c in range(cols):
                new_row = []
                for r in range(rows):
                    new_row.append(matrix[r][c])
                transposed_matrix.append(new_row)

            new_group.append(transposed_matrix)

        transposed_a.append(new_group)

    rows = len(transposed_a)
    cols = len(transposed_a[0])
    transposed = []
    for c in range(cols):
    	new_row = []
    	for r in range(rows):
    		new_row.append(transposed_a[r][c])
    	transposed.append(new_row)
    a=transposed
    twist2()
   
 
def twist2():
    global a2,count
    transposed_a = []

    # Loop over each 3D group
    for group in a2:
        new_group = []

        # Loop over each 2D matrix in the group
        for matrix in group:
            rows = len(matrix)
            cols = len(matrix[0])

            # Transpose the matrix
            transposed_matrix = []
            for c in range(cols):
                new_row = []
                for r in range(rows):
                    new_row.append(matrix[r][c])
                transposed_matrix.append(new_row)

            new_group.append(transposed_matrix)

        transposed_a.append(new_group)

    rows = len(transposed_a)
    cols = len(transposed_a[0])
    transposed = []
    for c in range(cols):
    	new_row = []
    	for r in range(rows):
    		new_row.append(transposed_a[r][c])
    	transposed.append(new_row)
    a2=transposed
    
			



def fix():
	global a,a2,count
	l=3
	for h in range(0,l):
							for t in range(0,l):
								for r in range(0,l):
									for c in range(0,l):
										for t2 in range(0,l):
											for r2 in range(0,l):
												for c2 in range(0,l):
													if t!=t2:
														if ((r==r2) and (a2[h][t][r][c]!=0)):
															list=a[h][t][r][c]
															list2=a[h][t2][r2][c2]
															list3=a2[h][t][r][c].copy()
															
						
														
															
															
															if ((list2!=0)):
																try:
																	
																	list3.remove(list2)
																	a2[h][t][r][c]=list3
																	
																	if (len(list3)==1):
																		a[h][t][r][c]=list3[0]
																		
																		a2[h][t][r][c]=0
																		count-=1
																		
																except:
																	pass
															
																
														

#Initializing the sudoku puzzle
count=81
a2=[]
co={}
print("Enter coordinates for \n ")
for i in range(1,10):
	print(i," : ",end="")
	code=input(" ")
	value=code.split(" ")
	co[i]=value

for dl in co.keys():
    dal=co[dl]
    for i in dal:
        count-=1
        
        
        j=str(i)+ " "+ str(dl)
        if (int((j.split(" "))[0])) <= 27:
            if (int((j.split(" "))[0])) <= 9:
                if (int((j.split(" "))[0])) <= 3:
                    a[0][0][0][(int((j.split(" "))[0])) - 1] = (int((j.split(" "))[1]))
                elif (int((j.split(" "))[0])) <= 6:
                    a[0][0][1][(int((j.split(" "))[0])) - 4] = (int((j.split(" "))[1]))
                elif (int((j.split(" "))[0])) <= 9:
                    a[0][0][2][(int((j.split(" "))[0])) - 7] = (int((j.split(" "))[1]))
            elif (int((j.split(" "))[0])) <= 18:
                if (int((j.split(" "))[0])) <= 12:
                    a[0][1][0][(int((j.split(" "))[0])) - 10] = (int((j.split(" "))[1]))
                elif (int((j.split(" "))[0])) <= 15:
                    a[0][1][1][(int((j.split(" "))[0])) - 13] = (int((j.split(" "))[1]))
                elif (int((j.split(" "))[0])) <= 18:
                    a[0][1][2][(int((j.split(" "))[0])) - 16] = (int((j.split(" "))[1]))
            elif (int((j.split(" "))[0])) <= 27:
                if (int((j.split(" "))[0])) <= 21:
                    a[0][2][0][(int((j.split(" "))[0])) - 19] = (int((j.split(" "))[1]))
                elif (int((j.split(" "))[0])) <= 24:
                    a[0][2][1][(int((j.split(" "))[0])) - 22] = (int((j.split(" "))[1]))
                elif (int((j.split(" "))[0])) <= 27:
                    a[0][2][2][(int((j.split(" "))[0])) - 25] = (int((j.split(" "))[1]))
        elif (int((j.split(" "))[0])) <= 54:
            if (int((j.split(" "))[0])) <= 36:
                if (int((j.split(" "))[0])) <= 30:
                    a[1][0][0][(int((j.split(" "))[0])) - 28] = (int((j.split(" "))[1]))
                elif (int((j.split(" "))[0])) <= 33:
                    a[1][0][1][(int((j.split(" "))[0])) - 31] = (int((j.split(" "))[1]))
                elif (int((j.split(" "))[0])) <= 36:
                    a[1][0][2][(int((j.split(" "))[0])) - 34] = (int((j.split(" "))[1]))
            elif (int((j.split(" "))[0])) <= 45:
                if (int((j.split(" "))[0])) <= 39:
                    a[1][1][0][(int((j.split(" "))[0])) - 37] = (int((j.split(" "))[1]))
                elif (int((j.split(" "))[0])) <= 42:
                    a[1][1][1][(int((j.split(" "))[0])) - 40] = (int((j.split(" "))[1]))
                elif (int((j.split(" "))[0])) <= 45:
                    a[1][1][2][(int((j.split(" "))[0])) - 43] = (int((j.split(" "))[1]))
            elif (int((j.split(" "))[0])) <= 54:
                if (int((j.split(" "))[0])) <= 48:
                    a[1][2][0][(int((j.split(" "))[0])) - 46] = (int((j.split(" "))[1]))
                elif (int((j.split(" "))[0])) <= 51:
                    a[1][2][1][(int((j.split(" "))[0])) - 49] = (int((j.split(" "))[1]))
                elif (int((j.split(" "))[0])) <= 54:
                    a[1][2][2][(int((j.split(" "))[0])) - 52] = (int((j.split(" "))[1]))
        elif (int((j.split(" "))[0])) <= 81:
            if (int((j.split(" "))[0])) <= 63:
                if (int((j.split(" "))[0])) <= 57:
                    a[2][0][0][(int((j.split(" "))[0])) - 55] = (int((j.split(" "))[1]))
                elif (int((j.split(" "))[0])) <= 60:
                    a[2][0][1][(int((j.split(" "))[0])) -58] = (int((j.split(" "))[1]))
                elif (int((j.split(" "))[0])) <= 63:
                    a[2][0][2][(int((j.split(" "))[0])) - 61] = (int((j.split(" "))[1]))
            elif (int((j.split(" "))[0])) <= 72:
                if (int((j.split(" "))[0])) <= 66:
                    a[2][1][0][(int((j.split(" "))[0])) - 64] = (int((j.split(" "))[1]))
                elif (int((j.split(" "))[0])) <= 69:
                    a[2][1][1][(int((j.split(" "))[0])) - 67] = (int((j.split(" "))[1]))
                elif (int((j.split(" "))[0])) <= 72:
                    a[2][1][2][(int((j.split(" "))[0])) - 70] = (int((j.split(" "))[1]))
            elif (int((j.split(" "))[0])) <= 81:
                if (int((j.split(" "))[0])) <= 75:
                    a[2][2][0][(int((j.split(" "))[0])) - 73] = (int((j.split(" "))[1]))
                elif (int((j.split(" "))[0])) <= 78:
                    a[2][2][1][(int((j.split(" "))[0])) - 76] = (int((j.split(" "))[1]))
                elif (int((j.split(" "))[0])) <= 81:
                    a[2][2][2][(int((j.split(" "))[0])) - 79] = (int((j.split(" "))[1]))
    
    
def block():
	global a,a2,count
	update()
	display(a2,2)
	update()
	
print("Question \n")
display(a,1)
#Checking each blocks

# Checking horizontal

while (count!=0):
		block()
		
		fix()
		
		twist()
		fix()
		twist()
		
print("Solution \n")
display(a,1)
	

						

	
