# Dictionary to map operations to their corresponding functions
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else None  # Return None for division by zero
}

def main():
    # Get valid numbers from the user
    num1 = get_valid_number("Enter the first number: ")
    num2 = get_valid_number("Enter the second number: ")

    # Get a valid operation from the user
    operation = get_valid_operation()

    # Perform the calculation using the dictionary mapping
    result = operations[operation](num1, num2)

    # Handle division by zero
    if result is None:
        print("Error: Division by zero is not allowed.")
    else:
        # Display the result
        print(f"{num1} {operation} {num2} = {result}")

# Function to get a valid number input from the user
def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")

# Function to get a valid operation input from the user
def get_valid_operation():
    while True:
        operation = input("Enter the operation (+, -, *, /): ")
        if operation in operations:
            return operation
        else:
            print("Error: Invalid operation. Please enter +, -, *, or /.")

# This block ensures the main() function runs only when the script is executed directly,
# not when it is imported as a module.
if __name__ == "__main__":
    main()
