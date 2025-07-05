num = int(input("Enter the number greater than 1: "))

count = 0;
if num < 2:
    print("Enter number grater than 1")
else:
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count==2:
        print(f"The number {num} is Prime")
    else:
        print(f"The number {num} is not Prime")
