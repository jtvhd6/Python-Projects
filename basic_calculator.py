"""Basic Calculator
This program performs basic arithmetic operations: addition, subtraction, multiplication, and division.
It takes two numbers and an operator as input from the user and returns the result of the operation."""

def calculator(): # Basic calculator function
    operations = { # Using lambda functions for operations.  Format: lambda arguements: expression
        '1': ('+', lambda x, y: x + y), # Using tuple to store operator and function
        '2': ('-', lambda x, y: x - y), # Using tuple to store operator and function
        '3': ('*', lambda x, y: x * y), # Using tuple to store operator and function
        '4': ('/', lambda x, y: "Error! Division by zero." if y == 0 else x / y) # Using tuple to store operator and function
    }

    print("\nSelect operation: 1. Add 2. Subtract 3. Multiply 4. Divide")
    
    while True:
        choice = input("Enter choice (1, 2, 3, or 4): ")
        if choice not in operations: # Invalid choice handling
            print("Invalid choice!"); continue
        
        try:
            num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
            op, operation = operations[choice] # Get operator and function
            result = operation(num1, num2) # Perform operation
            result = int(result) if result == int(result) else result # Convert to integer if result is a whole number
            print(f"{num1} {op} {num2} = {result}")
        except ValueError: # Handle non-numeric input
            print("Invalid input! Please enter numeric values.")

        if input("Another calculation? (yes/no): ").lower() != 'yes': break # Exit loop

    print("Thank you for using this basic calculator!")

calculator()