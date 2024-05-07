from z3 import *
from pathlib import Path
import random
import networkx as nx
import matplotlib.pyplot as plt
import pickle
import os


def Vetex_Cover_Use_File(G1,G2,folder_path,file_name1,file_name2):
    '''G1=open("G1.txt", "r")
    G2=open("G1.txt", "r")
    vertex=[]
    edges_list=[]
    for line in G1:
        try:
            vertex.append(int(line.strip()))'''
    s1=[]
    Graph_edges_list=[]        
    if os.path.exists(G1) and os.path.isfile(G1):
        with open(G1, 'r') as file:          
            
            for line in file:
                try:
                    s1.append(int(line.strip()))
                except:
                        edge = [int(x.strip()) for x in line.split(',')]
                        Graph_edges_list.append(edge)
            #print(vertex) 

    s2=[]       
    if os.path.exists(G2) and os.path.isfile(G2):
        with open(G2, 'r') as file:                      
            for line in file:
                try:
                    s2.append(int(line.strip()))
                except:
                        break    
    #print(s1,s2) 
    s1_vertex_cover=[] 
    for i in range(len(s1)):
        if s1[i]==1:
            s1_vertex_cover.append(i+1)

    s2_vertex_cover=[] 
    for i in range(len(s2)):
        if s2[i]==1:
            s2_vertex_cover.append(i+1)  
    #print(s1_vertex_cover,s2_vertex_cover) 
    #print(Graph_edges_list)   
    m=MVC_Visualisation(Graph_edges_list,s1_vertex_cover,s2_vertex_cover,file_name1,file_name2) 
    return m

def MVC_Visualisation(list_edges,s1,s2,file_name1,file_name2):#n=no of vertices
    #print('edges',list_edges)
    #print(list_edges,random_vertex_cover)    
    G = nx.Graph() # Create an empty undirected graph
    G.add_edges_from(list_edges)
    colors=[]
    for vertex in G.nodes():
        colors.append('blue')     
    nx.draw(G, with_labels=True, node_color=colors, node_size=300,font_size=10)
    #plt.title(f'{file_name} Graph')
    plt.plot([], [],'o', label='Vertex', color='blue')
    
    plt.legend(loc='upper left')
    plt.show()

    Attack_E=input('Enter Attack edge with space:').split(' ') #Enter edge to attack
    Attack_Edge=[]
    for i in Attack_E:
        Attack_Edge.append(int(i))
    #print((Attack_Edge))
    b=bipartite_graph(list_edges,s1,s2,sorted(Attack_Edge),file_name1,file_name2)
    return b

def bipartite_graph(list_edges,s1,s2,Attack_Edge,file_name1,file_name2): #n=no of vertices,s1,s2=2 random vertex cover.
    #print(list_edges)
    #print('s1 and  s2',s1,s2)
    undirected_edge_list=[] #collecting all undirected edges and with self loops 
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
    #print('undirected edges',undirected_edge_list)  
    edges_cmbntn_s1s2=[] #combine all vertices betn s1 and s2
    for node1 in s1:
        for node2 in s2:
            edges_cmbntn_s1s2.append([node1,node2])
            #edges_cmbntn_s1s2.append([node2,node1])
    #print('all edges',edges_cmbntn_s1s2)
        bipartite_edges=[] #Bipartite edges in the form of x_i,x_j
    for edge in  edges_cmbntn_s1s2:
        if edge in  undirected_edge_list:
            bipartite_edges.append([edge[0],edge[1]])         
    k=bipartite_visualisation(bipartite_edges,s1,s2,Attack_Edge,undirected_edge_list,edges_cmbntn_s1s2,list_edges,file_name1,file_name2)
    return k


