import threading
import time

# Define two locks
lock_a = threading.Lock()
lock_b = threading.Lock()

def thread_1():
    """Tries to acquire lock_a then lock_b."""
    name = threading.current_thread().name
    print(f"{name} is trying to acquire lock_a")
    with lock_a:
        print(f"{name} acquired lock_a")
        time.sleep(0.1) # Give a chance for thread_2 to acquire lock_b
        print(f"{name} is trying to acquire lock_b")
        with lock_b:
            print(f"{name} acquired both locks")

def thread_2():
    """Tries to acquire lock_b then lock_a."""
    name = threading.current_thread().name
    print(f"{name} is trying to acquire lock_b")
    with lock_b:
        print(f"{name} acquired lock_b")
        time.sleep(0.1) # Give a chance for thread_1 to acquire lock_a
        print(f"{name} is trying to acquire lock_a")
        with lock_a:
            print(f"{name} acquired both locks")

if __name__ == "__main__":
    print("Starting Deadlock Example (may hang)")
    t1 = threading.Thread(target=thread_1, name="Thread-1")
    t2 = threading.Thread(target=thread_2, name="Thread-2")

    t1.start()
    t2.start()

    # The program will likely hang here due to deadlock
    # t1.join()
    # t2.join()
    print("Main thread finished execution (Deadlock may occur in background)")
