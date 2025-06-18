def calculatemake(a, b):
    make = (a*b)/(a+b)
    print(make)



def greater(a, b):
    if a > b:
     print("c is greater than d")
    else:
     print("d is greater than c")   



def isLesser(a, b):
   pass



a = 9
b = 8
# make1 = (a*b)/(a+b)
# print(make1)
calculatemake(a, b)
# if a>b:
#     print("a is greater than b")
# else:
#     print("b is greater than a")



c = 2
d = 3
# make2 = (c*d)/(c+d)
# print(make2)
calculatemake(c, d)
greater(c, d)






#functions in python
#always in camel case
def displayHelloWorld():
    print("Hello, World")
    
#function with no arg and return value
def add ():
    num1 = 10
    num2 = 20
    sum = num1 +num2
    return sum


#function with arg and no return value
def displayName(name):
    print("Hello, "+ name + "!w")
    
    
#function with arg and return value
def displayData(num1, num2):
    prod = num1 +num2
    return prod

displayHelloWorld() #calling the function
result = add() +10 #calling the function and storing the resukt in a variable
print(result) #printing the result

your_name = "Jhon"
displayName("your_name")

def fidplayData (num1, num2):
    prod = num1  * num2
    return prod
print(displayData(50,20))