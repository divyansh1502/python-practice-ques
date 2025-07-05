#Takinig input
num = int(input("Enter the number : "))

# Factorial of 0 and 1 is 1
fact = 1
if num < 0:
    print("Factorial is not defined for negative numbers ")
else:
    for i in range(1,num + 1):
        fact *= i
    print(f"The factorial of {num} is {fact}")