# from system module import argv
from sys import argv

# on run, expecting two inputs
# the first being 'script' (ex15.py) and the second being the filename
# , which is, in this instance, ex15_sample.txt
script, filename = argv

# the variable 'txt' is allocated the data 'open' the 'ex15_sameple.txt'
txt = open(filename)

# formatted print to list what 'filename' was from your initial
# running of the ex15.py code
print(f"Here's your file {filename}:")

# once thx .txt is opened to mem-buffer from line 10
# the txt.read() reads the mem-buffer and prints to screen
print(txt.read())

# prompt for action...
print("Type the filename again:")
# and allocate the answer to 'input' in the variable 'file_again'
file_again = input("> ")

# here the variable 'txt_again' is loaded with the data of the
# open(ed) file_again (from the input above)
txt_again = open(file_again)

# and then txt_again.read() is printed from mem-buffer to screen
print(txt_again.read())
