import argparse

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

def generate_fibonacci_sequence(n_terms=10):
    if n_terms <= 0:
        return []
    
    sequence = [fibonacci(i) for i in range(n_terms)]
    return sequence

def main():
    parser = argparse.ArgumentParser(description='Generate Fibonacci sequence.')
    parser.add_argument('num_terms', nargs='?', default=10, type=int,
                        help='Number of terms to generate (default: 10)')
    
    args = parser.parse_args()
    
    print(f"The first {args.num_terms} terms of the Fibonacci sequence are:")
    fibonacci_sequence = generate_fibonacci_sequence(args.num_terms)
    print(fibonacci_sequence)

if __name__ == "__main__":
    main()