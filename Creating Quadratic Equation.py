a = int(input("Enter the 2 roots to create the quadratic equation:\nRoot 1:"))
b = int(input("Root 2:"))
sor = a+b
por = a*b
print("The Quadratic equation for the given roots is :")
if(sor<=0 and por>=0):
      print("x2+"+str(-sor)+"x+"+str(por))
elif(sor>0 and por>=0):
      print("x2"+str(-sor)+"x+"+str(por))
elif(sor<=0 and por<0):
      print("x2+"+str(-sor)+"x"+str(por))
elif(sor>0 and por<0):
      print("x2"+str(-sor)+"x"+str(por))
      