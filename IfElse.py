# a = int(input("Enter your age: "))
# if a > 18:
#     print("You are an adult")
# else:
#  print("You are a minor")
# print("Good Boy")



# Chocolate = "200"
# You = int (input("Enter your money: "))
# if (You >= int(Chocolate) ):
#    print("You can buy the chocolate")
# else:
#     print("You can't buy the chocolate")



# num = int(input("Enter the number: "))
# if num<0:
#     print("Number is negative")
# elif num == 0:
#     print("Number is zero")
# else:
#     print("Number is positive")


# import time
# timestamp = time.strftime('%H:%M:%D')
# print(timestamp)


# a = int(input("Enter number: "))

# if a == 0:
#     print(f"{a} is Zero")
# elif a %2== 0:
#     print(f"{a} is even number")
# else:
#     print(f"{a} is odd number")


a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a > b and c:
    print(f"{a} is greater than {b} and {c}")
elif b > a and b > c:                  
    print(f"{b} is greater than {a} and {c}")  
else:
    print(f"{c} is greater than {a} and {b}")