def bipartite_visualisation(bipartite_edges,s1,s2,Attack_Edge,undirected_edge_list,edges_cmbntn_s1s2,list_edges,file_name1,file_name2):
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

    '''Bipartite graph'''

    bipartite_edges=[]
    for edge in  edges_cmbntn_s1s2:
        if edge in  undirected_edge_list:
            #for node in range(len(edge)):
            bipartite_edges.append((f'x{edge[0]}',f'y{edge[1]}'))
    #print(bipartite_edges)
    partition11=[]
    partition22=[]
    for i in bipartite_edges:
        if i[0] not in partition11:
            partition11.append(i[0])
        if i[1] not in partition22:    
            partition22.append(i[1])
    B = nx.Graph()
    B.add_nodes_from(partition11,bipartite=0)
    B.add_nodes_from(partition22,bipartite=1)
    B.add_edges_from(bipartite_edges)
    pos = nx.bipartite_layout(B, partition11)
    nx.draw(B, pos, with_labels=True, node_color=['b']*len(partition11) + ['r']*len(partition22), node_size=500)
    plt.title('Bipartite Graph')
    plt.show()
    #print('Randomly choose 2 vertex cover of Graph')
    #return s1,s2
    m=Maximum_Matching_Edges(bipartite_edges,Attack_Edge,partition1,partition2,s1,s2,list_edges,edges_cmbntn_s1s2,file_name1,file_name2)
    return m

def Maximum_Matching_Edges(B_edge,Attack_Ed,partition1,partition2,s1,s2,list_edges,edges_cmbntn_s1s2,file_name1,file_name2): #B_edge:All Bipartite edges
    #print('Bipartite edges',B_edge)
    #print('Attack',Attack_Ed)
    Remng_B_edge=[] #Removing attack edge from bipartite, then remaing edge 
    B_edge_index=[]
    for k in B_edge:
        t1=[]
        t1.append(int(k[0][1:]))
        t1.append(int(k[1][1:]))
        B_edge_index.append(t1)
    index_v1=1
    Attack_Edge=[]
    '''Handle attacking edge in Bipartite graph'''
    for edge in B_edge_index:
        if Attack_Ed==sorted(edge):
            index_v1=edge.index(Attack_Ed[0])
            if index_v1==0:
                Attack_Edge.append((f'x{Attack_Ed[0]}',f'y{Attack_Ed[1]}'))
            if index_v1==1: 
                Attack_Edge.append((f'x{Attack_Ed[1]}',f'y{Attack_Ed[0]}'))       
    #print(edge[0],Attack_Edge[0])
    #print(edge[1],Attack_Edge[0])
    for edge in B_edge:
        if edge[0] in Attack_Edge[0] or edge[1] in Attack_Edge[0]:
            continue
        else:
            Remng_B_edge.append(edge)

    #print('Matching after attack',Remng_B_edge)                  
    v=Visualise_Max_Match(Remng_B_edge,Attack_Edge,partition1,partition2,B_edge,s1,s2,list_edges,edges_cmbntn_s1s2,file_name1,file_name2)    
    return v

def Visualise_Max_Match(Remng_B_edge,Attack_edge,partition1,partition2,B_edge,s1,s2,list_edges,edges_cmbntn_s1s2,file_name1,file_name2): #B_edge:Bipartite edges
    #print(Remng_B_edge)
    bipartite_edges=sorted(Remng_B_edge) #after attacking the edge, remaing bipartite graph 
    '''Bipartite graph after removing attack edge'''
    #print('remng sorted b edges',Remng_B_edge)
    remn=[]
    for edge in Remng_B_edge:
        remn.append((f'{edge[0]}',f'{edge[1]}'))
    #print('remn',remn)    
    partition11=[]
    partition22=[]
    for i in remn:
        if i[0] not in partition11:
            partition11.append(i[0])
        if i[1] not in partition22:    
            partition22.append(i[1]) 
    #print(partition11)
    #print(partition22)        
    B = nx.Graph()
    B.add_nodes_from(partition11,bipartite=0)
    B.add_nodes_from(partition22,bipartite=1)
    B.add_edges_from(remn)
    pos = nx.bipartite_layout(B, partition11)
    nx.draw(B, pos, with_labels=True, node_color=['b']*len(partition11) + ['r']*len(partition22), node_size=500)
    plt.show()

    max_matching = nx.maximal_matching(B) #find max matching of the remaining graph, this is in set form   
    #print('matching',max_matching)
    #l1=[]
    #l1.append((f'x{Attack_edge[0]}',f'y{Attack_edge[1]}'))#convert Attack edge node to X_i,Y_i form
    max_matching.add(Attack_edge[0])   
    #print('After adding attack edge',max_matching) 
    max_match=[]
    for i in max_matching:
        max_match.append(i)
    partition3=[]
    partition4=[]
    for i in max_matching:
        if i[0] not in partition3:
            partition3.append(i[0])
        if i[1] not in partition4:    
            partition4.append(i[1]) 
    #print(partition3)
    #print(partition4)
    B_M = nx.Graph()
    B_M.add_nodes_from(partition3,bipartite=0)
    B_M.add_nodes_from(partition4,bipartite=1)
    B_M.add_edges_from(max_match)
    pos = nx.bipartite_layout(B_M, partition3)
    nx.draw(B_M, pos, with_labels=True, node_color=['b']*len(partition3) + ['r']*len(partition4), node_size=500)
    plt.show()
    fb=final_Bipartite(B_edge,Attack_edge,max_match,s1,s2,list_edges,edges_cmbntn_s1s2,file_name1,file_name2) 
    return fb  

