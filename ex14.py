# from the module 'sys(tem)' import 'argv'
from sys import argv

# when runing this, the program takes ex14.py as the first argument
# and is expecting a 'name' (your name) as the 2nd argument
script, user_name = argv

# when the program is run, you see a '>' waiting for first answer
prompt = '>'

# print(f... is for format printing using the, already provided, variables
# user_name and script.
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")

# This is the first question (you see the first prompt '>')
print(f"Do you like me {user_name}?")
# this captures the first question's answer
likes = input(prompt)

# second prompt and captured answer
print(f"Where do you live {user_name}?")
lives = input(prompt)

# third prompt and captured answer
print(f"What kind of computer do you have?")
computer = input(prompt)

# and to finish, we use the print(f""" formatted 'free typing'
# to report back on the above captured answers
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
