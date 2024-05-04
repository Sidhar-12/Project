from z3 import *
import random
import networkx as nx
import matplotlib.pyplot as plt
import pickle

def Visualise_Max_Match(Remng_B_edge,Attack_edge):
    #print(Remng_B_edge)
    bipartite_edges=sorted(Remng_B_edge) #after attacking the edge, remaing bipartite graph
    partition1=[]
    partition2=[]
    for i in Remng_B_edge:
        if i[0] not in partition1:
            partition1.append(i[0])
        if i[1] not in partition2:    
            partition2.append(i[1])
    #print('edges',bipartite_edges)    
    #print(partition1,partition2)    
    B = nx.Graph()
    B.add_nodes_from(partition1,bipartite=0)
    B.add_nodes_from(partition2,bipartite=1)
    B.add_edges_from(bipartite_edges)
    #max_matching = nx.maximal_matching(G)
    '''pos = nx.bipartite_layout(B, partition1)
    nx.draw(B, pos, with_labels=True, node_color=['b']*len(partition1) + ['r']*len(partition2), node_size=500)
    plt.show() # Remaining bipartite graph visualisation after attacking the edge'''

    max_matching = nx.maximal_matching(B) #find max matching of the remaining graph, this is in set form
    #print(max_matching)
    j=tuple(Attack_edge)
    max_matching.add(j)   
    #print(max_matching) 
    partition3=[]
    partition4=[]
    for i in max_matching:
        if i[0] not in partition3:
            partition3.append(i[0])
        if i[1] not in partition4:    
            partition4.append(i[1]) 

    B_M = nx.Graph()
    B_M.add_nodes_from(partition3,bipartite=0)
    B_M.add_nodes_from(partition4,bipartite=1)
    B_M.add_edges_from(max_matching)
    #B_M.add_edges_from(Attack)

    pos = nx.bipartite_layout(B_M, partition3)
    #nx.draw(B, pos, with_labels=True, node_color=['b']*len(partition1) + ['r']*len(partition2), node_size=500)
    nx.draw(B_M, pos, with_labels=True, node_color=['b']*len(partition3) + ['r']*len(partition4), node_size=500)
    plt.show()

def Maximum_Matching_Edges(B_edge):
    #print(bipartite_edge)
    bipartite_edges=[]
    for i in B_edge:
        bipartite_edges.append(list(i))  
    print('Enter Youtr Attack Edge with space separation:')
    inpt=input('').split(' ')
    Attack_edge=[]
    for i in inpt:
        Attack_edge.append(i)
    #print('attack',Attack_edge) 
    Remng_B_edge=[] #Matching edge from bipartite graph except Attack one 
    for i,x in enumerate(bipartite_edges):
        if x[0] in Attack_edge or x[1] in Attack_edge:
            pass
        else:
            Remng_B_edge.append(x)
    #print(Remng_B_edge)
    Visualise_Max_Match(Remng_B_edge,Attack_edge)     
    

def bipartite_visualisation(bipartite_edges,s1,s2):
    #print(bipartite_edges,s1,s2)
    bipartite_edges=sorted(bipartite_edges)
    partition1=[]
    partition2=[]
    for i in bipartite_edges:
        if i[0] not in partition1:
            partition1.append(i[0])
        if i[1] not in partition2:    
            partition2.append(i[1])
    #print(bipartite_edges)    
    #print(partition1,partition2)    
    B = nx.Graph()
    B.add_nodes_from(partition1,bipartite=0)
    B.add_nodes_from(partition2,bipartite=1)
    B.add_edges_from(bipartite_edges)
    pos = nx.bipartite_layout(B, partition1)
    nx.draw(B, pos, with_labels=True, node_color=['b']*len(partition1) + ['r']*len(partition2), node_size=500)
    plt.show()
    #print('Randomly choose 2 vertex cover of Graph')
    #return s1,s2
    Maximum_Matching_Edges(bipartite_edges)

def bipartite_graph(list_edges,n,s1,s2): #n=no of vertices,s1,s2=2 random vertex cover.
    #print(list_edges)
    #print(s1,s2)
    undirected_edge_list=[] #collecting all undirected edges and ith self loops 
    for edge in list_edges:
        undirected_edge_list.append([edge[0],edge[1]])
        undirected_edge_list.append([edge[1],edge[0]])
    
    #adding self loop edges in undirected edge list 
    Nodes_existing_edges=[]# collecting all nodes from given graph edges
    for edges in list_edges:
        for vertex in edges:
            if vertex not in Nodes_existing_edges:
                Nodes_existing_edges.append(vertex)
            else:
                pass
    #print(Nodes_existing_edges)
    for node in Nodes_existing_edges:
        undirected_edge_list.append([node,node])
    #print(undirected_edge_list)  
    edges_cmbntn_s1s2=[]#combine all vertices betn ss1 and s2
    for node1 in s1:
        for node2 in s2:
            edges_cmbntn_s1s2.append([node1,node2])

    bipartite_edges=[]
    for edge in  edges_cmbntn_s1s2:
        if edge in  undirected_edge_list:
            #for node in range(len(edge)):
            bipartite_edges.append((f'x{edge[0]}',f'y{edge[1]}'))
    #print(bipartite_edges)
    k=bipartite_visualisation(bipartite_edges,s1,s2)
    return k


def MVC_Visualisation(list_edges,n,s1,s2):#n=no of vertices
    print('edges',list_edges)
    #print(list_edges,random_vertex_cover)    
    G = nx.Graph() # Create an empty undirected graph
    v_list=[]
    for i in range(1,n+1):
        v_list.append(i)
    #print(G.nodes())
    G.add_nodes_from(v_list)
    G.add_edges_from(list_edges)
    colors=[]
    for vertex in G.nodes():
        colors.append('blue')     
    nx.draw(G, with_labels=True, node_color=colors, node_size=300,font_size=10)
    plt.plot([], [],'o', label='Vertex', color='blue')
    plt.legend(loc='upper left')
    plt.show()

    b=bipartite_graph(list_edges,n,s1,s2)
    return b

def index_solution(sat_list,dic,min_no_one,list_edges,n):#n=no of vertices
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
    print('All Possible Vertex Covers',vertex_cover) #list of all vertex covers
    random_vertex_cover =(random.choice(vertex_cover)) #Randomly choose first vertex cover
    vertex_cover.remove(random_vertex_cover) #remove vertex cover from vertex cover list
    random_vertex_cover1=sorted(random_vertex_cover)
    #print('remaining',vertex_cover)
    random_vertex_cover2 = sorted(random.choice(vertex_cover))#Randomly choose first vertex cover
    #print('Randomly choose 2 vertex cover of Graph',random_vertex_cover1,random_vertex_cover2)
    k=MVC_Visualisation(list_edges,n,random_vertex_cover1,random_vertex_cover2)
    return  k   

def optimal_sat_sol(list_edges,n,T): #n=no of vertices
    constraint=[]
    for i in (list_edges):
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
        return f'No solution for {min_no_one} no of True'
    else:       
        l=index_solution(sat_list,dic,min_no_one,list_edges,n)   
        return l 

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