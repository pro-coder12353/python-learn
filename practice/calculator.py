

operation = input("Enter a arithmetic operation : ")
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))


if operation == '+':
    operation = num1 + num2
    print(f"The sum of {num1} and {num2}  is {operation}")
elif operation == '-':
    operation = num1 - num2
    print(f"The subtraction of {num1} and {num2}  is {operation}")
elif operation == '*':
    operation = num1 * num2
    print(f"The multiplication of {num1} and {num2}  is {operation}")
elif operation == '/':
    operation = num1 / num2
    print(f"The division of {num1} and {num2}  is {operation}")
elif operation == '%':
    operation = num1 % num2
    print(f"The remainder of {num1} and {num2} is {operation}")
elif operation == '**':
    operation = num1 ** num2
    print(f"The exponent of {num1} and {num2} is {operation}")
else:
    print(f"Invalid input ")