def final_Bipartite(B_edge,Attack_edge,max_match,s1,s2,list_edges,edges_cmbntn_s1s2,file_name1,file_name2):
    bipartite_E=[]
    for edge in B_edge:
        bipartite_E.append((f'{edge[0]}',f'{edge[1]}'))
    #print('1',bipartite_E) 
    #print('11',Attack_Edge)   
    Attack_E=[(Attack_edge[0][0],Attack_edge[0][1])]
    #print('2',Attack_E)  
    #print('3',max_match)

    G = nx.Graph()
    partition1=[]
    partition2=[]
    for edge in bipartite_E:
        partition1.append(edge[0])
        partition2.append(edge[1])
    G.add_nodes_from(partition1, bipartite=0)
    G.add_nodes_from(partition2, bipartite=1)    

    G.add_edges_from(bipartite_E)
    color=[]
    for edge in G.edges():
        if edge in max_match:
            if edge in Attack_E:
                color.append('Red')
            else:
                color.append('y')
        else:
            color.append('Black')
    pos = nx.bipartite_layout(G,partition1)
    nx.draw(G, pos, with_labels=True, edge_color=color)
    #nx.draw(G, with_labels=True, node_color=colors, node_size=500)
    plt.plot([], [],'o', label='Attacking edge', color='red')
    plt.plot([], [],'o', label='Matching edge', color='y')
    plt.plot([], [],'o', label='Graph edge', color='Black')
    plt.legend(loc='lower center')
    plt.show()
    f=final_Output(B_edge,Attack_edge,max_match,s1,s2,list_edges,edges_cmbntn_s1s2,file_name1,file_name2)
    return f

