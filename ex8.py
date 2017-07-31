formatter = "{} {} {} {}" # the four {} are spaced containers
# for the following formated print statements

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))

# this next, weird one, is telling .format to print "{} {} {} {}" four
# times (so there'll be twelve of them!).
print(formatter.format(formatter, formatter, formatter, formatter))

# don't be fooled by the four lines of comma seperated stings
# they print as spaced strings in the formatter format!
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
