# Things to use:
# print: print("There are", cars, "cars available.")
# math: print("Hens", 25 + 30 / 6)
# variables: with = stings OR = integers
# print inc' vars with f(ormat): print(f"Let's talk about {my_name}.")
# print(ing) with dots ("." * 10)
# or formatted variables: thing = "{} {}", print(thing.format(""))
# and also with triple quotes!
# \n new lines, \t indents, and \\ general escaped char$
#
#
ob1 = "Shoes"
ob2 = "T-shirts"
ob3 = "Shorts"
ob4 = "Socks"
ob5 = "Laptop"
ob6 = "Phone"
shoes = 2

packing_list = "{}\n{}\n{}\n{}\n{}\n{}"

print("-" * 20)
print("My Holiday Packing List:")
print(packing_list.format(ob1, ob2, ob3, ob4, ob5, ob6))
print("-" * 20)
print("*\tOne indent\t\t\t*")
print("*\t\tTwo indents\t\t*")
print("*\t\t\tThree indents\t*")
print("-" * 20)
print("Shoes =", shoes * 2, "pairs.")
print("T-shirts =", 10 / 2)
print("Shorts =", 1 + 1 * 2)
print("Socks =", shoes * 3, "pairs.")
print("Laptop =", 1)
print("Phone =", 2 - 1)
print("""
I guess you \"could\" say that this short
packing list isn't going to \\get\\ me very far.
In fact, this is only part of what is in my
suitcase. There are a lot more things in there!""")
