from z3 import *
import random
#Q.1,2
def optimal_sat_sol(l,n):
    constraint=[]
    #print(l)
    for i in l:
        var1=f'x_{i[0]}'
        var2=f'x_{i[1]}'
        bool_var1=Bool(var1) 
        bool_var2=Bool(var2)
        constraint.append((Or(bool_var1,bool_var2)))
    constraint_0=And(constraint)
    #print(constraint_0)
    sat_list=[]
    s=Solver()
    s.add(constraint_0)
    if s.check()==sat:
        solution=s.model()
        sat_list.append(solution)
        #print(solution)
        size=2**v
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
    min_no_one = (min(dic.values()))
    key_min_no_one=0
    for key,value in dic.items():
        if value==min_no_one: #dict value=min no of one's
            key_min_no_one=key
            print(sat_list[key_min_no_one])
            
n=int(input('Pairs of variables:'))
v=int(input('No of Variables:'))
print('Enter all pairs of variables:')
if n>=0:
    l=[]
    for i in range(n):
        l.append(input(''))
    list_edges=[]
    for i in range(len(l)):
        list_edges.append([int(l[i][0]),int(l[i][1])])    
    (optimal_sat_sol(list_edges,v))   
else: 
    print('Take Positive Number:')

