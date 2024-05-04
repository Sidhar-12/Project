def check_int(n_E,n_V):
    edges=[]
    for i in range(n_E):
        inpt=input('').split(' ')
        l=[]
        for j in inpt:
            try:
                k=int(j)
                if k>n_V:
                    return ['x']
                l.append(k)
            except:
                return  ['y']    
        edges.append(l)   
    return edges 



name = input("Text File name which will be created:")
n_V=int(input('Total Vertices in Graph:')) 



'''Creating Graph by giving user input'''
# n_E=int(input('Total Edges in Graph:'))  
# print('Give all list of edges with comma separate:')
# list_edges=(check_int(n_E,n_V))

# #T=int(input('In Solution, no of True are:'))
# if 'y'in list_edges:
#     print('Give integer type input')
# elif 'x'in list_edges:
#     print(f'Vertex Index should be less than total vertices index {n_V}')         
# else:
#     file=open(r"C:\Users\Desktop\CODE\INPUT\{}.txt".format(name),"w")
#     file.write(str(n_V)+'\n') #adding no of vertices in file
#     for edge in list_edges:
#         #file.write(str(edge[0]),str(edge[1])+'\n') 
#         file.write(str(edge[0]) + ',' + str(edge[1]) + '\n') #adding edges in file   



''' Creating Cyclic and path Graph'''
# '''file=open(r"C:\Users\Desktop\CODE\INPUT\{}.txt".format(name),"w")
# file.write(str(n_V)+'\n')
# for i in  range(1,n_V):
#     file.write(str(i) + ',' + str(i+1) + '\n') #make file for path

# #for cycle
# file.write(str(n_V) + ',' + str(1) + '\n')'''


'''For Creating Complete Graph'''
file=open(r"C:\Users\Desktop\CODE\INPUT\{}.txt".format(name),"w")
file.write(str(n_V)+'\n')
for i in range(1,n_V+1):
    for j in range(i+1,n_V+1):
        file.write(str(i) + ',' + str(j) + '\n')
file.write(str(n_V) + ',' + str(1) + '\n')        
        

