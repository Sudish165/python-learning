from abc import ABC, abstractmethod

class IIC(ABC):
    @abstractmethod
    def pay(self):
        pass

class Student(IIC):
    def pay(self):
        print("Paid from student account")
        
    def displayinfo():
        IIC.pay()

obj = Student()
print(obj.pay())  # ✅ Output: Paid from student account
