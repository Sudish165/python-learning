#construction in python

class ConstructorDemo:
    def _init_(self):
        print("This is a constructor in python")
        
class AddNumbers:
    def _init_(self, a, b):
        self.a = a
        self.b = b
        
    def sum(Self):
        return Self.a + Self.b
    
    def _call_(self, a, b):
        return a +b
        
    
    
obj = ConstructorDemo()
obj1 = AddNumbers(5, 7)
print(obj1.sum())

print(obj1(20,30))