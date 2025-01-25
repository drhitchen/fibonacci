# Fibonacci Project

This project is designed for learning Python through implementing and analyzing different Fibonacci sequence algorithms. It includes iterative, recursive, and memoized solutions.

## Project Structure

- `fibonacci_recursive.py`: Computes the Fibonacci sequence using a simple recursive approach.
- `fibonacci_memoized.py`: Computes the Fibonacci sequence using a memoized recursive approach.
- `fibonacci_iterative.py`: Computes the Fibonacci sequence using an iterative approach.
- `fibonacci_test.py`: Script to benchmark and compare the performance of different implementations.
- `plot_fibonacci.py`: Plots timing results for visualization.
- `tests/`: Contains unit tests for each approach.
- `data/`: Stores generated data files and plots.

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd fibonacci-project
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running Fibonacci Scripts

Execute any of the Fibonacci scripts with an optional number of terms:
```bash
python fibonacci_iterative.py <num_terms>
```

### Running Tests

To run all unit tests with detailed output:
```bash
python -m unittest discover tests -v
```

### Timing and Plotting

Run `fibonacci_test.py` to generate performance data and `plot_fibonacci.py` to visualize it:
```bash
python fibonacci_test.py
python plot_fibonacci.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.