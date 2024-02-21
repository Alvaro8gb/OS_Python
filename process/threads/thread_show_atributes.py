import threading
import time

def print_thread_attributes(thread):
    print(f"Thread Name: {thread.name}")
    print(f"Thread ID: {thread.ident}")
    print(f"Is Daemon: {thread.daemon}")
    print(f"Is Alive: {thread.is_alive()}")
    print()

def thread_function():
    time.sleep(2)

# Create a thread
my_thread = threading.Thread(target=thread_function)

# Print thread attributes before starting
print_thread_attributes(my_thread)

# Start the thread
my_thread.start()

# Print thread attributes after starting
print_thread_attributes(my_thread)

# Wait for the thread to finish
my_thread.join()

# Print thread attributes after joining
print_thread_attributes(my_thread)
