import argparse

def generate_fibonacci_sequence(n_terms=10):
    if n_terms <= 0:
        return []
    elif n_terms == 1:
        return [0]

    fibonacci_sequence = [0, 1]
    
    while len(fibonacci_sequence) < n_terms:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)

    return fibonacci_sequence

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