# MultiThreading with the Thread Pool executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number: {number}"

numbers = [1,2,3,4,5]

#Here we want to do the same work with different numbers 
# In generally it is done by single threading but by using ThreadPool Eaecutor we can do the work with multiple threads

t = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number,numbers)

for result in results:
    print(result)

final_time = time.time()-t
print(final_time)
