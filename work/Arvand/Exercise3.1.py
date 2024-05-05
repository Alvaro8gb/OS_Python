from sklearn import datasets # pip install scikit-learn
import pandas as pd # pip install pandas
import threading
import time
 
dataset = datasets.load_breast_cancer()
 
# Convert the data to a Pandas DataFrame
df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
df['target'] = dataset.target

def calculate_average(low, high):
    for c in range(low, high + 1):
        df.iloc[:, c].mean() # calculate the mean of the column at index c

def with_threads():
    '''
        ‼ computer has six cores, allowing for 12 working processes (threads) at a time ‼
        ‼ dataset of 31 attributes is partitioned into 12 sections, one section per thread ‼
    '''

    threads = []
    start_time = time.time()

    i = 0
    while i < 31: # attempt to split up work as evenly as possible between the 12 available threads
        if i < 24: # 8 threads calculate average of three columns
            thread = threading.Thread(target=calculate_average, args=(i, i + 2))
            threads.append(thread)
            thread.start()
            i += 3

        elif i < 30: # 3 threads calculate average of two columns
            thread = threading.Thread(target=calculate_average, args=(i, i + 1))
            threads.append(thread)
            thread.start()
            i += 2
        else: # 1 thread calculates average of one column
            thread = threading.Thread(target=calculate_average, args=(i, i))
            threads.append(thread)
            thread.start()
            i += 1

    for t in threads:
        t.join()

    return (time.time() - start_time)

def without_threads():
    start_time = time.time()
    for i in range(31):
        calculate_average(i, i)

    return (time.time() - start_time)

with open("thread_analysis.md", "a") as file:
    file.write(f"With threads {with_threads()} || Without threads {without_threads()} \n")