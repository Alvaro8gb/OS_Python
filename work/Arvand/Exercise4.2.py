import os
import random

'''
    ‼ SYMBOLIC LINKS ‼
'''

# symbolic link begins here and leads to test1.txt
# l1 holds the path to test1.txt
l1 = f'test{random.randint(2, 16)}.txt' 

try:
    os.symlink('test1.txt', l1) # creates the link from l1 to test1.txt
except FileExistsError:
    pass

print(os.stat('test1.txt').st_ino, os.stat('test1.txt').st_nlink)
print(os.stat(l1))

# symbolic link begins here and leads to testA
# l2 holds the path to testA
l2 = f'test{random.randint(17, 32)}' 

try:
    os.symlink('testA', l2) # creates the link from l2 to testA
except FileExistsError:
    pass

print(os.stat('testA').st_ino, os.stat('testA').st_nlink)
print(os.stat(l2))

'''
    ‼ HARD LINKS ‼
'''

# create a file
h = f'hard{random.randint(2, 16)}.txt' 

try: 
    os.link('htest.txt', h) # direct connection from h1 to htest.txt's i-node (they are now connected to the same i-node)
except FileExistsError:
    pass

print(os.stat('htest.txt').st_ino, os.stat('htest.txt').st_nlink)
print(os.stat(h))

'''
    ‼ COMMENTS + ANSWERS ‼

    An i-node is still accessable if there are hard links leading to it. If there are no hard links leading to an i-node
    the operating system will deem the i-node available and will repurpose that i-node. So, if there are multiple hard links leading
    to an i-node, deleting one hard link doesn't affect the i-node. But once the last hard link to the i-node is removed, the 
    i-node is available again to the OS.

    A deletion of a symbolic link has no effect on an i-node. Deleting an a symbolic link means the link is lost, but the file
    will remain unaffected.

    When a file is deleted, the symbolic link will remain; sym links are capable of pointing to null. On the other hand, all the hard
    links will have been deleted along with the file.
'''

