print(""" I can handle the following operation:
1. Addition
2. Subtraction
3. Multiplication
""")


operation_str: str = input("Pick an operation from the option [Enter 1 -8]: ")
operation: int = int(operation_str)
num1_str: str = input("Enter num1: ")
num2_str: str = input("Enter num2: ")
num1: float = float(num1_str)
num2: float = float(num2_str)


if operation == 1:
    result = num1 + num2
elif operation == 2:
    result = num1 - num2
elif operation == 3:
    result = num1 * num2


print(f"The result is: {result}")
