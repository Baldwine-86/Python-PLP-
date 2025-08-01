while True:
    print("Simple calculator")
    print("Operations: +, -, *, /")

    num1 = input("Enter first number: ")

    operator = input("Enter operator: ")

    num2 = input("Enter second number: ")

    try:
    
        num1 = float(num1)
        num2 = float(num2)


        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 ==0:
                print("Error: Divisionby zero!")
                continue
            results = num1 / num2
        else:
            print("Invalid operator!")
            continue

        print(f"Result: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Error: Invalid number input")