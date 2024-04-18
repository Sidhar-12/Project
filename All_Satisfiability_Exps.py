from z3 import *

#Q.0 Operation is not satisfiability
'''p=Bool('p')
s=Solver()
s.add(And(p,Not(p)))
print(s.check())
if s.check()==sat:
    print(s.model())'''

#Q.1 'Or' operation is satisfiabiality
'''P,Q=Bools('p q')
F = Or(P, Q)

solve(F)
print('\n')

F = And(F, Not(And(P, Not(Q))))
solve(F)
print('\n')

F = And(F, Not(And(Not(P), Q)))
solve(F)

F = And(F, Not(And((P), Q)))
solve(F)'''



#Q.2 'And' operation is satisfiabiality
'''p,q=Bools('p q')
s=Solver()
s.add(And(p,q))
s.check()
if s.check()==sat:
    print(s.model())'''   
#Q.3 'XoR' operation is satisfiabiality
'''p,q=Bools('p q')
s=Solver()
s.add((p^q))
s.check()
if s.check()==sat:
    print(s.model())'''
#Q.4 'Conditional' operation is satisfiability 
'''p,q=Bools('p q')
s=Solver()
s.add(Implies(p,q))
#s.add(Implies(Not(q),Not(p)))
s.check()
if s.check()==sat:
    print(s.model())''' 
#Q.5,6 Operation is satisfiability 
'''p,q=Bools('p q')
s=Solver()
s.add(Implies(p,q))
print(s.check())
s.add(Implies(q,p))
s.check()
if s.check()==sat:
    print(s.model())''' 
#Q.7 Operation is satisfiability 
'''p,q=Bools('p q')
p1=Or(p,Not(q))
q1=And(p,q)
s=Solver()
s.add(Implies(p1,q1))
#s.add(Implies(Or(p,Not(q)),And(p,q)))
s.check()
if s.check()==sat:
    print(s.model())'''  
#Q.8 Operation is Satisfiability
'''p,q=Bools('p q')
p1=Or(p,Not(q))
q1=And(p,q)
s=Solver()
s.add(Or(Not(q),(And(Not(p),q))))
s.check()
if s.check()==sat:
    print(s.model())''' 
#Q.9 Operation is Satisfiability  
'''p,q,r=Bools('p q r')
p1=And(p,q)
q1=And(Not(q),r)
s=Solver()
s.add(Or(p1,q1))
#s.add(And(p1,q1)) #Not Satisfiability
s.check()
if s.check()==sat:
    print(s.model())'''          
#Q.10 Operation is Satisfiability 
'''p,q,r=Bools('p q r')
p1=Implies(p,Not(r))
q1=Implies(q,Not(r))
s=Solver()
s.add(Or(p1,q1))
s.check()
if s.check()==sat:
    print(s.model())'''
#Q.11 Operation is Satisfiability
'''q,r=Bools('q r')
q1=Implies(Not(q),r)
r1=Implies(r,Not(q))
s=Solver()
s.add(And(q1,r1))
print(s.check())
if s.check()==sat:
    print(s.model())''' 
#Q.12 Operation is Satisfiability 
'''p,s,t=Bools('p s t')
p1=Or(p,Not(t))
s1=Or(p,Not(s))
s=Solver()
s.add(And(p1,s1))
print(s.check())
if s.check()==sat:
    print(s.model())''' 
#Q.14 Operation is satisfiability
'''p,q,r,s,t=Bools('p q r s t')  
p1=And(p,r,s)
p2=And(q,t)
p3=And(r,Not(t))
s=Solver()
#s.add(Or((Or(p1,q1)),r1)) 
s.add(Or(p1,p2,p3))    
#print(s.check())  
if s.check()==sat:
    print(s.model())'''     
