from sqlite3 import connect

Id = int(input("Id: "))
Ism = input("Ism: ")
Yosh = int(input("Yosh: "))
Univer = input("Univer: ")

with connect("talabalar.db") as test:
    cursor = test.cursor()
    cursor.execute(f"INSERT INTO studentlar VALUES('{Id}','{Ism}','{Yosh}','{Univer}')")
    cursor.execute('''
    SELECT * FROM studentlar;
    ''')
    print(cursor.fetchall())