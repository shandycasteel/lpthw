tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

outline = '''
Learning Escape Sequences:
\t* Memorize escape sequences
\t* Use flashcards
\t* Use .format and excapes in a string
\t* Jot down anything you don't understand:
\t\tLike what does \\uxxxx do? It gives you: \u1812!
\t\tAnd how about \\222? Which nets you \222!
'''
print(outline)

escapes = "Do you here that\a\a\a\a\a\a\a?"
print(escapes)