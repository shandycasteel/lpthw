# Creates a variable and  asigns it to a string containing variable placeholders
formatter = "{} {} {} {}"

# Prints string using the the fromat function with variable values for each placeholder in the string
print(formatter.format(1, 2, 3, 4))
# Prints string using the the fromat function with variable values for each placeholder in the string
print(formatter.format("one", "two", "three", "four"))
# Prints string using the the fromat function with variable values for each placeholder in the string
print(formatter.format(True, False, False, True))
# Prints string using the the fromat function with variable values for each placeholder in the string
print(formatter.format(formatter, formatter, formatter, formatter))
# Prints string using the the fromat function with variable values for each placeholder in the string
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a peom",
    "Or a song about fear"
))
