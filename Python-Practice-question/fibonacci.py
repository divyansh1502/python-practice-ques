def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

num = int(input("Enter the number of terms in Fibonacci sequence: "))
print(f"{fibonacci(num)}")
