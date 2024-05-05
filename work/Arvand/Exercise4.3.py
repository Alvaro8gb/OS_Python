import sys

with open(sys.argv[1], 'a') as output_file: # open as output file

    sys.stdout, sys.stderr = output_file, output_file # redirect stdout and stderror to the output file 
    for i in range(16):
        print(f'test {i}')
 
    sys.stderr.write("stderror") # writing to stderror to ensure output is redirected to file