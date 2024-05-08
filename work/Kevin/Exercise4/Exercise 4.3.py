import sys


# No difference if redirects are done in a different order
if len(sys.argv) != 2:
    print("Usage python \"Exercise 4.3.py\" output_file_path")
    sys.exit(1)    
with open(sys.argv[1], 'w') as output_file:
    sys.stdout= output_file 
    sys.stderr = output_file

    for j in range(100, 200):
        sys.stderr.write("hi")

    for i in range(100):
        print(i)
 
   