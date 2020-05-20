# defines a function that takes two paramaters
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # prints an f-string that uses one of the function arguments
    print(f"You have {cheese_count} cheeses!")
    # prints an f-string that uses one of the function arguments
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # prints an f-string
    print("Man, that's enough for a party!")
    # prints an f-string and returns a new line
    print("Get a blanket.\n")


# prints an f-string
print("We can just give the function numbers directly:")
# calls the function and passes two arguments into it
cheese_and_crackers(20, 30)


# prints an f-string
print("OR, we can use variables from our script:")
# creates a variable and gives it a value
amount_of_cheese = 10
# creates a variable and gives it a value
amount_of_crackers = 50

# calls the function and passes the two variables into it as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# prints an f-string
print("We can even do math inside too:")
# calls the function with arguments using caluclations to find the value
cheese_and_crackers(10 + 20, 5 + 6)


# prints an f-string
print("And we can combine the two, variables and math:")
# calls the function and passes two variables with calcualations as arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def counts_books(number_of_books, number_of_authors):
    avg_books_per_author = float(number_of_books/number_of_authors)
    print(f"I have {number_of_books} books!")
    print(f"There are {number_of_authors} different authors in my collection.")
    print("I'll eventually need more bookshelves.")
    print(f"It should be noted that comes out to about {avg_books_per_author} books for each author.\n")


counts_books(230, 87)

books = 113
authors = 32
counts_books(books, authors)

counts_books(150 + 300, 60 + 72)

books = 16
authors = 4
counts_books(books + 114, authors + 24)

i = 1
for book in range(6):
    counts_books(100 * i, 10 * i)
    i += 1

books = int(float(input("How about you tell us how many books: ")))
authors = int(float(input("...and now how many authors: ")))
counts_books(books, authors)