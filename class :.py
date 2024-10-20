import json

# فئة الكتاب
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def __repr__(self):
        return f"'{self.title}' by {self.author} - {self.copies} copies available"

# فئة العضو
class Member:
    def __init__(self, name, member_id, borrowed_books=None):
        self.name = name
        self.member_id = member_id
        # borrowed_books معامل اختياري
        self.borrowed_books = borrowed_books if borrowed_books is not None else []

    def borrow_book(self, book):
        if book.copies > 0:
            book.copies -= 1
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}.")
        else:
            print(f"Sorry, {book.title} is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.copies += 1
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} does not have {book.title}.")

    def __repr__(self):
        return f"Member: {self.name}, ID: {self.member_id}, Borrowed books: {len(self.borrowed_books)}"

# فئة المكتبة
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author, copies):
        book = Book(title, author, copies)
        self.books.append(book)
        print(f"Added {book} to the library.")

    def add_member(self, name, member_id):
        member = Member(name, member_id)
        self.members.append(member)
        print(f"Added member {name} with ID {member_id}.")

    def list_books(self):
        for book in self.books:
            print(book)

    def list_members(self):
        for member in self.members:
            print(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        print(f"Book titled '{title}' not found.")
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        print(f"Member with ID {member_id} not found.")
        return None

# التعامل مع الملفات
class FileHandler:
    @staticmethod
    def save_data(filename, data):
        with open(filename, 'w') as file:
            json.dump(data, file, default=lambda o: o.__dict__)

    @staticmethod
    def load_data(filename, cls):
        with open(filename, 'r') as file:
            data = json.load(file)
            return [cls(**item) for item in data]

# استخدام النظام
library = Library()

# إضافة كتب
library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 3)
library.add_book("1984", "George Orwell", 5)

# إضافة أعضاء
library.add_member("Anas", "M001")
library.add_member("Sara", "M002")

# عرض الكتب والأعضاء
print("\nAvailable Books:")
library.list_books()

print("\nLibrary Members:")
library.list_members()

# استعارة الكتب
member1 = library.find_member("M001")
book1 = library.find_book("1984")
if member1 and book1:
    member1.borrow_book(book1)

# حفظ البيانات
FileHandler.save_data('books.json', library.books)
FileHandler.save_data('members.json', library.members)

# استرجاع البيانات
loaded_books = FileHandler.load_data('books.json', Book)
loaded_members = FileHandler.load_data('members.json', Member)

print("\nLoaded Books from file:")
for book in loaded_books:
    print(book)

print("\nLoaded Members from file:")
for member in loaded_members:
    print(member)
