# import 'argv' from module 'sys'
# run as python3.6 ex13a...py and then something to fill vars one-three
# as in python3.6 ex13a..py age sex religion
# i've not print() the first one (script) as that's not needed
# so it only picks up the last three and outputs v1,v2 and v3

from sys import argv

script, varone, vartwo, varthree = argv

print("What is your", varone , "?")
print("What is your", vartwo , "?")
print("What is your", varthree , "?")
