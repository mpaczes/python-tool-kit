# nowy sposob tworzenia watkow - 'thread pool executor'
# pojawil sie w wersji 3.2 Pythona

import concurrent.futures # Execute computations asynchronously using threads or processes.
import time

start = time.perf_counter() # Performance counter for benchmarking.

def do_something(seconds):
    print(f'sleeping {seconds} ...')
    time.sleep(seconds)
    return f'done sleeping {seconds} ...'

with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(do_something, 1)
    # f2 = executor.submit(do_something, 1)

    # ponizej jest skladnia 'list comprehensions'
    # results = [executor.submit(do_something, 2) for _ in range(10)]

    seconds = [5,4,3,2,1]
    results = [executor.submit(do_something, sec) for sec in seconds]

    # funkcja 'as_completed' zwraca wyniki w dowolnej kolejnosci, czyli ten watek ktory szybciej sie skonczy wygrywa
    for f in concurrent.futures.as_completed(results):
        print(f.result())

    # print(f1.result())
    # print(f2.result())

finish = time.perf_counter() # Performance counter for benchmarking.

print(f'finished in {round(finish - start, 2)} second(s)')

# inny sposob wywolania watkow z metoda 'map'
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    # funkcja 'map' zwraca wyniki w kolejnosci jak one byly wywolane
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

