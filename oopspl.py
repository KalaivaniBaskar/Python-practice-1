# The __init__(), __str__(), __len__() and __del__() methods
# These special methods are defined by their use of underscores. They allow us to use Python specific functions on objects created through our class.

class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed") 

book = Book("Python Rocks!", "Jose Portilla", 159)

# w/o specifying __str__
print(book) #<__main__.Book object at 0x0000024B714A6030>

#Special Methods
print(book) # after manually defining __str__ fn
print(len(book))
del book