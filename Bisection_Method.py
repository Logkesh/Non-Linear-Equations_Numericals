#bisection method
import math as m
t=0.0001      
def q(x):
    return x * m.log(x) - 1.21  # Change the equation accordingly
def a(a,b):
    return((a+b)/2)
def b(x,y,i=2):
    
    v=q(a(x,y))
    if v==0:
        print("Apporoximate Root: ",a(x,y))
        return a(x,y)
    if (v>0 and v<t)or(v>-t and v<0) or a(x,y)==x:
        print("Apporoximate Root: ",x)
        return x
    if(v*q(x)<0):
        print(i,"Intreval : (",x,",",a(x,y),")")
        i+=1
        b(x,a(x,y),i)
    elif(v*q(y)<0):
        print(i,"Intreval : (",a(x,y),",",y,")")
        i+=1
        b(a(x,y),y,i)
b(1,2)