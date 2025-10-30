#Open
with open("books.txt") as books:
    # read
    for book in books:
        #take off the whitespaces
        lines = book.strip()
        #display
        print(lines)
