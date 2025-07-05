n = int(input("Enter the positive number : "))

if n < 1:
    print("Please enter a positive integer")
else:
    sum =  0
    for i in range(1,n+1):
        sum += i
    print(f"The sum of natural number from 1 to {n} is {sum}")
