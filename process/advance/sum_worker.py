# subprocess_sum_worker.py
import sys

def calculate_sum(start, end):
    numbers = list(range(1, 10001))
    return sum(numbers[start:end])

if __name__ == "__main__":
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    result = calculate_sum(start, end)
    print(result)
