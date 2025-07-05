import math

# Taking input for coefficients a, b, and c
a = float(input("Enter the coefficient of a: "))
b = float(input("Enter the coefficient of b: "))
c = float(input("Enter the coefficient of c: "))

# Calculating the Discriminant
discriminant = b**2 - 4*a*c

# Calculating the nature of roots
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Two distinct real roots: {root1} and {root2}")
elif discriminant == 0:
    root = -b / (2 * a)
    print(f"One real root (repeated): {root}")
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
    print(f"Complex roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")
