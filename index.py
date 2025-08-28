# Enhanced Calculator with loop
print("Simple Calculator")
print("Enter 'quit' to exit")

while True:
    # Get input
    num1 = input("Enter first number (or 'quit' to exit): ")
    
    if num1.lower() == 'quit':
        print("Goodbye!")
        break
    
    operator = input("Enter operator (+, -, *, /): ")
    num2 = input("Enter second number: ")
    
    try:
        # Convert to numbers
        num1 = float(num1)
        num2 = float(num2)
        
        # Perform calculation
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."
        else:
            result = "Invalid operator!"
        
        # Display result
        print(f"Result: {result}")
        print("-" * 30)
        
    except ValueError:
        print("Please enter valid numbers!")
        print("-" * 30)