from z3 import *
graph = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2, 4],
    4: [2, 3]   
    }

constraint_1 = []

for i, j in graph.items():
    for k in j:
        var_1 = f'x_{i}'
        var_2 = f'x_{k}'
        bool_var_1 = Bool(var_1)
        bool_var_2 = Bool(var_2)
        constraint_1 .append(Or(bool_var_1, bool_var_2))

#print(constraint_1)
s=Solver()
s.add(constraint_1)
#print(s.check())

if s.check()==sat:
    model=s.model()
    #print(model
    for i in model:
        if model[i]==True:
            #num = (i.split('_')[1])
            num = (str(i).split('_')[1])
            print(num)        




   
