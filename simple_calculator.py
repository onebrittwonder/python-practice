
# simple calculator

valid_operations = ["add", "subtract", "multiply", "divide", "history"]
operation_history = []

def add(x: int, y: int):
    return x + y

def subtract( x: int, y: int):
    return x - y

def multiply(x: int, y: int):
    return x * y

def divide(x: int, y: int):
    if y == 0:
        return "Error: Division by zero is undefined."
    return x // y

def add_to_history(result):
    operation_history.append(result)

def check_history():
    if operation_history:
        for operation in operation_history:
            print(operation)
    else:
        print("No history to display.")

def is_float(input):
    if input.count('.') == 1:
        left, right = input.split('.')
        if (left.isdigit() or left == '') and (right.isdigit() or right == ''):
            return True
        return False
    
def get_number(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        elif is_float(user_input):
            return float(user_input)
        else:
            print("Invalid input! Please enter valid number (whole number or decimal).")

def main():
    print("""
        A simple calculator. It works with input. 
        The program will ask for an operation and two numbers.
        """)
    
    operation_count = 0

    while True:
        operation = input("Operation (Add / Subtract / Multiply / Divide / History / Exit): ").lower()

        if operation == "exit":
            print(f"Total completed operations: {operation_count}")
            print("Exiting calculator...")
            break
            
        if operation == "history":
            check_history()
            continue

        if operation not in valid_operations:
            print("Invalid operation. Please try again.")
            continue # goes back to loop
        
        print("Enter two numbers for a calculation:")
        x = get_number("Enter the first number: ")
        y = get_number("Enter the second number: ")

        if operation == "add":
            result = add(x, y)
            operation_count += 1
            printed_operation = (f"{x} + {y} = {result}")
            print(printed_operation)
            add_to_history(printed_operation)

        elif operation == "subtract":
            result = subtract(x, y)
            operation_count += 1
            printed_operation = (f"{x} - {y} = {result}")
            print(printed_operation)
            add_to_history(printed_operation)

        elif operation == "multiply":
            result = multiply(x, y)
            operation_count += 1
            printed_operation = (f"{x} * {y} = {result}")
            print(printed_operation)
            add_to_history(printed_operation)

        elif operation == "divide":
            result = divide(x, y)
            operation_count += 1
            printed_operation = (f"{x} / {y} = {result}")
            print(printed_operation)
            add_to_history(printed_operation)
    
        print(f"Number of completed operations: {operation_count}")

if __name__ == "__main__":
    main()