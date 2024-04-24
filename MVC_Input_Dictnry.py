from z3 import *

# Define the graph as an adjacency list
graph = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2, 4],
    4: [2, 3]   
    }

# Create Z3 boolean variables for each vertex
vertex_binry = {v: Bool('x_%s' % v) for v in graph.keys()}
#print(vertex_binry)

constraint_1 = [] # For each edge at least one of its vertices is in the cover
for u, neighbors in graph.items():
    for v in neighbors:
        constraint_1.append(Or(vertex_binry[u], vertex_binry[v]))
print(constraint_1)

# Minimize the sum of vertices in the cover
#constraint_2 = Sum([If(vertex_binry[v], 1, 0) for v in graph.keys()])
#print(constraint_2)
# Create a Z3 solver instance
solver=Solver()
#solver = Optimize()

# Add the constraints_1 to the solver
solver.add(constraint_1)

# Add the constraint_2 function to the solver
#solver.minimize(constraint_2)
solver.check() #Check the hich is true or false
#print(solver.model())

# Check if the problem is satisfiable, hen input constraints are satisfiable

if solver.check() == sat:
    # Get the model (solution)
    model = solver.model() #Save our model ith variable
    demo=[]
    for i in model:
        #print(i)
        if model[i]==True:
            demo.append(i)
    print(demo)

    for i,j in vertex_binry.items():
        print(j)
        if j in demo:
            print(j)
            print(i)

    # Extract the vertices in the cover
    '''min_vertex_cover = [v for v in graph.keys() if is_true(model.eval(vertex_binry[v]))]

    # Print the minimum vertex cover
    print("Minimum Vertex Cover:", min_vertex_cover)
else:
    print("No Minimum Vertex Cover")'''
