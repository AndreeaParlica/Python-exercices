# Creaţi o bază de date cu tabelul Books a cărei câmpuri sunt:
# id – cheia primară;
# title – text;
# year – int.
#
# Permiteți ca utilizatorul să poată insera, din linia de comandă, prin funcţia input(), cărţi în baza de date ce au un id scris pe ele.
# De asemenea, oferiți-i utilizatorului posibilitatea de citire a tot ceea ce a fost inserat până în momentul
# respectiv în baza de date.

import sqlite3

conn = sqlite3.connect('assgn1_database_v1.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Books (
    bookId INT PRIMARY KEY,
    Title TEXT,
    Year INT);
""")
conn.commit()

# inserare carte noua
while True:
    question = input("Do you want to insert a new book? Y(YES)/N(NO):  ")
    if question.upper() == 'Y':
        try:
            insert_id_new_book = int(input('Please insert de ID Book: '))
            insert_title_new_book = input('Please insert Title of the book: ')
            insert_year_new_book = int(input('Please insert Year of the book: '))
            sql_comm = "INSERT INTO Books(bookId,Title,Year) VALUES (?, ?, ?)"
            cursor.execute(sql_comm, (insert_id_new_book, insert_title_new_book, insert_year_new_book))
        except ValueError:
            print("ERROR: Number must be inserted for the ID field and the Year field!!!")
        except sqlite3.IntegrityError:
            print("ID field must be unique, data inserted already exists")
    elif question.upper() == 'N':
        display_question = input('Do you want to display the all the books from the database? Y(YES)/N(NO):  ') # functionalitate de vizualizare imediat dupa o adaugare
        if display_question.upper() == 'Y':
            cursor.execute('SELECT * FROM Books;')
            results = cursor.fetchall()
            conn.commit()
            cursor.close()
            conn.close()
            for i in results:
                print(f"{i[0] : <5} {i[1] : <30} {i[2] : >10}")
        elif display_question.upper() == 'N':
            print('Thank you! Have a nice day!')
            break
        else:
            print('Answer not supported, please insert Y for Yes or N for No')
    else:
        print('Answer not supported, please insert Y for Yes or N for No')
