from z3 import *
from pathlib import Path
import os
s=Solver()
def Z3_solver(list_edges,n,T,file_name):
    eqn=0
    for i in range(n):
        var=f'x{i+1}'
        x=Int(var) 
        eqn=eqn+x  
        s.add(x>=0)
        s.add(x<=1)
    #print(eqn) 
    s.add(eqn==T)   
    for i in list_edges:
        var1=f'x{i[0]}'
        var2=f'x{i[1]}'
        int_var1=Int(var1) 
        int_var2=Int(var2) 
        s.add(int_var1+int_var2 >=1) 
     
    if s.check()==sat:
        solution=(s.model())
        solution=(solution) 
        count=1

        directory_path = Path(r"C:\Users\Desktop\CODE\OUTPUT")
        subfolder_name = f'{file_name}_T{T}'
        #print(subfolder_name)
        new_folder_path = directory_path / subfolder_name
        new_folder_path.mkdir(parents=True, exist_ok=True) #creating subfolder of name of given input

        file=open(new_folder_path / "G1.txt", "w") #adding file inside subfolder
        l=[]
        #count=1
        for i in solution:
            if solution[i]==1:
                l.append(int(str(i)[1:]))
        demo=1
        for i in range(len(solution)):
            if demo in l: #adding 1,0 in file in plaace of satisfying soln
                file.write(str(1) + '\n')
                demo+=1
            else:
                file.write(str(0) + '\n') 
                demo+=1 
        for edge in list_edges: #adding edge in file
            file.write(str(edge[0]) + ',' + str(edge[1]) + '\n')             
        '''creating eqn'''

        while True:          
            eq=0
            for i in solution:                   
                if solution[i]==1:
                    eq=eq+(Int(str(i)))
       
            s.add(eq!=T) #To finding another solution, adding this eqn in solver
            if s.check()==sat: 
                solution=s.model() 
                count+=1 
                #print(solution)                
                l=[]
                for i in solution:
                    if solution[i]==1:
                        l.append(int(str(i)[1:]))

                file=open(new_folder_path / "G{}.txt".format(count), "w")      
                demo=1
                for i in range(len(solution)):   
                    if demo in l: #adding 1,0 in file in plaace of satisfying soln
                        file.write(str(1) + '\n')
                        demo+=1
                    else:
                        file.write(str(0) + '\n') 
                        demo+=1 
                       
                for edge in list_edges: #adding edge in file
                    file.write(str(edge[0]) + ',' + str(edge[1]) + '\n')
                 
            else:
                print('Output Folder and Text file has created')
                break 
    else:
        print(f'No Solution for {T} no of True Values.')        

file_name=input('which file want to Open to Find Vertex Cover of the Graph:')
#print(file_name)
file=open("C:\\Users\\Desktop\\CODE\\INPUT\\{}.txt".format(file_name),"r")
#print(file)
n=0 #no of vertices
list_edges=[]
for line in file:
    try:
        n=int(line.strip())
    except:
        edge = [int(x.strip()) for x in line.split(',')]
        list_edges.append(edge)   
#print(list_edges,n)         
T=int(input('In Solution, no of True are:'))
(Z3_solver(list_edges,n,T,file_name))
        