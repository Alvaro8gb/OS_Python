Respond this questions about [run_processes.py](../run_processes.py)

a) **What happens if `run_processes` is executed without any arguments?**
If 'run_processes' is executed without arguments, it will print "Usage: python 1 number" because the length of the argument does not equal two. 

b) **What will the first child process created during the execution of `run_processes 3` do?**

During the execution of 'run_process 3', the first child will fork again to create another child process and print python, the name of the script, and the number of arguments. There is an image of the output in this directory (../exersize2_1b.png)

upload and image in this markdown

c) **Draw the process tree resulting from the execution of `run_processes 3`.**

Parent
   |
Child 1
   |
Child 2

d) **What would be the total number of processes created during the execution of `run_processes 3`, not counting the original parent process?**

2

e) **Reason whether, by executing `run_processes 3`, there could be any orphaned processes and/or any zombie processes. An orphaned process is considered to be one whose parent has died and is adopted by the `init` process.**

There could be an orphaned process/zombie process if the parent doesn't wait for the second child. This will happen if the second child process finishes before the parent child does.