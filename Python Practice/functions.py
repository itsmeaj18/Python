# def goodday():
#     print("good day")

# goodday()    

# 1st
# def greatest(a,b,c):
#     if(a>b)and(a>c):
#         print(f"{a} is greatest ")
#     elif(b>a)and(b>c):
#         print(f"{b} is greatest ")
#     else:        
#         print(f"{c} is greatest ")    

# greatest(4,1,5)        

# 2nd
# def convertftoc(f):
#     return 5*(f-32)/9
# f = int(input("enter the temp"))
# print(f"{round(convertftoc(f))} is the temp in celcius")

# 3rd
# def sum(x):
#     if(x==1):
#         return 1
#     return x+sum(x-1)
# print(sum(9))

# 4th
def pattern(n):
    if (n==0):
        return
    print("*"*n)
    pattern(n-1)

pattern(5)    