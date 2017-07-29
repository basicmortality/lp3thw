name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# The next bit is going to convert the 'inches' and 'lbs' to 'centimeters' and 'kilograms'.

metric_height = height * 2.54
metric_weight = weight * 0.453

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually, that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth}, depending on the coffee.")

# this line is tricky. try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
print(f"Imperial weight is {weight} lbs and Metric weight is {metric_weight} kg.")
print(f"Imperial height is {height} inches and Metric height is {metric_height} cm.")
