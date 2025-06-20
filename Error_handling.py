# First block: divide by zero
try:
    result = 2 / 0
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

print("Test")

# Second block: divide by zero again with error object
try:
    result = 15 / 0
    print(result)
except ZeroDivisionError as e:
    print("Error:", e)


# Third block: user input with ValueError or TypeError handling
try:
    num = int(input("Enter a Number: "))
    print("You entered:", num)
except (ValueError, TypeError) as e:
    print("Invalid input:", e)


# Fourth block: check if a number is even or odd
try:
    num1 = int(input("Enter an old number: "))
    if num1 % 2 == 0:
        print(f"{num1} is even.")
    else:
        print(f"{num1} is odd.")
except (ValueError, TypeError) as e:
    print("Invalid input:", e)
