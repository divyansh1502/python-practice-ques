# Taking input from the user
num = int(input("Enter the number : "))

# Convert number to string to count the digit
num_digit = len(str(num))

# Compute the sum of digits raised to the power of num_digits
sum_of_digits = sum(int(digit) ** num_digit for digit in str(num))

# Check if the number is Armstrong
if num == sum_of_digits:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not a Armstrong number")
