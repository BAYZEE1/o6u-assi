import threading
import time
import random

# A semaphore with a capacity of 3
semaphore = threading.Semaphore(3)

def access_resource(thread_id):
    """Function that simulates accessing a limited resource."""
    print(f"Thread {thread_id}: trying to acquire semaphore...")
    
    # Acquire the semaphore
    with semaphore:
        print(f"Thread {thread_id}: acquired semaphore. Accessing resource...")
        # Simulate work
        sleep_time = random.uniform(1, 3)
        time.sleep(sleep_time)
        print(f"Thread {thread_id}: finished accessing resource in {sleep_time:.2f}s. Releasing semaphore.")

if __name__ == "__main__":
    print("Starting Semaphore Example (Max 3 threads can run concurrently)")
    threads = []
    for i in range(10):
        t = threading.Thread(target=access_resource, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Main thread: all threads finished")
