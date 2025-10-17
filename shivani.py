def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    while True:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+ - * /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2 if num2 != 0 else "Error (divide by zero)"
        else:
            result = "Invalid operator"

        print("Result:", result)
        if input("Continue? (y/n): ").lower() != 'y':
            bre
