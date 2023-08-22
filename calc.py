# TASK 2 - CALCULATOR by Kunwar Pal Singh

def calculator(num1, num2, operator):
    # addition
    if operator == "+":
        result = num1 + num2
        # subtract
    elif operator == "-":
        result = num1 - num2
        # multiply
    elif operator == "*":
        result = num1 * num2
        # divide
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Cannot divide by zero"
    else:
        result = "Error: Invalid operator"
    
    return result

# input numbers and operators
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

# printing result
result = calculator(num1, num2, operator)
print("Result:", result)
