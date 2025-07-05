n = int(input("Enter the number : "))

original = n
reverse = 0

while n > 0:
    ld = n % 10
    reverse = (reverse * 10) + ld
    n = n // 10
if original == reverse:
    print(f"Number is Palindrome")
else:
    print("Number is not Palindrome")