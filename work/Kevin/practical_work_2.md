
# Exercise 2.1
Respond this questions about [run_processes.py](../run_processes.py)

a) **What happens if `run_processes` is executed without any arguments?**

` it tells the user how to run the program and returns 1.`
---


b) **What will the first child process created during the execution of `run_processes 3` do?**

` it will fork and print some arguments then re-run the program with the counter decremented.`

---


c) **Draw the process tree resulting from the execution of `run_processes 3`.**

.          A
       ____|____
      |         |
      B         C
   __|__     __|__
  |     |   |     |
  D     E   F     G
 | |   | | | |   | |
 H I   J K L M   N O

---


d) **What would be the total number of processes created during the execution of `run_processes 3`, not counting the original parent process?**

`14`


---
e) **Reason whether, by executing `run_processes 3`, there could be any orphaned processes and/or any zombie processes. An orphaned process is considered to be one whose parent has died and is adopted by the `init` process.**

`I don't think so as every parent process runs os.wait to wait for their children to finish executing before they end.`



# Exercise 2.2

`See kill.py`



# Exercise 2.3

`See daemon.py and daemon2.py`



# Exercise 2.3

`See timer.py`

