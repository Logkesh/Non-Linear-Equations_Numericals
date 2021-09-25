# Newton Method
import math as m
t=0.00001      
def q(x):
    return x * m.log(x) - 1.21   # Change the equation accordingly
def qd(x):
    return 1
def a(x):
    return x - (q(x)/qd(x))
def b(x,i=1):
    v=q(a(x))
    if v==0:
        print("Apporoximate Root: ",a(x))
        return a(x)
    if(q(a(x)) > -t and q(a(x)) < t):
        print("Apporoximate Root: ",a(x))
        return a(x)
    else:
        print("x",i," = ",a(x))
        i+=1
        b(a(x),i)
b(2)