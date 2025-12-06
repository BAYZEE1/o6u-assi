import threading
import time

def worker(name):
    """Function to be executed by the thread."""
    print(f"Thread {name}: starting")
    time.sleep(1)
    print(f"Thread {name}: finishing")

if __name__ == "__main__":
    print("Starting Threading Example")
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Main thread: all workers finished")
