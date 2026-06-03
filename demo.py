def calculate(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ValueError("Division by zero")
        return a / b
    else:
        raise ValueError(f"Unknown operator: {op}")


def main():
    print("Simple Calculator")
    print("Type 'exit' to quit\n")

    while True:
        expression = input("Enter expression (e.g. 3 + 5): ").strip()
        if expression.lower() == "exit":
            break

        parts = expression.split()
        if len(parts) != 3:
            print("Error: use format 'number operator number'\n")
            continue

        try:
            a = float(parts[0])
            op = parts[1]
            b = float(parts[2])
            result = calculate(a, op, b)
            print(f"Result: {result}\n")
        except ValueError as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
