import multiprocessing

def calculate_sum(start, end, numbers, result_list):
    result_list.append(sum(numbers[start:end]))

def sum_with_fork(numbers):
    total = 0
    num_processes = 4
    processes = []
    manager = multiprocessing.Manager()
    result_list = manager.list() #shared variable between process
    

    for i in range(num_processes):
        start = i * len(numbers) // num_processes
        end = (i + 1) * len(numbers) // num_processes

        # Run a subprocess for each segment of the list
        process = multiprocessing.Process(target=calculate_sum, args=(start, end, numbers, result_list))
        processes.append(process)

    # Start all processes
    for process in processes:
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    # Aggregate results
    total = sum(result_list)
    return total

if __name__ == "__main__":
    numbers = list(range(1, 1001))
    result = sum_with_fork(numbers)
    print("Sum using fork:", result)
