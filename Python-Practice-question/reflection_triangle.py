def pattern(n):
    # First half of the triangle
    for i in range(1, N + 1):
        print("*" * i)

    # Second half of the triangle
    for i in range(N - 1, 0, -1):
        print("*" * i)  

# Taking input from the user
N = int(input("Enter the number of rows: "))        
# Calling the function to print the pattern
pattern(N)

'''
*
**
***
****
*****
****
***
**
*
'''