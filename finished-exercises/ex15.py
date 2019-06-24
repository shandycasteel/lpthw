# Imports the argv command line arguments object from the sys package
from sys import argv

# Assigns variables to the two comman lind argument values
script, filename = argv

# Opens the file with the name passed in at the command line and assigns its value to a variable
txt = open(filename)

# Print statement
print(f"Here's your file {filename}:")
# Reads the file passed into the txt variable and prints the results
print(txt.read())
txt.close()

# Print statement asking for input
print("Type the filename again:")
# Assigns the user input to a variable
file_again = input('> ')

# Opens the file with the name given through the above input and assigns its value to a variable
text_again  = open(file_again)

# Reads the file passed into the text_again variable and prints the results
print(text_again.read())
txt.close()