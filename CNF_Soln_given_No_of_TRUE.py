from z3 import *
import random
#Q.1,2
def optimal_sat_sol(l,n,T=None):
    constraint=[]
    for i in (l):
        var1=f'x_{i[0]}'
        var2=f'x_{i[1]}'
        bool_var1=Bool(var1) 
        bool_var2=Bool(var2)
        constraint.append((Or(bool_var1,bool_var2)))
    constraint_0=And(constraint)
    #print(constraint_0)
    sat_list=[]
    s=Solver()
    s.add((constraint_0))
    if s.check()==sat:
        solution=s.model()
        sat_list.append(solution)
        #print(solution)
        size=2**n
        for j in range(size):
            rec_cons=[]
            for i in solution:
                if solution[i]==False:
                    rec_cons.append((Not((Bool(str(i))))))
                if solution[i]==True:
                    rec_cons.append(((Bool(str(i))))) 
            #print(rec_cons)   
            constraint_1=Not(And(rec_cons))
            constraint_0=And(constraint_0,constraint_1)
            s1=Solver()
            s1.add(constraint_0)
            if s1.check()==sat:
                solution=s1.model()
                sat_list.append(solution)
                #print(solution)
            else:
                break  
    print('List of Satisfiability Solutions are:')         
    print(sat_list)
    print('\n')
    h=len(sat_list)
    dic={}
    for i in range(h):
        dic[i]=0
    for i in (sat_list):
        for j in i:
            if i[j]==True:
                dic[sat_list.index(i)]+=1
            else:
                pass    
    print(dic) # Represent dict having count of all ones for all satifiability truth assignment
    print('\n')
    min_no_one=T
    #min_no_one = (min(dic.values()))

    dic_values=[]
    for key,value in dic.items():
        dic_values.append(value)
    if T not in dic_values:
        return f'No solution for {T} no of True'  

    
    key_min_no_one=0
    for key,value in dic.items():
        if value==min_no_one: #dict value=min no of one's
            key_min_no_one=key
            print(sat_list[key_min_no_one])
            
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

n_V=int(input('Total Vertices in Graph:')) 
n_E=int(input('Total Edges in Graph:'))  
print('Give all list of edges with comma separate:')
list_edges=(check_int(n_E,n_V))

T=int(input('In Solution, no of True are:'))
if 'y'in list_edges:
    print('Give integer type input')
elif 'x'in list_edges:
    print('Vertex Index should be less than total vertices index')         
else:
    print(optimal_sat_sol(list_edges,n_V,T))