def final_Output(B_edge,Attack_Edgee,max_match,s1,s2,list_edges,edges_cmbntn_s1s2,file_name1,file_name2):
    #print(s1,'and',s2)
    #print('edges',list_edges)
    #print('attack',Attack_Edge) 
    #print('matching',max_match)
    '''max_match in the form of(x_i,y_j), so convert it into integer format'''
    Max_M=[]
    for edge in max_match:
        l=[]
        for i in edge:
            l.append(int(i[1:]))
        Max_M.append(l)    
    #print('max',Max_M)

    nodes=[]
    for edge in list_edges:
        for i in edge:
            if i not in nodes:
                nodes.append(i)
            else:
                pass
    #print('nodes',nodes) 
    Attack_Edge=[]
    for edge in Attack_Edgee:
        Attack_Edge.append(int(edge[0][1:]))
        Attack_Edge.append(int(edge[1][1:]))
    #print('Att',Attack_Edge)   
          
    if Attack_Edge not in edges_cmbntn_s1s2:
        G1 = nx.Graph() #created empty graph for s1
        G1.add_edges_from(list_edges)
        colors_s1=[]
        for vertex in G1.nodes():
            if vertex in s1:
                colors_s1.append('red')
            else:
                colors_s1.append('blue') 
        fig, axes = plt.subplots(1, 2, figsize=(15, 5)) 
        #nx.draw(G1, with_labels=True, node_color='skyblue', font_color='black')
        nx.draw(G1, with_labels=True, node_color=colors_s1, node_size=300,ax=axes[0])
        plt.plot([], [],'o', label='Vertex Cover', color='red') 
        axes[0].set_title('First Vertex Cover in Graph')

        G2 = nx.Graph() #created empty graph for s1
        G2.add_edges_from(list_edges)
        colors_s2=[]
        for vertex in G2.nodes():
            if vertex in s2:
                colors_s2.append('red')
            else:
                colors_s2.append('blue') 
        #nx.draw(G1, with_labels=True, node_color='skyblue', font_color='black')
        nx.draw(G2, with_labels=True, node_color=colors_s2, node_size=300,ax=axes[1])
        plt.plot([], [],'o', label='Vertex Cover', color='red') 
        axes[1].set_title('Second Vertex Cover in Graph')  

        plt.tight_layout()

        # Displaying the graphs
        plt.show()
        return f'This Attack Edge {Attack_Edge} can not be defeated. '
        #possible for the {file_name1},{file_name2} text files.

    else:
        '''creat first vertex cover in graph'''
        G1 = nx.Graph() #created empty graph for s1
        G1.add_edges_from(list_edges) #Graph for first vertex cover set
        colors_s1=[]
        for vertex in G1.nodes():
            if vertex in s1:
                colors_s1.append('red')
            else:
                colors_s1.append('blue') 
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))        
        #plt.subplot(1, 2, 1)  # 1 row, 2 columns, position 1
        #nx.draw(G1, with_labels=True, node_color='skyblue', font_color='black')
        nx.draw(G1, with_labels=True, node_color=colors_s1, node_size=200,ax=axes[0])
        axes[0].set_title('First Vertex Cover in Graph')
        #plt.plot([], [],'o', label='Vertex Cover', color='red') 

        #plt.show()
        '''Create a directed graph depend on the direction of matching'''
        G = nx.DiGraph()
        # Add nodes
        G.add_nodes_from(nodes)
        # Add undirected edges
        for edge in list_edges:
            if edge in Max_M:
                G.add_edge(edge[0], edge[1], direction='forward')
            else:
                G.add_edge(edge[0],edge[1])
    
        # Draw the graph
        pos = nx.spring_layout(G)  # positions for all nodes
        nx.draw_networkx_nodes(G, pos, node_size=200,ax=axes[1])
        nx.draw_networkx_edges(G, pos, edgelist=list_edges, width=1, edge_color='b', arrows=False,ax=axes[1])
        nx.draw_networkx_edges(G, pos, edgelist=Max_M, width=1, edge_color='r', arrows=True, arrowstyle='-|>', arrowsize=10,ax=axes[1])
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='Arial',ax=axes[1])
        axes[1].set_title('Transition Graph')
        plt.axis('off')
        #plt.show()

        '''creat second vertex cover in graph'''
        G2 = nx.Graph() #created empty graph for s1
        G2.add_edges_from(list_edges) #Graph for 2nd vertex cover set
        colors_s2=[]
        for vertex in G2.nodes():
            if vertex in s2:
                colors_s2.append('red')
            else:
                colors_s2.append('blue') 
               
        #plt.subplot(1, 2, 3)  # 1 row, 2 columns, position 1
        #nx.draw(G1, with_labels=True, node_color='skyblue', font_color='black')
        nx.draw(G2, with_labels=True, node_color=colors_s2, node_size=200,ax=axes[2])
        axes[2].set_title('Second Vertex Cover in Graph')
        #plt.plot([], [],'o', label='Vertex Cover', color='red')   

        plt.tight_layout()

        # Displaying the graphs
        plt.show()



folder_name=input('Enter Folder name to Open Text file:')
folder_path = os.path.join("C:\\Users\\Desktop\\CODE\\OUTPUT", folder_name)#going inside subfolder


if os.path.exists(folder_path) and os.path.isdir(folder_path):
    file_name1 = input('Enter first text file Name: ')
    G1 = os.path.join(folder_path, f"{file_name1}.txt") #1st text file
    file_name2 = input('Enter Second text file Name:')
    G2 = os.path.join(folder_path, f"{file_name2}.txt") #2nd Text file
    Vetex_Cover_Use_File(G1,G2,folder_path,file_name1,file_name2)      



    