#Q.15 Operation is Satisfiability  
'''p,q=Bools('p q')
p1=(p^q)

s1=(p^Not(q))
solve(And(p,Not(p)))
s=Solver()
#s.add(p1) #get [T F]
#s.add(s1) #get [F F]
s.add(Not(Or(p1,s1)))
print(s.check())
if s.check()==sat:
    print(s.model())'''
#Q.16 Operation is Satisfiability 
'''p,q=Bools('p q')
p1=Implies(p,q)
p2=Implies(q,p)
q1=Implies(Not(p),q)
q2=Implies(q,Not(p))

F=Or( (And(p1,p2)),(And(q1,q2)))
solve(F)

F=And(F, Not(And(Not(p),Not(q))))
solve(F)

F=And(F,Not(And(Not(p),(q))))
solve(F)

F=And(F,Not(And(p,Not(q))))
solve(F)
#if s.check()==sat:
    #print(s.model())'''
#Q.17 Operation is Satisfiability 
'''p,q=Bools('p q')
p1=Implies(Not(p),Not(q))
p2=Implies(Not(q),Not(p))
LHS=And(p1,p2)
q1=Implies(p,q)
q2=Implies(q,p)
RHS=And(q1,q2)
forard_eqn=Implies(LHS,RHS)
backard_eqn=Implies(RHS,LHS)
final_eqn=And(forard_eqn,backard_eqn)
s=Solver()
#s.add(LHS) #get[0 0]
#s.add(RHS)   #get[0 0]
#s.add(And(forard_eqn,backard_eqn)) #get empty
s.add(And(final1,final2) )
if s.check()==sat:
    print(s.model())   #Getting no output'''

#Q.18 Operation is satisfiability
'''p,q,r,s=Bools('p q r s') 
x=And(p,q,r)
y=And(x,s)
s=Solver()
s.add(y)  
if s.check()==sat:
    print(s.model())'''
#Q.19,20 x_1 or x_2 or....or x_n is satisfiability and for operation "And"
'''x_1=Bool('x_1')
n=int(input('Enter number:'))
for i in range(2,n+1):
    var1=f'x_{i}'
    bool_var1=Bool(var1) 
    x_1=And(x_1,bool_var1)
s=Solver()
s.add(x_1)
if s.check()==sat:
    print(s.model())'''




#Q.21,22 is satisfiability
'''constraint=[]
n=int(input("Enter Number: "))
for i in range(1,n+1,2):
    var1=f'x_{i}'
    var2=f'x_{i+1}'
    bool_var1=Bool(var1) 
    bool_var2=Bool(var2)
    constraint.append((And(bool_var1,bool_var2)))
    #constraint.append(And(bool_var1,bool_var2))
constraint_0=Or(constraint) 
print((constraint_0))   
#print(Or(constraint)) 
s=Solver()
s.add((constraint_0))
if s.check()==sat:
    solution=s.model()
    print(solution)

    size=2**n
    for j in range(size):
        print(j)
        rec_cons=[]
        for i in solution:
            #print(i)
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
            print(solution)
        else:
            break
    
print('\n') 
print('\n')'''    
    
    

#Q.23 operstion is satisfiability
'''constrain=[]
n=int(input('Enter number:'))
for i in range(1,n+1,3):
    var1=f'x_{i}'
    var2=f'x_{i+1}'
    var3=f'x_{i+2}'
    #print(var1,var2,var3)
    bool_var1=Bool(var1)
    bool_var2=Bool(var2)
    bool_var3=Bool(var3)
    res1=Or(bool_var1,bool_var2)
    res2=Or(bool_var1,bool_var3)
    constrain.append(And(res1,res2))
#print(constrain) 
s=Solver()
s.add(constrain)
if s.check()==sat:
    print(s.model())'''
