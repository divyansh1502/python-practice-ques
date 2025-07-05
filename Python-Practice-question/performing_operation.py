#taking input from the user
num1 = float(input("Enter the 1st number : "))
num2 = float(input("Enter the 2nd number : "))

# Performing Operation
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

#Managing division by 0
if num2 != 0:
    division = num1 / num2
else:
    print("Undefined Cannot divide by 0")

print(f"Addition : {addition}")
print(f"Subtraction : {subtraction}")
print(f"Multiplication : {multiplication}")
print(f"Division : {division}")
