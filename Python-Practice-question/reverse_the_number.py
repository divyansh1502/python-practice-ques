n = int(input("Enter the number : "))

reverse = 0

while n > 0:
    ld = n % 10
    reverse = (reverse * 10) + ld
    n = n // 10
print(f"The reverse of the given number is : {reverse}")