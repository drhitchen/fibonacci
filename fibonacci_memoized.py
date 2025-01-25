def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]

def generate_fibonacci_sequence_memoized(n_terms=10):
    if n_terms <= 0:
        return []
    
    sequence = [fibonacci_memoized(i) for i in range(n_terms)]
    return sequence

# Example usage
if __name__ == "__main__":
    n = 40  # You can adjust this
    print(f"The first {n} terms of the Fibonacci sequence are:")
    print(generate_fibonacci_sequence_memoized(n))