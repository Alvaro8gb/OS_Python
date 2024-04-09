import stat
import os, time

st = os.stat("data/hola.txt")

print("mode =", oct(stat.S_IMODE(st.st_mode)))

print("type =", end=' ')
if stat.S_ISDIR(st.st_mode):
    print("DIRECTORY")
if stat.S_ISREG(st.st_mode):
    print("REGULAR")
if stat.S_ISLNK(st.st_mode):
    print("LINK")

print("size =", st.st_size)

print("last accessed =", time.ctime(st.st_atime))
print("last modified =", time.ctime(st.st_mtime))
print("inode changed =", time.ctime(st.st_ctime))

