
from z3 import *
import random
import networkx as nx
import matplotlib.pyplot as plt

'''def MVC_Visualisation(list_edges,selected_vertex_cover,n):
    print(selected_vertex_cover) 
    
    G = nx.Graph() # Create an empty undirected graph
    
    #n=int(input)
    v_list=[]
    for i in range(1,n+1):
        v_list.append(i)
    #print(G.nodes())
    G.add_nodes_from(v_list)
    G.add_edges_from(list_edges)
    colors=[]
    for vertex in G.nodes():
        print(vertex)
        if vertex in selected_vertex_cover:
            colors.append('red')
        else:
            colors.append('blue') 
    #pickle.dump(dg, open('/tmp/graph.txt', 'w'))
    pickle.dump(G, open('q.txt','wb'))
    
    dg = pickle.load(open('q.txt','rb'))
    nx.draw(dg, with_labels=True, node_color=colors, node_size=500)
    plt.plot([], [],'o', label='Vertex Cover', color='red')
    plt.legend(loc='upper left')
    #plt.show()
    #return f'One of the minimum Vertx Cover:{random_vertex_cover}'''

def index_solution(sat_list,dic,min_no_one,list_edges,n):
    req_solution=[]
    key_min_no_one=0
    for key,value in dic.items():
        if value==min_no_one: #dict value=min no of one's
            key_min_no_one=key
            req_solution.append(sat_list[key_min_no_one])
    #print((req_solution)) #list of all satisfied solutions
    str_req_soln=[] #collecting truth assisgnments,true.
    for i in req_solution:
        l=[]
        for j in i:
            if str(i[j])=='True':
                l.append(str(j))
        str_req_soln.append(l) 
    #print(str_req_soln)  
    vertex_cover=[]
    for i in str_req_soln:
        l=[]
        for j in i:
            l.append(int(j[2:]))        
        vertex_cover.append(l)
        print(l)
    
    for i in range(len(vertex_cover)):
        demo_vertex=1
        with open(r"C:\Users\Desktop\CODE\OUTPUT\G{}.txt".format(i+1), "w") as file:
            for j in range(n):
                if demo_vertex in vertex_cover[i]:
                    file.write(str(1) + '\n')
                else:
                    file.write(str(0) + '\n')
                demo_vertex+=1
            for edge in list_edges:
                #file.write(str(edge[0]),str(edge[1])+'\n') 
                file.write(str(edge[0]) + ',' + str(edge[1]) + '\n')
        #k=MVC_Visualisation(list_edges,vertex_cover[i],n) 
    print('All vertex covers with given truth values:') 
    return vertex_cover         

def optimal_sat_sol(list_edges,n,T=None): #n=no. of vertices
    constraint=[]
    for i in (list_edges):
        var1=f'x_{i[0]}'
        var2=f'x_{i[1]}'
        bool_var1=Bool(var1) 
        bool_var2=Bool(var2)
        #print(int(bool_var1))
        constraint.append((Or(bool_var1,bool_var2)))
    constraint_0=And(constraint)
    #print(constraint_0)
    sat_list=[]
    s=Solver()
    s.add((constraint_0))
    if s.check()==sat:
        solution=s.model()
        sat_list.append(solution)
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
    #print('List of Satisfiability Solutions are:')         
    #print(sat_list)
    #print('\n')
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
    #print(dic) # Represent dict having count of all ones for all satifiability truth assignment
    #print('\n')
    min_no_one=T
    #min_no_one = (min(dic.values()))
    dic_values=[]
    for key,value in dic.items():
        dic_values.append(value)
    if min_no_one not in dic_values:
        return f'No solution for {min_no_one} no of Truth values'
    else:       
        l=index_solution(sat_list,dic,min_no_one,list_edges,n)   
        return l 
   
'''def check_int(n_E,n_V):
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
    print(f'Vertex Index should be less than total vertices index {n_V}')         
else:
    print(optimal_sat_sol(list_edges,n_V,T))''' 

file_name=input('which file want to Open to Find Vertex Cover of the Graph:')
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
print(optimal_sat_sol(list_edges,n,T))