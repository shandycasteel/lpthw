from sys import argv
# read the WYSS section for how to run this
script, count, food = argv

answer = False
while answer == False:
    question = input(f"So that's {count} {food} you wanted? (Yes/No): ")
    if question == "Yes":
        answer = True
        print("Ok, we'll get your order ready!")
