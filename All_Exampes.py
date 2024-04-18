from z3 import *
'''x=Int('x')
y=Int('y')
s=Solver()
s.add(x+2*y==2)
s.add(x+y==3)
if s.check() ==sat:
    model1=s.model()
    print(model1)
    
    x1=model1.eval(x).as_long()
    y1=model1.eval(y).as_long()
    result=x1*y1
    print(result)'''

'''from z3 import *
Tie, Shirt = Bools('Tie Shirt')
s = Solver()
s.add(Or(Tie, Shirt), 
    Or(Not(Tie), Shirt), 
    Or(Not(Tie), Not(Shirt)))
(s.check())
    
if s.check()==sat:
    model=(s.model())
    print((model))
    for i in model:
        if model[i]==True:
            print(f"{i}")'''

'''for var in model:
        if model[var]:
            print(f"{var} is True")'''


'''from z3 import *
x, y = Ints('x y')
s = Solver()
s.add((x % 4) + 3 * (y / 2) > x - y)
print(s.check())
print(s.model())'''

'''class BlockTracked(None):
    def __init__(self, s):
        #UserPropagateBase.__init__(self, s)
        self.trail = []
        self.lim   = []
        self.add_fixed(lambda x, v : self._fixed(x, v))
        self.add_final(lambda : self._final())

    def push(self):
        self.lim += [len(self.trail)]

    def pop(self, n):
        self.trail = self.trail[0:self.lim[len(self.lim) - n]]
        self.lim = self.lim[0:len(self.lim)-n]

    def _fixed(self, x, v):
        self.trail += [(x, v)]

    def _final(self):
        print(self.trail)
        self.conflict([x for x, v in self.trail]) 
b = BlockTracked(4)
x, y, z, u = Bools('x y z u') 
b.add(x) 
b.add(y) 
b.add(z)
s.add(Or(x, Not(y)), Or(z, u), Or(Not(z), x))
print(s.check())'''

'''p,q,r=Bools('p q r')
s=Solver()
#Sequence of constraints matters
s.add( Or(Not(p),r))
s.add(r==Not(q))
s.add(Implies(p,q))
(s.check())
print(s.model())'''

'''p,q,r=Ints('p q r')
s=Solver()
s.add(p*p+q*q==r*r,p>0,q>0,r>0)
s.check()
m=s.model()
x1=m.eval(p)
#x1=m.eval(x).as_long()
print(x1.as_long()**2)
print(m[q].as_long()*4)'''


'''x = Int('x')
y = Int('y')
n = x + y >= 3
print("num args: ", n.num_args())
print("children: ", n.children())
print("1st child:", n.arg(0))
print("2nd child:", n.arg(1))
print("operator: ", n.decl())
print("op name:  ", n.decl().name())'''


