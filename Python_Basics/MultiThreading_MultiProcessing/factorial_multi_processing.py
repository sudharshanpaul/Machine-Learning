'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, 
involve significant computational work. Multiprocessing 
can be used to distribute the workload across multiple 
CPU cores, improving performance.

'''

import multiprocessing
import time
import math
import sys

## Increase the mazimum of digits for Integer conversion
sys.set_int_max_str_digits(100000)

## function to compute factorial of a given number

def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers = [5000,6000,700,8000]

    start_time = time.time()

    # Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial,numbers)
    
    end_time = time.time()

    print(f"Results: {results}")
    print(f"Time taken {end_time - start_time} seconds")