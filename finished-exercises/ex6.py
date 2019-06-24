# Assigns the value 10 to the variable types_of_people
types_of_people = 10
# Assignes the value of an f-string to the varibale x
x = f"There are {types_of_people} types of people."

# Assigns the value "binary" to the variable binary
binary = "binary"
# Assigns the value "don't" to the variable do_not
do_not = "don't"
# Assings the value of an f-string to the variable y
y = f"Those who know {binary} and those who {do_not}."

# Prints the value of variable x
print(x)
# Prints the value of variable y
print(y)

# Prints the value of variable x within an f-string
print(f"I said: {x}")
# Prints the value of variable y within an f-string
print(f"I also said: '{y}'")

# Sets the value of variable hilarious to False
hilarious = False
# Assigns the value of an f-string to the variable joke_evaluation and prints 
# the value of variable hilarious within
joke_evaluation = "Isn't that joke so funny?! {}"
# Prints the value of the joke_evaluation and the value of the hilarious
# variable using the .format string method
print(joke_evaluation.format(hilarious))

#  Assigns the value of a string to the variable w
w = "This is the left side of..."
#  Assigns the value of a string to the variable e
e = "a string with a right side."

# Prints a concatenation of the values of the w and e variables
print(w + e)