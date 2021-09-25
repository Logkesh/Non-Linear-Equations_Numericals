# Secant Method
import math as m
t=0.00001      
def q(x):
    return x * m.log(x) - 1.21  # Change the equation accordingly
def qd(x,y):
    return ((q(x)-q(y))/(x-y))
def a(x,y):
    return y - (q(y)/qd(x,y))
def b(x,y,i=1):
    v=q(a(x,y))
    if((v > -t and v < t) or v==0):
        print("Apporoximate Root: ",a(x,y))
        return a(x,y)
    else:
        print("x",i," = ",a(x,y))
        i+=1
        b(y,a(x,y),i)
b(2,2.7)