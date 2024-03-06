#Code in Python for Unix the program "timer" whose invocation is: timer segs command [args...]

#capable of limiting the maximum execution time of the command indicated as an argument:

#The indicated command (mandate) will be executed in a child process with the arguments (args...) indicated in the invocation.
#If the user presses Ctrl-C the indicated command (mandate) should die, but the parent process (temporizar) should not.
#If the child process does not finish before the time (seconds) indicated, the parent should warn it by sending the proper signal.
#If it has not finished (the child process) one second later, the parent should kill it.

