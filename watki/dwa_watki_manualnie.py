# tworzenie watkow w sposob manualny (stary sposób)

import time # This module provides various functions to manipulate time values.

import threading # Thread module emulating a subset of Java's threading model.

start = time.perf_counter() # Performance counter for benchmarking.

def do_something():
    print('sleeping 1 second ...')
    time.sleep(1)
    print('done sleeping ...')

# do_something()
# do_something()

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start() # Start the thread's activity.
t2.start()

t1.join() # Wait until the thread terminates.
t2.join()

finish = time.perf_counter() # Performance counter for benchmarking.

print(f'finished in {round(finish - start, 2)} second(s)')

