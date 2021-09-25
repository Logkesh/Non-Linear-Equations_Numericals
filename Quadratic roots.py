try: 
    eq = input("Enter the quadratic equation in the format of\nax2+bx+c :")
    if(eq.split('x2')[0]==''):a=1
    else:a = float(eq.split('x2')[0])

    if 'x' not in eq.split('x2')[1]:b=0
    elif((eq.split('x2')[1]).split('x')[0]=='+'):b=1
    elif((eq.split('x2')[1]).split('x')[0]=='-'):b=-1
    else:b=float((eq.split('x2')[1]).split('x')[0])

    if 'x' not in eq.split('x2')[1]:c=float((eq.split('x2')[1]).split('x')[0])
    elif((eq.split('x2')[1]).split('x')[1]==''):c=0
    else:c=float((eq.split('x2')[1]).split('x')[1])

    if(a!=0):
        x1 = (-b + (b**(2) - 4*a*c)**(0.5))/2*a
        x2 = (-b - (b**(2) - 4*a*c)**(0.5))/2*a
    print("Roots of the equation: {",x1,",",x2,"}")
except:print('Invalid Equation...')