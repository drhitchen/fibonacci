import matplotlib.pyplot as plt
import csv
import os

def read_csv_data(csv_file):
    num_terms = []
    recursive_times = []
    memoized_times = []
    iterative_times = []
    
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            num_terms.append(int(row["Num Terms"]))
            recursive_times.append(float(row["Recursive Time (s)"]))
            memoized_times.append(float(row["Memoized Time (s)"]))
            iterative_times.append(float(row["Iterative Time (s)"]))
    
    return num_terms, recursive_times, memoized_times, iterative_times

def plot_fibonacci_times(csv_file='data/fibonacci_timing.csv'):
    num_terms, recursive_times, memoized_times, iterative_times = read_csv_data(csv_file)
    
    plt.figure(figsize=(10, 6))
    plt.plot(num_terms, recursive_times, label='Recursive', marker='o', color='orange')
    plt.plot(num_terms, memoized_times, label='Memoized', marker='o', color='blue')
    plt.plot(num_terms, iterative_times, label='Iterative', marker='o', color='green')
    
    plt.xlabel('Number of Terms')
    plt.ylabel('Time (seconds)')
    plt.title('Fibonacci Sequence Timing')
    plt.yscale('log')  # Use a logarithmic scale to better visualize differences
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    # Ensure the data directory exists
    os.makedirs('data', exist_ok=True)
    plt.savefig("data/fibonacci_timing_plot.png")  # Save the plot as an image file
    plt.show()

if __name__ == "__main__":
    plot_fibonacci_times('data/fibonacci_timing.csv')