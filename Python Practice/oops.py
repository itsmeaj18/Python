# 1st
# class programmer:
#     company="microsoft"
#     def __init__(self,name,salary,pin):
#         self.name=name
#         self.salary=salary
#         self.pin=pin

# p=programmer("harry",12000,131466)
# print(p.name,p.salary,p.company)

# 2nd
class Calculator:
    def __init__(self, z):
        self.z = z

    def sqre(self):
        square = self.z * self.z
        return square

    def cube(self):
        cube = self.z * self.z * self.z
        return cube

    def sqrt(self):
        squroot = self.z ** 0.5
        return squroot

a = Calculator(5)
print(a.cube())  # Calls the cube method
print(a.sqre())  # Calls the sqre method
print(a.sqrt())  # Calls the sqrt method