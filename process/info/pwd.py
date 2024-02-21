import os

#create a new directory
os.mkdir("mydir")

#change the currently running directory
os.chdir("mydir")

#Print the updated directory path
print ("Updated directory:" , os.getcwd())

