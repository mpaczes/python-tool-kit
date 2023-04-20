# tworzenie watkow w sposob manualny (stary sposób)

import time # This module provides various functions to manipulate time values.

import threading # Thread module emulating a subset of Java's threading model.

start = time.perf_counter() # Performance counter for benchmarking.

def do_something(seconds):
    print(f'sleeping 1 {seconds} ...')
    time.sleep(seconds)
    print('done sleeping ...')

threads = []

# kilkanascie watkow
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    # nie mozemy wywolac t.join() w petli bo zrobilibysmy wywolania synchroniczne
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter() # Performance counter for benchmarking.

print(f'finished in {round(finish - start, 2)} second(s)')

