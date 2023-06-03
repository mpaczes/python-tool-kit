from threading import Thread, Lock, RLock
from time import time, ctime, sleep

def print_time(threadName: str, delay: int, counter: int):
    while counter:
        sleep(delay)
        print(f'wątek - {threadName}, czas lokalny - {ctime(time())}')
        counter -= 1

class WatekZBlokada(Thread):

    def __init__(self, thread_id: int, thread_name: str, counter: int):
        Thread.__init__(self, name=thread_name)
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.counter = counter

    def run(self):
        print(f'Starting thread : {self.thread_name}')

        # Get lock to synchronize threads
        thread_lock.acquire(blocking=True)

        print_time(self.thread_name, 3, self.counter)

        # Free lock to release next thread
        thread_lock.release()

print("Entering Main Thread")

# There are two ways to get thread lock - Lock and RLock classes.

# Lock - A lock is not owned by the thread that locked it; another thread may unlock it.  
# A thread attempting to lock a lock that it has already locked will block until another thread unlocks it. 
# Deadlocks may ensue.
# thread_lock = Lock()

# RLock - This class implements reentrant lock objects.
# A reentrant lock must be released by the thread that acquired it. 
# Once a thread has acquired a reentrant lock, the same thread may acquire it again without blocking; 
# the thread must release it once for each time it has acquired it.
thread_lock = RLock()

threads = []
# Create new threads
thread_one = WatekZBlokada(401, 'Wątek nr 1', 2)
thread_two = WatekZBlokada(502, 'Wątek nr 2', 3)
threads.append(thread_one)
threads.append(thread_two)

# Start new Threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("Exiting Main Thread")
