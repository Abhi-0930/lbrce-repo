# Calculating the result of a mathematical operation based on user input.

a = int(input())
b = int(input())

op = input()

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
    case "//":
        print(a // b)
    case "%":
        print(a % b)
    case _:
        print("Invalid operator")