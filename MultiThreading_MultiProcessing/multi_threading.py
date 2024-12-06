## Multi Threading
## When to use multi threading?
### I?O bound task: Task that spends more time waiting for I?O operations(e.g., file operationd, network requests)
## Concurrent execution: When you want to improve the throughput of your application by concurrent execution

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter:{letter}")

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)

t = time.time()

## Starting the Threads
t1.start()
t2.start()

##Wait for threads to complete and join with the main thread

t1.join()
t2.join()


finished_time = time.time()-t
print(finished_time)