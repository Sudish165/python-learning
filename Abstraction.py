from abc import ABC, abstractmethod

# Abstract base class
class IIC(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete class: Student
class Student(IIC):
    def pay(self, amount):
        print(f"Paid {amount} from student account")

# Concrete class: Teacher
class Teacher(IIC):
    def pay(self, amount):
        print(f"Paid {amount} from teacher account")

# Function to process payment
def Member(member: IIC, amount):
    member.pay(amount)

# Main logic
college_location = input("College Location: ")
amount = float(input("College fee per month: "))

# Simulate a payment (choose student or teacher)
user_type = input("Are you a student or teacher? ").lower()

if user_type == "student":
    member = Student()
elif user_type == "teacher":
    member = Teacher()
else:
    print("Invalid user type.")
    exit()

# Call payment
Member(member, amount)