#Q.24 operstion is satisfiability
'''constrain=[]
n=int(input('Enter number:'))
for i in range(1,n+1,3):
    var1=f'x_{i}'
    var2=f'x_{i+1}'
    var3=f'x_{i+2}'
    #print(var1,var2,var3)
    bool_var1=Bool(var1)
    bool_var2=Bool(var2)
    bool_var3=Bool(var3)
    res1=And(bool_var1,bool_var2)
    res2=And(bool_var1,bool_var3)
    constrain.append(Or(res1,res2))
print(constrain) 
s=Solver()
s.add(constrain)
if s.check()==sat:
    print(s.model())'''
#Q.25 operation is satisfiability
'''x1=Not(Bool(' x_1'))
n=int(input('Enter number:'))
for i in range(2,n+1):
    var=f'x_{i}'
    bool_var=Bool(var) 
    x1=And(x1,Not(bool_var))
s=Solver()
s.add(x1)
if s.check()==sat:
    k=s.model()
    print(s.model()) 
    for i in k:
        if k[i]==False:
            print(str(i).split('_')[1])'''   
#Q.26 (ϕ) Satisfiability => Not(ϕ) satisfiability
'''p,q=Bools('p q')
s=Solver()
s.add(Or(p,q))   #satisfiability
#s.add(And(Not(p),Not(q))) #satisfiability
if s.check()==sat:
    print(s.model())''' 
#Q.26 (ϕ) Satisfiability <=> Not(ϕ) not satisfiability 
'''p=Bool('p')
s=Solver()
s.add(Or(Not(p),p)) #satisfiability
#s.add(And(p,Not(p))) #Not satisfiability
print(s.check())
if s.check()==sat:
    print(s.model())'''
#Q.26 (ϕ) Not Satisfiability <=> Not(ϕ) Not satisfiability
'''p=Bool('p')
s=Solver()
s.add((Implies(And(p,Not(p)),Or(p,Not(p)))))
s.add((Implies(Or(p,Not(p)),And(p,Not(p)))))
print(s.check())
if s.check()==sat:
    print(s.model())'''                    

#exp
constraint=[]
x1,x2=Bools('x1 x2')
x3,x4=Bools('x3 x4')
data1=And(Or(x1,x2),Or(x1,x3),Or(x1,x4))
data2=And(Or(x2,x4),Or(x2,x3),Or(x3,x4))
constraint.append(And(data1,data2))
constraint_0=(And(constraint) )
#print(type(constraint_0))

s=Solver()
s.add(constraint_0)

if s.check()==sat:
    solution=s.model()
    #print(solution)

    size=2**4
    for j in range(size):
        rec_cons=[]
        for i in solution:
            if solution[i]==False:
                rec_cons.append((Not((Bool(str(i))))))
            if solution[i]==True:
                rec_cons.append(((Bool(str(i))))) 
        #print(rec_cons)        
        constraint_1=Not(And(rec_cons))
        #print(constraint_1) 
        constraint_0=And(constraint_0,constraint_1)
        s1=Solver()
        s1.add(constraint_0)
        if s1.check()==sat:
            solution=s1.model()
            #print(solution)
        else:
            break    

print('\n')



#exp
constraint=[]
x1,x2=Bools('x1 x2')
x3,x4=Bools('x3 x4')
data1=Or(And(x1,x2),And(x1,x3),And(x1,x4))
data2=Or(And(x2,x4),And(x2,x3),And(x3,x4))
constraint.append(Or(data1,data2))
constraint_0=Or(constraint) 
print((constraint)) 

s = Solver()
s.add(constraint_0)

if s.check() == sat:
    solution = s.model()
    #print(solution)

    size = 2 ** 4
    for j in range(size):
        rec_cons = []
        for i in solution:
            if solution[i] == False:
                rec_cons.append(Not(Bool(str(i))))
            if solution[i] == True:
                rec_cons.append(Bool(str(i)))
        constraint_1 = Not(And(rec_cons))
        constraint= And(Or(constraint), constraint_1)
        s.add(constraint)
        if s.check() == sat:
            solution = s.model()
            print(solution)
        else:
            break