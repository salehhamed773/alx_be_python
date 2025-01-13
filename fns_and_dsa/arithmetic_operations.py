result = perform_operation(num1, num2, operation)
print(f"Result: {result}")
def perform_operation(num1: float, num2: float, operation: str) -> float:
     if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation."
