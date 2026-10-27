# Level 2& 3- Combine two ideas

books = []

online_books = {"title": "A little life",
                "author": "Hanya Yanagihara",
                "pages": 780,
                }

hardcopy_books = {"title": "The fine print",
                  "author": "Lauren Asher",
                  "pages": "350"
                  }

library_books = {"title": "The unwritten rules",
                 "author": "Elizabeth Scott",
                 "pages": "408"}

books.append(online_books)
books.append(hardcopy_books)
books.append(library_books)
#function to display list
#def shelf():
   #print(books)

#shelf()

#--- searching for the book---
def search(title):
    for book in books:
        if book["title"] == title:
            print(book)
        else:
            print("Book not found.")

book = input("Enter the book you are searching for: ")
#Level 1
def greet(name):
    print(f"Hello, {name}!")

greet("Palesa")

def add(a, b):
    return a + b

sum = add(5, 4)
print(f"The answer is: {sum}")

#Dictionary

book = {"title": "A little Life",
        "author": "Hanya Yanagihara",
        "Pages": 780,
        }

print(f'The next book on your TBR is: {book["title"]}')