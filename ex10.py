tabby_cat = "\tI'm tabbed in." # \t adds a tab/indent (four spaces)
persian_cat = "I'm split\non a line." # \n splits this to a new line
backslash_cat = "I'm \\ a \\ cat." # the 1st \ lets you print the 2nd \!

# and here we have our free-style text again,
# but this time with \t indents and an indented new line, \n\t !
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# righto... to print the results!
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
