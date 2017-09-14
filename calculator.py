#This program creates a simple calculator


# Operation functions are created below

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

def square(x, y):
    return x ** y

def main():

    # Tells the user their operation choices

    print("1) Addition")
    print("2) Subtraction")
    print("3) Divide")
    print("4) Multiply")
    print("5) Square")

    # Asks the user for their inputs

    operation = int(input("Choose your operation choice: (1/2/3/4/5) "))
    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second numbebr: "))


    if operation == 1:
        print(add(num1,num2))

    elif operation == 2:
        print(subtract(num1,num2))

    elif operation == 3:
        print(divide(num1,num2))

    elif operation == 4:
        print(multiply(num1,num2))

    elif operation == 5:
        print(square(num1,num2))

    else:
        print("Please restart and enter a valid operation choice.")

main()
