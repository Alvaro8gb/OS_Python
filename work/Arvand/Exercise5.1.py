import os
import sys

cmd1, cmd2 = sys.argv[1], sys.argv[3]
arg1, arg2 = sys.argv[2], sys.argv[4]
r, w = os.pipe()
pid = os.fork()

if pid > 0: # parent
    os.dup2(w, 1)
    os.close(w) # close unused end of pipe

    os.execlp(cmd1, cmd1, arg1)

elif pid == 0: # child
    os.dup2(r, 0)
    os.close(r) # close unused end of pipe

    os.execlp(cmd2, cmd2, arg2)

else: # error
    print("WEE WOO")
    sys.exit()