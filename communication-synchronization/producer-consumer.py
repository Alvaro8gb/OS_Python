import time
import random
from threading import Thread, Lock, Condition

BUFFER_SIZE = 5
buffer = []
lock = Lock()
buffer_not_full = Condition(lock)
buffer_not_empty = Condition(lock)

class Producer(Thread):
    def run(self):
        global buffer
        while True:
            item = random.randint(1, 1000)
            with buffer_not_full:
                while len(buffer) >= BUFFER_SIZE:
                    buffer_not_full.wait()
                buffer.append(item)
                print(f"Produced {item}. Buffer: {buffer}")
                buffer_not_empty.notify()

            time.sleep(1)

class Consumer(Thread):
    def run(self):
        global buffer
        while True:
            with buffer_not_empty:
                while not buffer:
                    buffer_not_empty.wait()
                item = buffer.pop(0)
                print(f"Consumed {item}. Buffer: {buffer}")
                buffer_not_full.notify()

            time.sleep(2)

def main():
    producer = Producer()
    consumer = Consumer()

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

if __name__ == "__main__":
    main()
