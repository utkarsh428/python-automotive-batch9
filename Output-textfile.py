import sys

#Open a file in write mode

file = open("Output.txt", "w")

#Redirect standard output to the file

sys.stdout = file

#All print statements will go into output.txt

print("Hi, My Name is Utkarsh Mishra")
print("We are on Python Automotive Testing Batch")

#closing the file

file.close()