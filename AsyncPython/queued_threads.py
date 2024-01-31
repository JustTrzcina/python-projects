import time
import random
import queue
from threading import Thread

counter = 0
job_queue = queue.Queue() #things to print
counter_queue = queue.Queue() ## amount by which we ned to increase the counter

def increment_manager():
    global counter
    while True:
        increment = counter_queue.get() # wait until item is available and lock queue
        old_counter = counter
        time.sleep(random.random())
        counter = old_counter+increment
        time.sleep(random.random())
        job_queue.put((f'New counter values is {counter}','------'))
        counter_queue.task_done()

Thread(target=increment_manager,daemon=True).start()


def printer_manager():
    while True:
        for line in job_queue.get():
            print(line)
        job_queue.task_done()

Thread(target=printer_manager,daemon=True).start()

def increment_counter():
    counter_queue.put(1)
    time.sleep(random.random())

workerThreads = [Thread(target=increment_counter) for thread in range(10)]

for thread in workerThreads:
    thread.start()

for thread in workerThreads:
    thread.join()

counter_queue.join()
job_queue.join()