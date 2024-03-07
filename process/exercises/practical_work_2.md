
# Exercise 2.1
Respond this questions about [run_processes.py](../run_processes.py)

a) **What happens if `run_processes` is executed without any arguments?**

    The program catches an error, as the program requires an argument to be run.
---

b) **What will the first child process created during the execution of `run_processes 3` do?**

    The first child process will fork again, then print the arguments that the command prompt will use to run the execute the program again. These arguments are the same as their original arguments, except the number has been decremented by one (the new number is 2).

---

c) **Draw the process tree resulting from the execution of `run_processes 3`.**

                    3
                    |
                    -----
                        |
                        2
                        |
                    -------------------------
                    |                       |
                    1                       2
                    |                       |
                ----------                  1
                |        |                  |
                0        1              ---------
                |        |              |       |
                0        0              0       1
                         |              |       | 
                         0              0       0 
                                                |
                                                0
                 
d) **What would be the total number of processes created during the execution of `run_processes 3`, not counting the original parent process?**

    14 processes.
---

e) **Reason whether, by executing `run_processes 3`, there could be any orphaned processes and/or any zombie processes. An orphaned process is considered to be one whose parent has died and is adopted by the `init` process.**


    I believe that there can be orphaned/zombie processes that stem from 'run_processes 3.' In the program, an if-else sequence is used to determine whether the current process is a parent or a child process. In the the statement for the parent process, the operating system is instructed to wait until any child process is completed, as given by the line 'os.waitpid(pid, 0).' The argument of 0 means that it will wait for any child process to be completed, meaning that if other child processes exist, they will be abandoned by their parent process.


# Exercise 2.2

See killer.py

# Exercise 2.3

See daemon.py and daemon_function.py

# Exercise 2.3

See timer.py