while True:

    num1 = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Error")
    else:
        print("Unknown operation")

    answer = input("Wanna continue? (y/n or yes/no): ").lower()
    if answer not in ("y", "yes"):
        print("Calculator finished working")
        break