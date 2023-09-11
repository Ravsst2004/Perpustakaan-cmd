class Book():
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

# Add books to list of books
def add_book():
    print("===ADD BOOK===")
    title = input("Title: ")
    author = input("Author: ")
    content = input("Content: ")
    new_book = Book(title, author, content)
    list_books.append(new_book)
    print("===BOOK ADDED===")

# show the list of books
def show_book():
    if len(list_books) == 0:
        print("===THERE'S NO BOOK====")
    else:
        print("===LIST OF BOOKS===")
        for index, book in enumerate(list_books):
            print(f"{index+1}) {book.title}")
            
        try:
            option = input("Option / (type:'back'): ")
            back_menu(option)
            
            option_next = int(option)
            if 1 <= option_next <= len(list_books):
                taken_book = list_books[option_next-1]
                print("==="*2)
                print(f"Title: {taken_book.title}")
                print(f"Author: {taken_book.author}")
                print(f"Content: {taken_book.content}")
                print("==="*2)
            else:
                print("===THERE'S NO BOOK====")
        except ValueError:
            print("===PLEASE INPUT A VALID OPTION===")

# delete the books
def delete_book():
    if len(list_books) == 0:
        print("===THERE'S NO BOOK====")
    else:
        print("===LIST OF BOOKS===")
        for index, book in enumerate(list_books):
            print(f"{index+1}) {book.title}")
            
        option = int(input("Option: "))
        if 1 <= option <= len(list_books):
            option_validation = input("===ARU U SURE TO DELETE THIS (y/n): ")
            if option_validation.lower() == "y":
                delete_book = list_books[option-1]
                list_books.remove(delete_book)
                print("===BOOKS DELETED===")
            elif option_validation.lower() == "n":
                return main()
            else:
                print("===PLEASE INPUT A VALID OPTION===")
        else:
            print("===THERE'S NO BOOK====")

# search book in the list
def search_book():
    search_book = input("Search: ")
    found_books = []
    for book in list_books:
        if search_book.lower() == book.title.lower():
            found_books.append(book)
            
    if len(found_books) == 0:
        print("===NO MATCHING BOOKS FOUND===")
    else:
        print("===MATCHING BOOKS===")
        for index, books in enumerate(found_books):
            print(f"{index+1}) {books.title}")
            
        try:
            option = input("Option / (type:'back'): ")
            back_menu(option)
            
            option_next = int(option)
            if 1 <= option_next <= len(list_books):
                taken_book = list_books[option_next-1]
                print(f"Title: {taken_book.title}")
                print(f"Author: {taken_book.author}")
                print(f"Content: {taken_book.content}")
            else:
                print("===THERE'S NO BOOK====")
        except ValueError:
            print("===PLEASE INPUT A VALID OPTION===")
        
# back to menu
def back_menu(option):
    if option.lower() == "back":
        print("BACK TO MENU")
        return main()

# list of books
list_books = []


# main
def main():
    while True:
        menu = """
        1) Add
        2) Show
        3) Delete
        4) Search
        5) Exit
        """
        print(menu)
        
        try:
            option = int(input("Option: "))
            
            if option == 1: 
                add_book()
            elif option == 2:
                show_book()
            elif option == 3:
                delete_book()
            elif option == 4:
                search_book()
            elif option == 5:
                exit()
            
        except ValueError:
            print("Please enter valid option")
        
        
main()