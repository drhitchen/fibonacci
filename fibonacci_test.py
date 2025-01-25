import time
import csv
import os
from fibonacci_recursive import generate_fibonacci_sequence as recur_fib
from fibonacci_memoized import generate_fibonacci_sequence_memoized as memoized_fib
from fibonacci_iterative import generate_fibonacci_sequence as iter_fib

def time_execution(func, n):
    start_time = time.perf_counter()
    func(n)
    end_time = time.perf_counter()
    return end_time - start_time

def run_tests(max_terms=40, output_file='data/fibonacci_timing.csv'):
    # Ensure the data directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Num Terms", "Recursive Time (s)", "Memoized Time (s)", "Iterative Time (s)"])

        for n in range(1, max_terms + 1):
            recursive_time = time_execution(recur_fib, n)
            memoized_time = time_execution(memoized_fib, n)
            iterative_time = time_execution(iter_fib, n)            
            writer.writerow([n, recursive_time, memoized_time, iterative_time])
            print(f"Computed times for {n} terms: Recursive = {recursive_time}s, Memoized = {memoized_time}s, Iterative = {iterative_time}s")

if __name__ == "__main__":
    run_tests(max_terms=40)  # Adjust `max_terms` as needed