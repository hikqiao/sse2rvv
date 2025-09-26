def calculate_factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    # Test factorial
    print(f"Factorial of 5: {calculate_factorial(5)}")
    
    # Test Fibonacci
    print(f"First 10 Fibonacci numbers: {fibonacci(10)}")
    
    # Test prime check
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"Is 20 prime? {is_prime(20)}")