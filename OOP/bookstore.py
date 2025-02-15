class Book:
  def __init__(self, name, author, price, pages_num):
     self.name = name
     self.author = author
     self.price = price
     self.pages_num = pages_num
  
  def __repr__(self):
     return f"{self.name} by {self.author}"
  
class Bookstore:
   
  def __init__(self,max_books):
    self.books = []
    self.max_books = max_books

  def add_book(self,book):
    if self.count_books() < self.max_books:
      self.books.append(book)
    else: 
      raise ValueError(f"Max number of books in the store is {self.max_books}")
  
  def remove_book(self,book):
    self.books.remove(book)

  def find_book(self,title):
        for book in self.books:
           if title.lower() in book.name.lower():
              return book
        return None
      
  def list_books(self):
    return self.books
  
  def count_books(self):
    return len(self.books)
  

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99, 218)
book2 = Book("1984", "George Orwell", 8.99, 328)
book3 = Book("Moby Dick", "Herman Melville", 12.99, 585)


store = Bookstore(max_books=5)

store.add_book(book1)
store.add_book(book2)
store.add_book(book3)
store.add_book(Book("To Kill a Mockingbird", "Harper Lee", 7.99, 324))

print(store.list_books())

print(store.find_book("das"))

store.add_book(Book("Mac Miller", "Hoo Lang", 9, 12))
store.add_book(Book("Enine", "Joe Peach", 19, 123))



print(store.list_books())
print(store.count_books())

