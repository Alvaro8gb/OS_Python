import subprocess

def calculate_sum(start, end, numbers):
    return sum(numbers[start:end])

def sum_with_subprocess(numbers):
    total = 0
    num_processes = 4
    processes = []

    for i in range(num_processes):
        start = i * len(numbers) // num_processes
        end = (i + 1) * len(numbers) // num_processes

        # Run a subprocess for each segment of the list
        process = subprocess.Popen(
            ["python", "sum_worker.py", str(start), str(end)],
            stdout=subprocess.PIPE, text=True
        )
        processes.append(process)

    # Wait for all subprocesses to finish and collect results
    for process in processes:
        process.wait()
        total += int(process.stdout.read().strip())

    return total

if __name__ == "__main__":
    numbers = list(range(1, 1001))
    result = sum_with_subprocess(numbers)
    print("Sum using subprocess:", result)
