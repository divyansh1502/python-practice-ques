n = int(input("Enter the number for their sum : "))


sum_of_digit = 0

while n > 0:
    ld = n % 10 # Get the last digit (ld)
    sum_of_digit += ld 
    n = n//10 #remove the last digit
print(f"The sum of digit is {sum_of_digit}")

    