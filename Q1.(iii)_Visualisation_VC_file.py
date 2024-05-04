from z3 import *
import random
import networkx as nx
import matplotlib.pyplot as plt
import os
#Visualising everything one by one from Directory
'''directory = "C:/Users/Desktop/CODE/OUTPUT/"
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        file=open(os.path.join(directory, filename), "r")
        vertex=[]
        edges_list=[]
        for line in file:
            try:
                vertex.append(int(line.strip()))
            except:
                edge = [int(x.strip()) for x in line.split(',')]
                edges_list.append(edge)

        #vertex_cover formed by using vertex here value is 1, take its index+1
        vertex_cover=[] 
        for i in range(len(vertex)):
            if vertex[i]==1:
                vertex_cover.append(i+1)
        #print(vertex_cover)        
        #print(edge_list)
        vertex_list=[] #Collecting all vertices
        for i in range(len(vertex)):
            vertex_list.append(i+1)
        G=nx.Graph() # Create an empty undirected graph    
        G.add_nodes_from(vertex_list)
        G.add_edges_from(edges_list)
        #print(vertex_list,edges_list)

        #vertex_from_edges=[] #to keep all edges node in a single list
        colors=[]
        for vertex in vertex_list:
            if vertex in vertex_cover:
                colors.append('red')
            else:
                colors.append('blue') 

        nx.draw(G, with_labels=True, node_color=colors, node_size=500)
        plt.plot([], [],'o', label='Vertex Cover', color='red')
        plt.legend(loc='upper left')
        plt.show()'''



#File wish to open
folder_name=input('which folder want to open:')
folder_path = os.path.join("C:\\Users\\Desktop\\CODE\\OUTPUT", folder_name)#going inside subfolder
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    file_name = input('Enter text file want to visualize: ')
    file_path = os.path.join(folder_path, f"{file_name}.txt")
    
    if os.path.exists(file_path) and os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            vertex=[]
            edges_list=[]
            for line in file:
                try:
                    vertex.append(int(line.strip()))
                except:
                        edge = [int(x.strip()) for x in line.split(',')]
                        edges_list.append(edge)                
            #print(vertex) 
            vertex_cover=[] 
            for i in range(len(vertex)):
                if vertex[i]==1:
                    vertex_cover.append(i+1) 

            #print('ver',vertex_cover)        
            #print(edge_list)
            vertex_list=[] #Collecting all vertices
            for i in range(len(vertex)):
                vertex_list.append(i+1) 

            G=nx.Graph() # Create an empty undirected graph    
            G.add_nodes_from(vertex_list)
            G.add_edges_from(edges_list) 

            colors=[]
            for v in vertex_list:
                if v in vertex_cover:
                    colors.append('red')
                else:
                    colors.append('blue') 

            nx.draw(G, with_labels=True, node_color=colors, node_size=500)
            plt.plot([], [],'o', label='Vertex Cover', color='red')
            plt.legend(loc='upper left')
            plt.show()    
    else:
        print(f"The text file '{file_name}.txt' does not exist")
else:
    print(f"The folder '{folder_name}' does not exist.")

