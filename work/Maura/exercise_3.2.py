# use subprocess library to execute 'nice -19 sleep 30'
# execute this in a terminal to check: 'ps -eo pid, user, cmd, ni | grep 19°

import subprocess

proc = subprocess.Popen(['nice', '-19', 'sleep', '30'])

proc.communicate()

# test with ps -eo pid,user,comm,ni | grep 19