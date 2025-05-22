def factorial(n):
    if n < 0:
        raise ValueError("Negative numbers don't have a factorial.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
print(factorial(5))  # Output: 120