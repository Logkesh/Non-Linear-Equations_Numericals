# Fixed Point Method
import math as m
t=0.00001
def q(x):
    x = m.e**(1.21 / x)              # Change the equation accordingly, here: "x * m.log(x) - 1.21 = 0"
    return x 
def qd(x):
    if(((1.21*(x**(-2))*q(x)) < 1)):
        return True      # Change the equation accordingly
    else: 
        return False
def b(x,i=1):
    if(qd(x)):
        v = q(x)
        print("x",i," = ",v)
        i+=1
        if(x-v < t and x-v > -t):
            print("Approximate Root: ",v)
            return
        return b(v,i)
    else: print("Invalid Differentiation...")
b(2)