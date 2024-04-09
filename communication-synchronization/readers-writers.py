import time
import random
from threading import Thread, Lock, Condition


NUM_READERS = 3
NUM_WRITERS = 2

readers_reading = 0
writing = False
lock = Lock()
reader_condition = Condition(lock)
writer_condition = Condition(lock)

class Reader(Thread):
    def run(self):
        global reader_condition, writer_condition, readers_reading, writing
        while True:
            time.sleep(random.uniform(0.1, 1))
            with reader_condition:
                while writing:
                    reader_condition.wait()
                readers_reading += 1
                print(f"Reader {self.name} is reading. Readers reading: {readers_reading}")
            
            time.sleep(random.uniform(0.1, 1))

            with reader_condition:
                readers_reading -= 1
                if readers_reading == 0:
                    writer_condition.notify()
            
            print(f"Reader {self.name} stop reading. Readers reading: {readers_reading}")
                
class Writer(Thread):
    def run(self):
        global reader_condition, writer_condition, readers_reading, writing

        while True:
            time.sleep(random.uniform(0.1, 1))
            with writer_condition:
                while readers_reading > 0 or writing:
                    writer_condition.wait()
                writing = True
                print(f"Writer {self.name} is writing.")
                
            time.sleep(random.uniform(0.1, 1))
            
            with writer_condition:
                writing = False
                reader_condition.notify_all()

            print(f"Writer {self.name} stop writing.")

def main():
    readers = [Reader() for _ in range(NUM_READERS)]
    writers = [Writer() for _ in range(NUM_WRITERS)]

    for reader in readers:
        reader.start()
    for writer in writers:
        writer.start()

    for reader in readers:
        reader.join()
    for writer in writers:
        writer.join()

if __name__ == "__main__":
    main()
