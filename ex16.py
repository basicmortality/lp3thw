# from module bring in a feature
from sys import argv

# setting up what's expected for argv to recieve
script, filename = argv

# formatting the supplied filename into the sentence
print(f"We're going to erase {filename}.")
# giving the option to quit out of the program
print("If you don't want that, hit CRTL-C (^C).")
# or carrying on!
print("If you do want that, hit RETURN.")

# so long as you don't quit, onwards!
input("?")

# and we are about to
print("Opening the file...")
# bring the "filename" file into mem-buffer as 'writeable'
target = open(filename, 'w')

# and we are about to
print("Truncating the file. Goodbye!")
# wipe the "filename"
target.truncate()

print("Now I'm going to ask you for three lines.")
# set up three variables from the inputs
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Now i'm going to write these to the file.")

# target (the filename) write the line1 variable to the file
target.write(line1)
# special char$ \n new line! written to the file
target.write("\n")
# rinse and repeat for the others
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
# nuff said :¬)
target.close()
