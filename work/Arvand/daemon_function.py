import os

fp = open('foo.txt', 'x')

# Verify that foo.txt has been created
print(os.listdir())

fp.close()