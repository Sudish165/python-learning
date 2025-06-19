class A:
    def displayName():
        print("My name is Sudish Karki")
        
    def displayAge():
        print("My age is 21")
        
class B(A):
    def displayName():
        print("My name is Sudish Karki and I am from Nepal")
        
class C(B):
    def displayName():
        print("My name is Sudish Karki and I am from Nepal and I am a Student")
        
        
    def sum(no1, no2=0, no3=0):
        return no1 + no2 + no3
    
    #Using Args
    def add(*args):
        sum=0
        for num in args:
             sum = sum + num
        return sum
        
# obj = A
# obj.displayName()

# obj1 = B
# obj1.displayName()

obj2 = C
# obj2.displayName()
# obj2.displayAge()

result = obj2.sum(10, 15, 20)
print(result)

#USing args
result2 = obj2.add(10, 15, 20 ,25, 30)
print = ("The sum is", result2)
