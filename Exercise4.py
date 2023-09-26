import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="library_db"
)

# Create tables
def create_tables():
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Books (BookID INT AUTO_INCREMENT PRIMARY KEY, Title VARCHAR(255), Author VARCHAR(255), ISBN VARCHAR(255), Status VARCHAR(255))")
    cursor.execute("CREATE TABLE IF NOT EXISTS Users (UserID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Email VARCHAR(255))")
    cursor.execute("CREATE TABLE IF NOT EXISTS Reservations (ReservationID INT AUTO_INCREMENT PRIMARY KEY, BookID INT, UserID INT, ReservationDate DATE, FOREIGN KEY (BookID) REFERENCES Books(BookID), FOREIGN KEY (UserID) REFERENCES Users(UserID))")
    db.commit()

# Add a new book to the database
def add_book():
    cursor = db.cursor()
    title = input("Enter the book title: ")
    author = input("Enter the author name: ")
    isbn = input("Enter the ISBN: ")
    status = input("Enter the book status: ")
    sql = "INSERT INTO Books (Title, Author, ISBN, Status) VALUES (%s, %s, %s, %s)"
    values = (title, author, isbn, status)
    cursor.execute(sql, values)
    db.commit()
    print("Book added successfully")

# Find a book's details based on BookID
def find_book_details():
    cursor = db.cursor()
    book_id = input("Enter the BookID: ")
    sql = "SELECT Books.*, Reservations.ReservationDate, Users.Name, Users.Email FROM Books LEFT JOIN Reservations ON Books.BookID = Reservations.BookID LEFT JOIN Users ON Reservations.UserID = Users.UserID WHERE Books.BookID = %s"
    values = (book_id,)
    cursor.execute(sql, values)
    result = cursor.fetchone()
    if result:
        print("Book Details:")
        print("BookID:", result[0])
        print("Title:", result[1])
        print("Author:", result[2])
        print("ISBN:", result[3])
        print("Status:", result[4])
        print("Reservation Date:", result[5])
        print("User Name:", result[6])
        print("User Email:", result[7])
    else:
        print("Book not found")

# Find a book's reservation status based on BookID, Title, UserID, and ReservationID
def find_reservation_status():
    cursor = db.cursor()
    search_text = input("Enter the BookID, Title, UserID, or ReservationID: ")
    if search_text.startswith("LB"):
        sql = "SELECT Books.*, Reservations.ReservationDate, Users.Name, Users.Email FROM Books LEFT JOIN Reservations ON Books.BookID = Reservations.BookID LEFT JOIN Users ON Reservations.UserID = Users.UserID WHERE Books.BookID = %s"
        values = (search_text,)
    elif search_text.startswith("LU"):
        sql = "SELECT Books.*, Reservations.ReservationDate, Users.Name, Users.Email FROM Books LEFT JOIN Reservations ON Books.BookID = Reservations.BookID LEFT JOIN Users ON Reservations.UserID = Users.UserID WHERE Users.UserID = %s"
        values = (search_text,)
    elif search_text.startswith("LR"):
        sql = "SELECT Books.*, Reservations.ReservationDate, Users.Name, Users.Email FROM Books LEFT JOIN Reservations ON Books.BookID = Reservations.BookID LEFT JOIN Users ON Reservations.UserID = Users.UserID WHERE Reservations.ReservationID = %s"
        values = (search_text,)
    else:
        sql = "SELECT Books.*, Reservations.ReservationDate, Users.Name, Users.Email FROM Books LEFT JOIN Reservations ON Books.BookID = Reservations.BookID LEFT JOIN Users ON Reservations.UserID = Users.UserID WHERE Books.Title = %s"
        values = (search_text,)
    cursor.execute(sql, values)
    result = cursor.fetchone()
    if result:
        print("Book Details:")
        print("BookID:", result[0])
        print("Title:", result[1])
        print("Author:", result[2])
        print("ISBN:", result[3])
        print("Status:", result[4])
        print("Reservation Date:", result[5])
        print("User Name:", result[6])
        print("User Email:", result[7])
    else:
        print("Book not found")

# Find all the books in the database
def find_all_books():
    cursor = db.cursor()
    sql = "SELECT Books.*, Reservations.ReservationDate, Users.Name, Users.Email FROM Books LEFT JOIN Reservations ON Books.BookID = Reservations.BookID LEFT JOIN Users ON Reservations.UserID = Users.UserID"
    cursor.execute(sql)
    results = cursor.fetchall()
    if results:
        print("All Books:")
        for result in results:
            print("BookID:", result[0])
            print("Title:", result[1])
            print("Author:", result[2])
            print("ISBN:", result[3])
            print("Status:", result[4])
            print("Reservation Date:", result[5])
            print("User Name:", result[6])
            print("User Email:", result[7])
            print("------------------------")
    else:
        print("No books found")

# Modify/update book details based on BookID
def update_book_details():
    cursor = db.cursor()
    book_id = input("Enter the BookID: ")
    new_status = input("Enter the new book status: ")
    sql = "UPDATE Books SET Status = %s WHERE BookID = %s"
    values = (new_status, book_id)
    cursor.execute(sql, values)
    db.commit()
    print("Book details updated successfully")

# Delete a book based on its BookID
def delete_book():
    cursor = db.cursor()
    book_id = input("Enter the BookID: ")
    sql = "DELETE FROM Books WHERE BookID = %s"
    values = (book_id,)
    cursor.execute(sql, values)
    db.commit()
    print("Book deleted successfully")

# Main menu
def main_menu():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add a new book")
        print("2. Find a book's details")
        print("3. Find a book's reservation status")
        print("4. Find all books")
        print("5. Modify/update book details")
        print("6. Delete a book")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")
        if choice == "1":
            add_book()
        elif choice == "2":
            find_book_details()
        elif choice == "3":
            find_reservation_status()
        elif choice == "4":
            find_all_books()
        elif choice == "5":
            update_book_details()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

# Create tables if they don't exist
create_tables()

# Run the main menu
main_menu()

# Close the database connection
db.close()
