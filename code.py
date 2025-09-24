# ---------- BIG TEST CODE START ----------
import random
import math
import time

def generate_primes(n: int):
    """Generate prime numbers up to n."""
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for div in range(2, int(math.sqrt(num)) + 1):
            if num % div == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def fibonacci(n: int):
    """Generate n Fibonacci numbers."""
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

def matrix_multiply(A, B):
    """Multiply 2D matrices A and B."""
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    if cols_A != rows_B:
        raise ValueError("Matrix dimensions do not match!")
    
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

def run_big_test():
    """Run multiple heavy computations for Render test."""
    print("🔹 Running Big Test Code...")

    # Prime numbers
    primes = generate_primes(2000)
    print(f"Generated {len(primes)} primes up to 2000.")

    # Fibonacci
    fib = fibonacci(30)
    print(f"Fibonacci sequence (30 terms): {fib}")

    # Matrix multiplication
    A = [[random.randint(1, 5) for _ in range(5)] for _ in range(5)]
    B = [[random.randint(1, 5) for _ in range(5)] for _ in range(5)]
    result = matrix_multiply(A, B)
    print("Matrix A:", A)
    print("Matrix B:", B)
    print("Matrix A*B:", result)

    print("✅ Big Test Code Completed!")

