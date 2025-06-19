#Class in python

class A:
    def displayName():
        print("Hello User!")
        
A.displayName()


#Inheritance in Python
class B(A):
    def displayClassB():
        print("Welcome to Python!")
        
class C(B):
    def displayClassC():
        print("Python is a great language!")
            

#Creating an instance of class A
obj = A
obj.displayName() #Output : Hellow user!
obj2 = B
obj2.displayClassB() #Output : Welcome to Python!
obj3 = C
obj3.displayClassC() #Output : Python is a great language!

