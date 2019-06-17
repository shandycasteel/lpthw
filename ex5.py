name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually, that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair")
print(f"His teeth are ususally {teeth} depending on coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

height_cm = round(height * 2.54)
print(f"Those {height} inches turn out to be about {height_cm} centimeters.")

weight_kg = round(weight / 2.2046)
print(f"Those {weight} pounts turn out to be about {weight_kg} kilograms.")