a1=int(input("ENTER THE NUMBER 1"))
a2=int(input("ENTER THE NUMBER 2"))
a3=int(input("ENTER THE NUMBER 3"))
a4=int(input("ENTER THE NUMBER 4"))

if(a1>a2  and  a1>a3 and a1>a4):
    print("greatest no is a1: ",a1)
elif(a2>a1  and  a2>a3 and a2>a4):
    print("greatest no is a2: ",a2)
elif(a3>a1  and  a2<a3 and a3>a4):
    print("greatest no is a3: ",a3)
else:
    print("greatest no is a4: ",a4)
