import sqlite3

def connect():
    conn= sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute ("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text , author text, year integer, isbn integer)")
    conn.commit()
    conn.close()


def insert (title, author , year, isbn):
    conn= sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
        conn= sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall() # stores all the values from the table and stores them in this varaible
        conn.close()
        return rows

def search(title = "", author= "", year="", isbn=""):
    conn= sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR ISBN = ?", (title,author,year,isbn))
    rows = cur.fetchall() # stores all the values from the table and stores them in this varaible
    conn.close()
    return rows

def delete(id):
    conn= sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?,author = ?, year=?, isbn=? WHERE id = ?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()




connect()
#insert("The Sun", "John Smith", 1945, 74035867303028)
#delete(6)

update(7,"The Moon", "Stephen Blaney", 2014, 123456789)
print(view())
print(search(author ="John Smith"))
