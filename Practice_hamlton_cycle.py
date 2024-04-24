from z3 import *

def hamiltonian_cycle_exists(graph):
    num_vertices = len(graph)

    # Create Z3 variables
    v = [[Bool(f"v_{i}_{j}") for j in range(num_vertices)] for i in range(num_vertices)]

    # Constraints: Each vertex appears exactly once in the cycle
    vertex_appearance = [Or([v[i][j] for j in range(num_vertices)]) for i in range(num_vertices)]
    # Constraints: Each position in the cycle is occupied
    position_occupied = [Or([v[i][j] for i in range(num_vertices)]) for j in range(num_vertices)]
    # Constraints: No two vertices can appear at the same position
    no_same_position = [Not(And(v[i][j], v[k][j])) for i in range(num_vertices) for k in range(num_vertices) if i != k for j in range(num_vertices)]
    # Constraints: Edges in the graph must be respected
    edge_constraints = [Or([And(v[i][j], v[k][(j+1)%num_vertices]) for i in range(num_vertices) for k in graph[i]]) for j in range(num_vertices)]

    # Create Z3 solver
    solver = Solver()

    # Add constraints to the solver
    solver.add(vertex_appearance)
    solver.add(position_occupied)
    solver.add(no_same_position)
    solver.add(edge_constraints)

    # Check satisfiability
    if solver.check() == sat:
        return True  # Hamiltonian cycle exists
    else:
        return False  # Hamiltonian cycle does not exist

# Example graph represented as an adjacency list
example_graph = {
    0: [1],
    1: [0, 2],
    2: [1]
}

# Check if a Hamiltonian cycle exists in the example graph
print("Does a Hamiltonian cycle exist in the example graph?", hamiltonian_cycle_exists(example_graph))
