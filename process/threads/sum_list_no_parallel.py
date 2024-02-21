import sys
from time import time

if __name__ == "__main__":
    num_elems = int(sys.argv[1])
    
    numbers = list(range(1, num_elems))
    print("Number of elements", len(numbers))

    start = time()
    total = 0

    for i in numbers:
        total+=i

    end = time()


    print("Time execution", end-start, "Total", total)