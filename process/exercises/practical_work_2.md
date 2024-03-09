
# Exercise 2.1
Respond this questions about [run_processes.py](../run_processes.py)

a) **What happens if `run_processes` is executed without any arguments?**


---

b) **What will the first child process created during the execution of `run_processes 3` do?**

upload and image in this markdown

---

c) **Draw the process tree resulting from the execution of `run_processes 3`.**


---

d) **What would be the total number of processes created during the execution of `run_processes 3`, not counting the original parent process?**


---

e) **Reason whether, by executing `run_processes 3`, there could be any orphaned processes and/or any zombie processes. An orphaned process is considered to be one whose parent has died and is adopted by the `init` process.**

# Exercise 2.2
The objective of this exercise is to develop a process through the use of Python’s os and signal modules that simulates `kill -9 <pid>` command

# Exercise 2.3
Create a daemon process.
 Daemon processes are started working when the system will be bootstrapped and terminate only when the system is  shutdown. ( dont have parents)
 It does not have a controlling terminal. It always runs in the background.

# Exercise 2.4

Code in Python for Unix the program "timer" whose invocation is:
`timer segs command [args...]`

capable of limiting the maximum execution time of the command indicated as an argument:

- The indicated command (mandate) will be executed in a child process with the arguments (args...) indicated in the invocation.
- If the user presses Ctrl-C the indicated command (mandate) should die, but the parent process (temporizar) should not.
- If the child process does not finish before the time (seconds) indicated, the parent should warn it by sending the proper signal.
- If it has not finished (the child process) one second later, the parent should kill it.
- In any of these cases, the parent process must decode the termination status of the child process, display said status on the standard output, and terminate correctly.
