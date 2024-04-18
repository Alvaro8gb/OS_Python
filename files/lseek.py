import os

filename = 'data/hola.txt'

fd = os.open(filename, os.O_RDONLY)

offset = 14

os.lseek(fd, 14, os.SEEK_SET)

data = os.read(fd, 20)

decoded_data = data.decode('utf-8')

print(f"Data read from position {offset}: {decoded_data}")

os.close(fd)
