from z3 import *
import random
def str_to_list(constraint):
    collect=constraint.split('v')  
    #print(collect) 
    list_variables=[]
    for s in collect:
        start,end=0,0
        if s[start]=='(':
            while s[end]!=')':
                end=end+1   
            clause=s[start+1:end].split('^')   
            #print(clause)
            list_variables.append(clause)
    #print(list_variables) 
    final_solution=Optimal_Variables(list_variables)
    return final_solution
    
def Optimal_Variables(list_variables):
    optimal_list_var=[]
    for clause in list_variables:
        #print(clause)
        s=set()
        for j in clause:
            if j[1:] in clause:
                s=set()
                break
            else:
                s.add(j)        
        if len(s)==0:
            pass
        else:        
            optimal_list_var.append(list(s)) 
            break
    #print(optimal_list_var)    
    if len(optimal_list_var)==0:
        return 'No Solution' 
    else:
        solution=bool_solution(optimal_list_var,list_variables) 
        return solution
      
def bool_solution(optimal_list_var,list_variables):
    #print(list_variables) 
    #print(optimal_list_var)

    s=set()
    for clause in list_variables:  
        for j in clause:
            if j[1:] in clause:
                pass
            else:
                s.add(j) 
    collect_distn_vars=(list(s)) 
    #print(collect_distn_vars)
    dist_optiml_vars=[]
    for i in optimal_list_var:
        for  j in i:
            dist_optiml_vars.append(j)  
    print('distict vars',collect_distn_vars) #distict all inputs variables
    print('optimal vars',dist_optiml_vars) #distinct optimal variables inside a single list
    solution_set=set()
    for var in collect_distn_vars:
        #print(var[0])
        if var in dist_optiml_vars:
            if var[0]=='~':
                solution_set.add(f'{var[1:]}=False') 
            else:
                solution_set.add(f'{var}=True') 
        elif f'~{var}' in   dist_optiml_vars:
            pass      
        else:
            if var[0]=='~':
                solution_set.add(f'{var[1:]}=False') 
            else:    
                r=random.random()
                output = round(r)
                if output==1:
                    solution_set.add(f'{var}=True')
                else:
                    solution_set.add(f'{var}=False')                
    lst=list(solution_set) 
    #print(lst)               
    s=sorted(lst) 
    #print(s)
    return s

#constraint=s="(x1^~x1)"                         
#constraint="(x1^~x1)v(~x3^x3)"
#constraint=s="(x1^x1)"
#constraint="(x1^~x1)v(x2^x3)"
#constraint="(x2^x3)v(x4^~x4)"
#constraint="(x1^x2)v(x3^x4)v(x5^x6)"
constraint="(x1^~x2)v(x2^x3)"
print(str_to_list(constraint))